class Calculate:
    def __init__(self, userCoordinates, direction ) -> None:
        self._axis=[]
        self._direction = direction
        self._volume = self.calculateVolume(userCoordinates)
        self._longestAxis = self.findLongestAxis(self._axis)


    def calculateLinedTunnelCoordinates(self, userCoordinates, dir):
        if userCoordinates is None or len(userCoordinates) < 6:
            return
        temp=[0,0,0,0,0,0]
        # x:  -x=e +x=w     y:  -y=d +y=u   z:  -z=n +z=s
        for i in range(len(userCoordinates)):
            if dir == 'n' or dir == 's':
                temp[2] = userCoordinates[2]
                temp[5] = userCoordinates[5]
                if i == 4 or i == 3:
                    temp[i] = userCoordinates[i]-1
                elif i == 0 or i == 1:
                    if userCoordinates[i] > 0:
                        temp[i]=userCoordinates[i]+1
                    else:
                        temp[i]=userCoordinates[i]-1
        
            elif dir == 'e' or dir == 'w':
                temp[0] = userCoordinates[0]
                temp[3] = userCoordinates[3]
                if i == 4:
                    temp[i]=userCoordinates[i]-1
                elif i == 1 or i == 2 or i == 5:
                    if userCoordinates[i] > 0:
                        temp[i]=userCoordinates[i]+1
                    else:
                        temp[i]=userCoordinates[i]-1        
        return temp


# returns the longest axis 
    def findLongestAxis(self, axis):
        if axis is None or len(axis) < 3:
            return ''
        largest=''
        if (axis[0] >= axis[1]) and (axis[0]>=axis[2]):
            largest = 'x'
        elif(axis[1]>=axis[0] and (axis[1]>=axis[2])):
            largest = 'y'
        else:
            largest = 'z'
        return largest


    #sorts userCoordinates highest to lowest mainly to standardize the mather operations
    def sortCoordinates(self, userCoordinates):
        if len(userCoordinates) < 6:
            return
        for i in range(0,3):
            temp = userCoordinates[i]
            if temp < userCoordinates[i+3]:
                userCoordinates[i] = userCoordinates[i+3]
                userCoordinates[i+3] = temp
        return userCoordinates


    #calculates the volume of the area to be worked
    def calculateVolume(self, userCoordinates):
        if userCoordinates is None or len(userCoordinates) < 6:
            return 0
        self._axis.append (userCoordinates[0] - userCoordinates[3])
        self._axis.append(userCoordinates[1] - userCoordinates[4])
        self._axis.append(userCoordinates[2] - userCoordinates[5])
        return ((self._axis[0]+1)*(self._axis[1]+1)*(self._axis[2]+1))


    # def generateNegativeCoords(self, userCoordinates, axis, dir, increments):
    #     distance = increments
    #     temp = []
    #     if axis == 'x':
    #         remainder = self._axis[0]%distance
    #         coord1 = userCoordinates[0]
    #         coord2 = userCoordinates[3]
    #     elif axis == 'y':
    #         remainder = self._axis[1]%distance
    #         coord1 = userCoordinates[1]
    #         coord2 = userCoordinates[4]
    #     elif axis == 'z':
    #         remainder = self._axis[2]%distance
    #         coord1 = userCoordinates[2]
    #         coord2 = userCoordinates[5]
    #     # the code below will calculate northward travels
    #     if remainder != 0:
    #         for coord in range(coord1, coord2,-distance):
    #             temp.append(coord)
    #         temp.append(temp[len(temp)-1]-remainder)
    #     else:
    #         for coord in range(coord1, coord2,-distance):
    #             temp.append(coord)
    #     return temp


    def generateNegativeCoords(self, userCoordinates, axis, dir, increments, distance):
        remainder = 0
        coord1 = 0
        coord2 = 0

        if len(userCoordinates) == 3:
            if axis == 'x':
                if dir == 'w':
                    userCoordinates.append(userCoordinates[0]-distance)
                    userCoordinates.append(userCoordinates[1])
                    userCoordinates.append(userCoordinates[2])
                elif dir == 'e':
                    userCoordinates.append(userCoordinates[0]+distance)
                    userCoordinates.append(userCoordinates[1])
                    userCoordinates.append(userCoordinates[1])
            elif axis == 'y':
                if dir == 'd':
                    userCoordinates.append(userCoordinates[0])
                    userCoordinates.append(userCoordinates[1]-distance)
                    userCoordinates.append(userCoordinates[2])
                elif dir == 'u':
                    userCoordinates.append(userCoordinates[0])
                    userCoordinates.append(userCoordinates[1]+distance)
                    userCoordinates.append(userCoordinates[1])
            elif axis == 'z':
                if dir == 'n':
                    userCoordinates.append(userCoordinates[0])
                    userCoordinates.append(userCoordinates[1])
                    userCoordinates.append(userCoordinates[2]-distance)
                elif dir == 's':
                    userCoordinates.append(userCoordinates[0])
                    userCoordinates.append(userCoordinates[1])
                    userCoordinates.append(userCoordinates[1]+distance)
            print(userCoordinates)

        temp = []
        if axis == 'x':
            remainder = self._axis[0]%increments
            coord1 = userCoordinates[0]
            coord2 = userCoordinates[3]
        elif axis == 'y':
            remainder = self._axis[1]%increments
            coord1 = userCoordinates[1]
            coord2 = userCoordinates[4]
        elif axis == 'z':
            remainder = self._axis[2]%increments
            coord1 = userCoordinates[2]
            coord2 = userCoordinates[5]
        # the code below will calculate northward travels
        if remainder != 0:
            for coord in range(coord1, coord2,-increments):
                temp.append(coord)
            temp.append(temp[len(temp)-1]-remainder)
        else:
            for coord in range(coord1, coord2,-increments):
                temp.append(coord)
        return temp


    # def generatePositiveCoords(self, userCoordinates, axis, dir, distance):
    #     temp=[]
    #     if axis == 'x':
    #         remainder = self._axis[0]%distance
    #         coord1 = userCoordinates[0]
    #         coord2 = userCoordinates[3]
    #     elif axis == 'y':
    #         remainder = self._axis[1]%distance
    #         coord1 = userCoordinates[1]
    #         coord2 = userCoordinates[4]
    #     elif axis == 'z':
    #         remainder = self._axis[2]%distance
    #         coord1 = userCoordinates[2]
    #         coord2 = userCoordinates[5]
    #     if remainder != 0:
    #         for coord in range(coord1, coord2, -distance):
    #             temp.append(coord)
    #         temp.append(temp[len(temp)-1]-remainder)
    #     else:
    #         if dir == 'n' or dir == 'w':
    #             for coord in range(coord1, coord2, distance):
    #                 temp.append(coord)
    #         elif dir == 's' or dir == 'e':
    #             for coord in range(coord1, coord2, -distance):
    #                 temp.append(coord)
    #     return temp


    def generatePositiveCoords(self, userCoordinates, axis, dir, increments, distance):
        if axis == 'x':
            if dir == 'w':
                userCoordinates.append(userCoordinates[0]-distance)
                userCoordinates.append(userCoordinates[1])
                userCoordinates.append(userCoordinates[2])
            elif dir == 'e':
                userCoordinates.append(userCoordinates[0]+distance)
                userCoordinates.append(userCoordinates[1])
                userCoordinates.append(userCoordinates[1])
        elif axis == 'y':
            if dir == 'd':
                userCoordinates.append(userCoordinates[0])
                userCoordinates.append(userCoordinates[1]-distance)
                userCoordinates.append(userCoordinates[2])
            elif dir == 'u':
                userCoordinates.append(userCoordinates[0])
                userCoordinates.append(userCoordinates[1]+distance)
                userCoordinates.append(userCoordinates[1])
        elif axis == 'z':
            if dir == 'n':
                userCoordinates.append(userCoordinates[0])
                userCoordinates.append(userCoordinates[1])
                userCoordinates.append(userCoordinates[2]-distance)
            elif dir == 's':
                userCoordinates.append(userCoordinates[0])
                userCoordinates.append(userCoordinates[1])
                userCoordinates.append(userCoordinates[1]+distance)
        print(userCoordinates)

        temp=[]
        if axis == 'x':
            remainder = self._axis[0]%increments
            coord1 = userCoordinates[0]
            coord2 = userCoordinates[3]
        elif axis == 'y':
            remainder = self._axis[1]%increments
            coord1 = userCoordinates[1]
            coord2 = userCoordinates[4]
        elif axis == 'z':
            remainder = self._axis[2]%increments
            coord1 = userCoordinates[2]
            coord2 = userCoordinates[5]
        if remainder != 0:
            for coord in range(coord1, coord2, -increments):
                temp.append(coord)
            temp.append(temp[len(temp)-1]-remainder)
        else:
            if dir == 'n' or dir == 'w':
                for coord in range(coord1, coord2, increments):
                    temp.append(coord)
            elif dir == 's' or dir == 'e':
                for coord in range(coord1, coord2, -increments):
                    temp.append(coord)
        return temp


    def generateCoordinates(self, userCoordinates, longestAxis, dir, increments=100, distance = 100):
        if userCoordinates is None or type(userCoordinates) == 'str':
            return

        temp = []
        if dir == 'n':#-z
            temp = Calculate.generateNegativeCoords(self, userCoordinates, self._longestAxis, dir, increments, distance)
        elif dir == 's':#+z
            temp = Calculate.generatePositiveCoords(self, userCoordinates, self._longestAxis, dir, increments, distance)
        elif dir == 'e':#+x
            temp = Calculate.generatePositiveCoords(self, userCoordinates, self._longestAxis, dir, increments, distance)
        elif dir == 'w':#-x
            temp = Calculate.generateNegativeCoords(self, userCoordinates, self._longestAxis, dir, increments, distance)
        elif dir == 'u':#+y
            temp = Calculate.generatePositiveCoords(self, userCoordinates, self._longestAxis, dir, increments, distance)
        elif dir == 'd':#-y
            temp = Calculate.generateNegativeCoords(self, userCoordinates, self._longestAxis, dir, increments, distance)
        return temp