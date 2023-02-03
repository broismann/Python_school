class MyString(str):
    def __add__(self, other):
        return str(MyString(super().__add__(str(other))))

    def __sub__(self, other):
        if str(other) in self:
            return str(MyString(self.replace(str(other), '', 1)))
        return str(MyString(self))


str1 = MyString('New') + None
print(str1)
print(type(str1))
str2 = ('pineapple apple pine') - 'apple'
print(str2)
print(type(str2))
