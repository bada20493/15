class StringVar:

    stroka=''

    def set(self,newStroka):
        self.stroka=newStroka

    def get(self):
        return self.stroka

s=StringVar()
s.stroka='Cтрока1'
print(s.get())
s.set('Строка2')
print(s.get())
