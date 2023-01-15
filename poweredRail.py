from calculate import Calculate as c

class PoweredRail:
    def __init__(self, beginningCoordinates, endingCoordinates, longestAxis, dir):
        self._begCoords = beginningCoordinates
        self._endCoords = endingCoordinates
        self._longestAxis = longestAxis
        self._dir = dir
    

    def generateRailCoordinates(self, beg, end, longestAxis, dir):
        railCoords = []
        if longestAxis == 'x':
            if dir == 'w':
                railCoords = c.generateNegativeCoords(self, beg, longestAxis, dir, 100, 3000000)
                coords=[]
                for rc in railCoords:
                    coords.append([rc,beg[1],beg[2]])

                t = 'b'
            elif dir == 'e':
                c.generatePositiveCoords()
        elif longestAxis == 'y':
            if dir == 'd':
                railCoords.append(c.generateNegativeCoords(self, beg, longestAxis, dir, 100, 100))
            elif dir == 'u':
                c.generatePositiveCoords()
        elif longestAxis == 'z':
            if dir == 'n':
                railCoords.append(c.generateNegativeCoords(self, beg, longestAxis, dir, 100, 100))
            elif dir == 's':
                c.generatePositiveCoords()

    def generateRailCommands(self):
        pass


    def calculatePSUcoords(self):
        pass

    
    def generatePSUCommands(self):
        pass

    # returns 3 commands
    # makes commands for a redstone power source under ground for powered rail
    def redStonePSU(self,coordinates):
        base=[]
        torch=[]
        surface=coordinates
        torch.append(coordinates[0])
        torch.append((coordinates[1]-1))
        torch.append(coordinates[2])
        base.append(coordinates[0]+1)
        base.append((coordinates[1]-2))
        base.append(coordinates[2]-1)
        base.append(coordinates[0]-1)
        base.append((coordinates[1])-1)
        base.append(coordinates[2]+1)
        command1 = 'fill'+" "+str(base[0])+" "+str(base[1])+" "+str(base[2])+" "+str(base[3])+" "+str(base[4])+" "+str(base[5])+" "+'minecraft:obsidian'
        command2 = 'fill'+" "+str(torch[0])+" "+str(torch[1])+" "+str(torch[2])+" "+str(torch[0])+" "+str(torch[1])+" "+str(torch[2])+" "+'minecraft:redstone_torch'
        command3 = 'fill'+" "+str(surface[0])+" "+str(surface[1])+" "+str(surface[2])+" "+str(surface[0])+" "+str(surface[1])+" "+str(surface[2])+" "+'minecraft:obsidian'
        return command1, command2, command3

    # 30000,45,9, -30000,45,9
    def layRail(self,coordinates,longestAxis,dir):
        commands = []
        teleport =[]
        teleportCommand =[]
        PSUcoords=[]
        PSUcommands=[]
        psu=[]
        coord=[]

        PSUincrements = self.generateCoordinates(coordinates,longestAxis,dir,9)
        for inc in PSUincrements:
            tpc = str(inc)+ " " +str(coordinates[1])+ " " +str(coordinates[2])
            teleport.append(tpc)
            teleportCommand.append(self.createTeleportCoords(coordinates,teleport,longestAxis,dir))
            PSUcoords.append([inc, coordinates[1], coordinates[2], inc, coordinates[1], coordinates[2]])
        
        for i in range(len(PSUcoords)):
            PSUcommands.append(self.redStonePSU(PSUcoords,dir))
        
        for c in PSUcoords:
            psu.append(self.redStonePSU(PSUcoords,dir))
        railCoords = self.generateCoordinates(coordinates,longestAxis,dir)
        railCommands=self.generateCommand('fill',coordinates,railCoords,'minecraft:powered_rail',longestAxis)
