class Point:
    x=''
    y=''

    def Print(self):
        print('ТОЧКА')

    def setPoint(self,newX,newY):
        self.x=newX
        self.y=newY

    def getPoint(self):
        return self.x,self.y

    def __init__(self,newX,newY):
        self.x=newX
        self.y=newY
        print('Точка ('+self.x+','+self.y+')')

point=Point('3','5')
print(point.getPoint())
point.Print()
point.setPoint(4,6)
print(point.getPoint())
