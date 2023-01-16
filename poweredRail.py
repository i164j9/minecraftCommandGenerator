from calculate import Calculate as c

class PoweredRail:
    def __init__(self, generatedCoordsinningCoordinates, endingCoordinates, longestAxis, dir):
        self._generatedCoordsCoords = generatedCoordsinningCoordinates
        self._endCoords = endingCoordinates
        self._longestAxis = longestAxis
        self._dir = dir


    def generateRailCoordinates(self, coords, longestAxis, dir):
        railCoords = []
        temp = []
        for rc in range(len(railCoords)-1):
            if longestAxis == 'x':
                if dir == 'w':
                    railCoords = c.generateNegativeCoords(self, coords, longestAxis, dir)
                    temp.append([railCoords[rc],coords[1],coords[2],railCoords[rc+1],coords[1],coords[2]])
                elif dir == 'e':
                    railCoords = c.generatePositiveCoords(self, coords, longestAxis, dir)
                    temp.append([railCoords[rc],coords[1],coords[2],railCoords[rc+1],coords[1],coords[2]])
            elif longestAxis == 'y':
                if dir == 'd':
                    railCoords = c.generateNegativeCoords(self, coords, longestAxis, dir)
                    temp.append([coords[0],railCoords[rc],coords[2],coords[0],railCoords[rc+1],coords[2]])
                elif dir == 'u':
                    railCoords = c.generatePositiveCoords(self, coords, longestAxis, dir)
                    temp.append([coords[0],railCoords[rc],coords[2],coords[0],railCoords[rc+1],coords[2]])
            elif longestAxis == 'z':
                if dir == 'n':
                    railCoords = c.generateNegativeCoords(self, coords, longestAxis, dir)
                    temp.append([coords[0],coords[1],railCoords[rc],coords[0],coords[1],railCoords[rc+1]])
                elif dir == 's':
                    railCoords = c.generatePositiveCoords(self, coords, longestAxis, dir)
                    temp.append([coords[0],coords[1],railCoords[rc],coords[0],coords[1],railCoords[rc+1]])
        return temp


    def generateRailCommands(self, genRailCoords):
        commands=[]
        for coord in genRailCoords:
            command = "fill"+" "+str(coord[0])+" "+str(coord[1])+" "+str(coord[2])+" "+str(coord[3])+" "+str(coord[4])+" "+str(coord[5])+" "+"minecraft:powered_rail"
            commands.append(command)
        return commands


    def calculatePSUcoords(self, coordinates, generatedCoords, axis, dir):
        coord1=0
        coord2=0
        coords=[]
        if axis == 'x':
            if dir == 'w':
                
                for i in generatedCoords:
                    coord = [coord1, (coordinates[4]-1), coordinates[2]]
                    coords.append(coord)
                    coord1-=10
            elif dir == 'e':
                
                for i in generatedCoords:
                    coord = [coord1, (coordinates[4]-1), coordinates[2]]
                    coords.append(coord)
                    coord1+=10
        elif axis == 'y':
            if dir == 'd':
                
                for i in generatedCoords:
                    coord = [coordinates[0], coord1, coordinates[2]]
                    coords.append(coord)
                    coord1-=10
            elif dir == 'u':
                
                for i in generatedCoords:
                    coord = [coordinates[0], coord1, coordinates[2]]
                    coords.append(coord)
                    coord1+=10
        elif axis == 'z':
            if dir == 'n':
                
                for i in generatedCoords:
                    coord = [coordinates[0], (coordinates[4]-1), coord1]
                    coords.append(coord)
                    coord1-=10
            elif dir == 's':
                
                for i in generatedCoords:
                    coord = [coordinates[0], (coordinates[4]-1), coord1]
                    coords.append(coord)
                    coord1+=10
        return coords


    # returns 3 commands
    # makes commands for a redstone power source under ground for powered rail
    # this takes a single coordinate <x,y,z>
    def redStonePSU(self,coordinates):
        base=[]
        torch=[]
        commands=[]
        for coordinate in coordinates:
            surface=coordinate
            torch.append(coordinate[0])
            torch.append((coordinate[1]-1))
            torch.append(coordinate[2])
            base.append(coordinate[0]+1)
            base.append((coordinate[1]-2))
            base.append((coordinate[2]-1))
            base.append((coordinate[0]-1))
            base.append((coordinate[1])-1)
            base.append(coordinate[2]+1)
            command1 = 'fill'+" "+str(base[0])+" "+str(base[1])+" "+str(base[2])+" "+str(base[3])+" "+str(base[4])+" "+str(base[5])+" "+'minecraft:obsidian'
            command2 = 'fill'+" "+str(torch[0])+" "+str(torch[1])+" "+str(torch[2])+" "+str(torch[0])+" "+str(torch[1])+" "+str(torch[2])+" "+'minecraft:redstone_torch'
            command3 = 'fill'+" "+str(surface[0])+" "+str(surface[1])+" "+str(surface[2])+" "+str(surface[0])+" "+str(surface[1])+" "+str(surface[2])+" "+'minecraft:obsidian'
            commands.append([command1,command2,command3])
            base=[]
            torch=[]
        return commands
