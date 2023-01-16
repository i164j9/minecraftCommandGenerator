import pyautogui,time
from calculate import Calculate as c
from poweredRail import PoweredRail as pr

class Tunnel:
    
# x:  -x=e +x=w     y:  -y=d +y=u   z:  -z=n +z=s
    def __init__(self, cmd1, cmd2, userCoordinates, block1, block2, direction) -> None:
        self._directionOfTravel=''
        self._tunnelLinning = []
        self._tunnelHollowingCoordinates = []
        self._tunnelLinningCommands = []
        self._tunnelLinningCoordinates = []
        self._tunnelHollowingCommands = []
        self._teleportCommands=[]
        self._axis=[]
        self._teleportCoordinates=[]
        self._newCmds=[]
        
        self._userCoordinates = userCoordinates
        self._directionOfTravel = direction.lower()
        self._cmd1 = cmd1
        self._cmd2 = cmd2
        self._block1 = block1
        self._block2 = block2
        
        self._userCoordinates = c.sortCoordinates(self, self._userCoordinates)
        self._volume = c.calculateVolume(self, self._userCoordinates)
        self._longestAxis = c.findLongestAxis(self, self._axis)

        self._newCmds = self.calculateTunnelParameters(self._userCoordinates, self._directionOfTravel, self._cmd1, self._cmd2, self._block1, self._block2, self._longestAxis)


    def coordinateBuilder(self,userCoordinates, generatedCoordinates, axis, type='std'):
        temp=[]

        if type == 'std':
            for i in range(len(generatedCoordinates)-1):
                if axis == 'x':
                    temp.append([generatedCoordinates[i],userCoordinates[1],userCoordinates[2],generatedCoordinates[i+1],userCoordinates[4],userCoordinates[5]])
                elif axis == 'y':
                    temp.append([userCoordinates[0],generatedCoordinates[i],userCoordinates[2],userCoordinates[3],generatedCoordinates[i+1],userCoordinates[5]])
                elif axis == 'z':
                    temp.append([userCoordinates[0],userCoordinates[1],generatedCoordinates[i],userCoordinates[3],userCoordinates[4],generatedCoordinates[i+1]])
        elif type == 'tele':
            for i in range(len(generatedCoordinates)-1):
                if axis == 'x':
                    temp.append([generatedCoordinates[i],userCoordinates[1],userCoordinates[2]])
                elif axis == 'y':
                    temp.append([userCoordinates[0],generatedCoordinates[i],userCoordinates[2]])
                elif axis == 'z':
                    temp.append([userCoordinates[0],userCoordinates[1],generatedCoordinates[i]])
        elif type == 'rail':
            for i in range(len(generatedCoordinates)-1):
                if axis == 'x':
                    temp.append([generatedCoordinates[i],userCoordinates[1],userCoordinates[2],generatedCoordinates[i+1],userCoordinates[1],userCoordinates[2]])
                elif axis == 'y':
                    temp.append([userCoordinates[0],generatedCoordinates[i],userCoordinates[2],userCoordinates[0],generatedCoordinates[i+1],userCoordinates[2]])
                elif axis == 'z':
                    temp.append([userCoordinates[0],userCoordinates[1],generatedCoordinates[i],userCoordinates[0],userCoordinates[1],generatedCoordinates[i+1]])
        return temp


    def generateCommand(self, cmd, generatedCoordinates, block, axis):
        if generatedCoordinates == None:
            return
        commands=[]
        for i in range(0,len(generatedCoordinates)-1):
            # if axis == 'x':
            #     commands.append(cmd+" "+str(generatedCoordinates[i])+" "+str(userCoordinates[1])+" "+str(userCoordinates[2])+" "+str(generatedCoordinates[i+1])+" "+str(userCoordinates[4])+" "+str(userCoordinates[5])+" "+block)
            # elif axis == 'y':
            #     commands.append(cmd+" "+str(userCoordinates[0])+" "+str(generatedCoordinates[i])+" "+str(userCoordinates[2])+" "+str(userCoordinates[3])+" "+str(generatedCoordinates[i+1])+str(userCoordinates[5])+" "+block)
            # elif axis == 'z':
            commands.append(cmd+" "+str(generatedCoordinates[i][0])+" "+str(generatedCoordinates[i][1])+" "+str(generatedCoordinates[i][2])+" "+str(generatedCoordinates[i][3])+" "+str(generatedCoordinates[i][4])+" "+str(generatedCoordinates[i][5])+" "+block)
        return commands


    def generateTeleportCommands(self, generatedCoordinates):
        if generatedCoordinates is None:
            return
        temp=[]
        for i in range(len(generatedCoordinates)-1):
            # if axis == 'x':
            temp.append('teleport @p '+ str((generatedCoordinates[i][0]))+ " " + str(generatedCoordinates[i][1]) + " " + str(generatedCoordinates[i][2]))
            # elif axis == 'y':
            #     temp.append('teleport @p '+ str(userCoordinates[0]) + " " + str((generatedCoordinates[i])) + " " + str(userCoordinates[2]))
            # elif axis == 'z':
            #     temp.append('teleport @p '+ str(userCoordinates[0])+ " " + str(userCoordinates[1]) + " " + str((generatedCoordinates[i])))
        return temp
        

    def writeToFile(self,cmds1,cmds2,cmds3):
        newCmds = []
        fh = open("commands.txt",'w')
        for i in range(len(cmds2)):
            fh.writelines(str(cmds1[i])+'\n')
            fh.writelines(str(cmds2[i])+'\n')
            fh.writelines(str(cmds3[i])+'\n')
        fh.close()


    def writeToFile(self,cmds1,):
        newCmds = []
        fh = open("commands.txt",'w')
        for i in range(len(cmds1)):
            fh.writelines(str(cmds1[i])+'\n')
        fh.close()


    def combineCommands(self,cmds1,cmds2,cmds3,):
        newCmds = []
        for i in range(len(cmds2)):
            newCmds.append(cmds1[i])
            newCmds.append(cmds2[i])
            newCmds.append(cmds3[i])
        return newCmds

    def calculateTunnelParameters(self, userCoordinates, dir, cmd1, cmd2, block1, block2, longestAxis):
        newCmds=[]
        print("volumetric displacement: " + str(self._volume) + " blocks to be replaced")
        self._tunnelLinning = c.calculateLinedTunnelCoordinates(self, userCoordinates, dir)
        self._tunnelHollowingCoordinates = c.generateCoordinates(self, userCoordinates, longestAxis, dir)
        coordBuild = self.coordinateBuilder(userCoordinates,self._tunnelHollowingCoordinates,longestAxis)
        self._tunnelHollowingCommands = self.generateCommand(cmd1, coordBuild, block1, longestAxis)
                
        self._tunnelLinningCoordinates = c.generateCoordinates(self, self._tunnelLinning, longestAxis, dir)
        coordBuild = self.coordinateBuilder(self._tunnelLinning,self._tunnelLinningCoordinates,longestAxis)
        self._tunnelLinningCommands = self.generateCommand(cmd2, coordBuild, block2, longestAxis)
        
        coordBuild = self.coordinateBuilder(userCoordinates,self._tunnelLinningCoordinates,longestAxis,'tele')
        self._teleportCommands = self.generateTeleportCommands(coordBuild)
        cmds = self.combineCommands(self._teleportCommands, self._tunnelLinningCommands, self._tunnelHollowingCommands)
        
        rc = pr.generateRailCoordinates(self,userCoordinates,self._longestAxis,self._directionOfTravel)
        cmds = pr.generateRailCommands(self,rc)
        
        psc1 = rc = c.generateCoordinates(self,userCoordinates,self._longestAxis,self._directionOfTravel,10)
        psc = pr.calculatePSUcoords(self,userCoordinates, psc1, self._longestAxis, self._directionOfTravel)
        psu = pr.redStonePSU(self,psc)
        
        tele = self.generateTeleportCommands(psc)
        
        #self.writeToFile(self._teleportCommands, self._tunnelLinningCommands, self._tunnelHollowingCommands)

        time.sleep(10)
        self.typeWritter(cmds)

    def typeWritter(self, newCmds):
        time.sleep(10)
        delay = 5
        for i in range(len(newCmds)):
            print(newCmds[i])
            pyautogui.press(['esc'])
            pyautogui.press(['/'])
            pyautogui.typewrite(newCmds[i],interval=0.01)
            pyautogui.press(['enter'])
            time.sleep(delay)
