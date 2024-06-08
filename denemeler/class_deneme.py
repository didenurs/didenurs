class Student:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def __str__(self):
        return f"{self.name}{self.surname}{self.id}"

    def MyFunc(self):
        print("Hello, my name is " + self.name + self.surname)
        print("My id is ", self.id)

s1 = Student("Didenur ", "Sezen ", 666)
s2 = Student("İrem ", "Bozdağ ", 747)

# print(s1.name, s1.surname, s1.id)
# print(s2.name, s2.surname, s2.id)

# print(s1)
# print(s2)

s1.MyFunc()
s2.MyFunc()
