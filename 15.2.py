class Animal:
    name=''
    def Eat(self):
        print("Ням-Ням");

    def setName(self, newName):
        self.name=newName

    def getName(self):
        return self.name

    def makeNoize(self):
        print(self.name+ 'Говорит Грр')

    def __init__(self, newName):
        self.name=newName
        print('Родилось животное ', self.name)

Cat=Animal('Васька')
print(Cat.getName())

Cat.setName('Василек')
print(Cat.getName())

Cat.Eat()
Cat.makeNoize()
