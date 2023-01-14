import pyautogui,time
class Tunnel:
    _directionOfTravel=''
    _coordinates=[]
    _coordinates2=[]
    _generatedCoordinates = []
    _generatedCoordinates2 = []
    _generatedCommands = []
    _generatedCommands2 = []
    _cmd1=''
    _cmd2=''
    _axis=[]
    _block1=''
    _block2=''
    _teleportCoordinates=[]
    _newCmds=[]

# x:  -x=e +x=w     y:  -y=d +y=u   z:  -z=n +z=s
    def __init__(self, cmd1, cmd2, coordinates, block1, block2, direction) -> None:
        self._coordinates = coordinates
        self._directionOfTravel = direction.lower()
        self._cmd1 = cmd1
        self._cmd2 = cmd2
        self._block1 = block1
        self._block2 = block2
        self._coordinates = self.sortCoordinates(coordinates)
        self._newCmds = self.calculateTunnelParameters(self._coordinates,self._directionOfTravel,self._cmd1,self._cmd2,self._block1,self._block2)
        time.sleep(10)
        self.typeWritter(self._newCmds)

    def calculateLinedTunnelCoordinates(self, coordinates, dir):
        temp=[0,0,0,0,0,0]
        # x:  -x=e +x=w     y:  -y=d +y=u   z:  -z=n +z=s
        for i in range(len(coordinates)):
            if dir == 'n' or dir == 's':
                temp[2] = coordinates[2]
                temp[5] = coordinates[5]
                if i == 4 or i == 3:
                    temp[i] = coordinates[i]-1
                elif i == 0 or i == 1:
                    if coordinates[i] > 0:
                        temp[i]=coordinates[i]+1
                    else:
                        temp[i]=coordinates[i]-1
        
            elif dir == 'e' or dir == 'w':
                temp[0] = coordinates[0]
                temp[3] = coordinates[3]
                if i == 4:
                    temp[i]=coordinates[i]-1
                elif i == 1 or i == 2 or i == 5:
                    if coordinates[i] > 0:
                        temp[i]=coordinates[i]+1
                    else:
                        temp[i]=coordinates[i]-1        
        return temp


# returns the longest axis 
    def findLongestAxis(self, axis):
        largest=''
        if (axis[0] >= axis[1]) and (axis[0]>=axis[2]):
            largest = 'x'
        elif(axis[1]>=axis[0] and (axis[1]>=axis[2])):
            largest = 'y'
        else:
            largest = 'z'
        return largest


    #sorts coordinates highest to lowest mainly to standardize the mather operations
    def sortCoordinates(self,coordinates):
        for i in range(0,3):
            temp = coordinates[i]
            if temp < coordinates[i+3]:
                coordinates[i] = coordinates[i+3]
                coordinates[i+3] = temp
        return coordinates


    #calculates the volume of the area to be worked
    def calculateVolume(self, coordinates):
        self._axis.append (coordinates[0] - coordinates[3])
        self._axis.append(coordinates[1] - coordinates[4])
        self._axis.append(coordinates[2] - coordinates[5])
        return ((self._axis[0]+1)*(self._axis[1]+1)*(self._axis[2]+1))


    def generateNegativeCoords(self, coordinates, axis, dir):
        distance = 100
        temp = []
        if axis == 'x':
            remainder = self._axis[0]%distance
            coord1 = coordinates[0]
            coord2 = coordinates[3]
        elif axis == 'y':
            remainder = self._axis[1]%distance
            coord1 = coordinates[1]
            coord2 = coordinates[4]

        elif axis == 'z':
            remainder = self._axis[2]%distance
            coord1 = coordinates[2]
            coord2 = coordinates[5]

        # the code below will calculate northward travels
        if remainder != 0:
            for coord in range(coord1, coord2,-distance):
                temp.append(coord)
            
            temp.append(temp[len(temp)-1]-remainder)
        else:
            for coord in range(coord1, coord2,-distance):
                temp.append(coord)
        return temp


    def generatePositiveCoords(self,coordinates, axis, dir):
        distance = 100
        temp=[]
        if axis == 'x':
            remainder = self._axis[0]%distance
            coord1 = coordinates[0]
            coord2 = coordinates[3]
        elif axis == 'y':
            remainder = self._axis[1]%distance
            coord1 = coordinates[1]
            coord2 = coordinates[4]

        elif axis == 'z':
            remainder = self._axis[2]%distance
            coord1 = coordinates[2]
            coord2 = coordinates[5]

        if remainder != 0:
            for coord in range(coord1, coord2, -distance):
                temp.append(coord)
            temp.append(temp[len(temp)-1]-remainder)
        else:
            if dir == 'n' or dir == 'w':
                for coord in range(coord1, coord2, distance):
                    temp.append(coord)
            elif dir == 's' or dir == 'e':
                for coord in range(coord1, coord2, -distance):
                    temp.append(coord)
        return temp


    def generateCommand(self, cmd, Coordinates, genCoordinates, block, axis):
        command = ""
        commands=[]

        if axis == 'x':
            for i in range(0,len(genCoordinates)-1):
                command = cmd+" "+str(genCoordinates[i])+" "+str(Coordinates[1])+" "+str(Coordinates[2])+" "+str(genCoordinates[i+1])+" "+str(Coordinates[4])+" "+str(Coordinates[5])+" "+block
                commands.append(command)
        elif axis == 'y':
            for i in range(0,len(genCoordinates)-1):
                command = cmd+" "+str(Coordinates[0])+" "+str(genCoordinates[i])+" "+str(Coordinates[2])+" "+str(Coordinates[3])+" "+str(genCoordinates[i+1])+str(Coordinates[5])+" "+block
                commands.append(command)
        elif axis == 'z':
            for i in range(0,len(genCoordinates)-1):
                command = cmd+" "+str(Coordinates[0])+" "+str(Coordinates[1])+" "+str(genCoordinates[i])+" "+str(Coordinates[3])+" "+str(Coordinates[4])+" "+str(genCoordinates[i+1])+" "+block
                commands.append(command)
        return commands


    '''supposed to generate the
    increments for tunnel boring'''
    def generateCoordinates(self,coordinates, longestAxis, dir):
        temp = []
        if dir == 'n':#-z
            temp = self.generateNegativeCoords(coordinates,longestAxis,dir)
        elif dir == 's':#+z
            temp = self.generatePositiveCoords(coordinates,longestAxis,dir)
        elif dir == 'e':#+x
            temp = self.generatePositiveCoords(coordinates,longestAxis,dir)
        elif dir == 'w':#-x
            temp = self.generateNegativeCoords(coordinates,longestAxis,dir)
        elif dir == 'u':#+y
            temp = self.generatePositiveCoords(coordinates,longestAxis,dir)
        elif dir == 'd':#-y
            temp = self.generateNegativeCoords(coordinates,longestAxis,dir)
        return temp


    def createTeleportCoords(self, coordinates, generatedCoordinates, axis, dir):
        tpc=[]
        for i in range(len(generatedCoordinates)):
            if axis == 'z':
                if dir == 'n':
                    if i == len(generatedCoordinates)-1:
                        return tpc
                    tpc.append('teleport @p '+ str(coordinates[0])+ " " + str(coordinates[4])+ " " + str((generatedCoordinates[i+1]+1)))
                    
                elif dir == 's':
                    tpc.append('teleport @p '+ str(coordinates[0])+ " " + str(coordinates[4])+ " " + str((generatedCoordinates[i]-1)))
            elif axis == 'x':
                if dir == 'e':
                    tpc.append('teleport @p '+ str((generatedCoordinates[i]))+ " " + str(coordinates[4]) + " " + str((coordinates[2]+1)))
                elif dir == 'w':
                    tpc.append('teleport @p '+ str((generatedCoordinates[i]))+ " " + str(coordinates[4]) + " " + str(coordinates[2]))

        return tpc


    def writeToFile(self,cmds):
        newCmds = cmds
        fh = open("commands.txt",'w')
        for i in range(len(self._generatedCommands2)):
            
            fh.writelines(self._teleportCoordinates[i])
            fh.writelines(self._generatedCommands2[i])
            fh.writelines(self._generatedCommands[i])
            
        fh.close()


    def calculateTunnelParameters(self, coordinates, dir, cmd1, cmd2, block1, block2):
        volume = self.calculateVolume(coordinates)
        print("volumetric displacement: " + str(volume) + " blocks to be replaced")
        longestAxis = self.findLongestAxis(self._axis)
        self._coordinates2 = self.calculateLinedTunnelCoordinates(coordinates,dir)
        self._generatedCoordinates2 = self.generateCoordinates(self._coordinates2,longestAxis,dir)
        self._generatedCommands2 = self.generateCommand(cmd2,self._coordinates2, self._generatedCoordinates2,block2,longestAxis)
        self._generatedCoordinates = self.generateCoordinates(coordinates,longestAxis,dir)
        self._teleportCoordinates = self.createTeleportCoords(coordinates,self._generatedCoordinates,longestAxis, dir)
        self._generatedCommands = self.generateCommand(cmd1,coordinates, self._generatedCoordinates,block1,longestAxis)
        newCmds=[]
        for i in range(len(self._generatedCommands2)):
            newCmds.append(self._teleportCoordinates[i])
            newCmds.append(self._generatedCommands2[i])
            newCmds.append(self._generatedCommands[i])
        self.writeToFile(newCmds)
        return newCmds
        

    def typeWritter(self, newCmds):
        time.sleep(10)
        delay = 5
        for i in range(len(newCmds)):
            print(newCmds[i])
            #pyperclip.copy(newCmds[i])
            pyautogui.press(['/'])
            pyautogui.typewrite(newCmds[i],interval=0.01)
            pyautogui.press(['enter'])
            time.sleep(delay)
