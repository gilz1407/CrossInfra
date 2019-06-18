class BasicFunc:
    @classmethod
    def listLength(cls,lst):
        totalLength=0
        for item in lst:
            if (type(item)==list):
                totalLength+=len(item)
            else:
                totalLength+=1
        return totalLength

    @classmethod
    def findIndex(cls,index, lst):
        middle = int(len(lst) / 2)
        if type(lst[middle]) is list:
            middleVal = lst[middle][0]
        else:
            middleVal = lst[middle]

        if index < middleVal:
            return cls.findIndex(index, lst[:middle])
        elif index > middleVal:
            return middle + cls.findIndex(index, lst[middle:])
        return middle

    #Search for the relevant template according to the length (pos=2)

    @classmethod
    def searchTemplate(cls, lst, expLength):
        middle = cls.findTemplates(lst, expLength)

        index = middle
        while lst[index-1] == expLength:
            index = index-1

        return index


    @classmethod
    def findTemplates(cls, lst, expLength):
        middle = int(len(lst) / 2)
        middleVal = lst[middle][2]

        if int(expLength) < middleVal:
            return cls.findTemplates(lst[:middle], int(expLength))
        elif int(expLength) > middleVal:
            return middle + cls.findTemplates(lst[middle:], int(expLength))

        first=0
        last=0
        #return middle
        for i in range(middle, len(lst)-1):
            if lst[i][2] > lst[middle][2]:
                last = i
                break

        for i in range(middle,0,-1):
            if lst[i][2] < lst[middle][2]:
                first = i+1
                break

        return lst[first:last]
