import pyautogui,time
from calculate import Calculate as c
from poweredRail import PoweredRail as pr

class Tunnel:
    
# x:  -x=e +x=w     y:  -y=d +y=u   z:  -z=n +z=s
    def __init__(self, cmd1, cmd2, userCoordinates, block1, block2, direction) -> None:
        c(userCoordinates, direction)
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
        
        pr(self, userCoordinates, self._longestAxis, self._directionOfTravel)
        beg=[userCoordinates[0],userCoordinates[1],userCoordinates[2],]
        end=[userCoordinates[3],userCoordinates[4],userCoordinates[5],]
        pr.generateRailCoordinates(self,beg,end,self._longestAxis,self._directionOfTravel)
        self._newCmds = self.calculateTunnelParameters(self._userCoordinates, self._directionOfTravel, self._cmd1, self._cmd2, self._block1, self._block2, self._longestAxis)
        # time.sleep(10)
        # self.typeWritter(self._newCmds)


    def generateCommand(self, cmd, userCoordinates, generatedCoordinates, block, axis):
        if userCoordinates == None or generatedCoordinates == None:
            return
        command = ""
        commands=[]
        if axis == 'x':
            for i in range(0,len(generatedCoordinates)-1):
                command = cmd+" "+str(generatedCoordinates[i])+" "+str(userCoordinates[1])+" "+str(userCoordinates[2])+" "+str(generatedCoordinates[i+1])+" "+str(userCoordinates[4])+" "+str(userCoordinates[5])+" "+block
                commands.append(command)
        elif axis == 'y':
            for i in range(0,len(generatedCoordinates)-1):
                command = cmd+" "+str(userCoordinates[0])+" "+str(generatedCoordinates[i])+" "+str(userCoordinates[2])+" "+str(userCoordinates[3])+" "+str(generatedCoordinates[i+1])+str(userCoordinates[5])+" "+block
                commands.append(command)
        elif axis == 'z':
            for i in range(0,len(generatedCoordinates)-1):
                command = cmd+" "+str(userCoordinates[0])+" "+str(userCoordinates[1])+" "+str(generatedCoordinates[i])+" "+str(userCoordinates[3])+" "+str(userCoordinates[4])+" "+str(generatedCoordinates[i+1])+" "+block
                commands.append(command)
        return commands


    def createTeleportCoords(self, userCoordinates, generatedCoordinates, axis, dir):
        if userCoordinates is None or generatedCoordinates is None:
            return
        tpc=[]
        for i in range(len(generatedCoordinates)):
            if axis == 'z':
                if dir == 'n':
                    if i == len(generatedCoordinates)-1:
                        return tpc
                    tpc.append('teleport @p '+ str(userCoordinates[0])+ " " + str(userCoordinates[4])+ " " + str((generatedCoordinates[i+1]+1))) 
                elif dir == 's':
                    tpc.append('teleport @p '+ str(userCoordinates[0])+ " " + str(userCoordinates[4])+ " " + str((generatedCoordinates[i]-1)))
            elif axis == 'x':
                if dir == 'e':
                    tpc.append('teleport @p '+ str((generatedCoordinates[i]))+ " " + str(userCoordinates[4]) + " " + str((userCoordinates[2]+1)))
                elif dir == 'w':
                    tpc.append('teleport @p '+ str((generatedCoordinates[i]))+ " " + str(userCoordinates[4]) + " " + str(userCoordinates[2]))
        return tpc
        

    def writeToFile(self,cmds1,cmds2,cmds3,):
        newCmds = []
        fh = open("commands.txt",'w')
        for i in range(len(cmds2)):
            newCmds.append(cmds1[i])
            newCmds.append(cmds2[i])
            newCmds.append(cmds3[i])
            l1 = len(cmds1)
            l2 = len(cmds2)
            l3 = len(cmds3)
            fh.writelines(cmds1[i]+'\n')
            fh.writelines(cmds2[i]+'\n')
            fh.writelines(cmds3[i]+'\n')
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
        self._tunnelHollowingCoordinates = c.generateCoordinates(self, userCoordinates, longestAxis, dir, 100, 100)
        self._tunnelHollowingCommands = self.generateCommand(cmd1, userCoordinates, self._tunnelHollowingCoordinates, block1, longestAxis)
                
        self._tunnelLinningCoordinates = c.generateCoordinates(self, self._tunnelLinning, longestAxis, dir, 100, 100)
        self._tunnelLinningCommands = self.generateCommand(cmd2, self._tunnelLinning, self._tunnelLinningCoordinates, block2, longestAxis)
        self._teleportCommands = self.createTeleportCoords(userCoordinates, self._tunnelHollowingCoordinates, longestAxis, dir)
        cmds = self.combineCommands(self._teleportCommands, self._tunnelLinningCommands, self._tunnelHollowingCommands)
        self.writeToFile(self._teleportCommands, self._tunnelLinningCommands, self._tunnelHollowingCommands)
        self.typeWritter(cmds)

    def typeWritter(self, newCmds):
        time.sleep(10)
        delay = 5
        for i in range(len(newCmds)):
            print(newCmds[i])
            pyautogui.press(['/'])
            pyautogui.typewrite(newCmds[i],interval=0.01)
            pyautogui.press(['enter'])
            time.sleep(delay)
