#   date : 2/2/2019
#   author : H. Gray
#   email : heathergray153@gmail.com
#
#   title : Class Vs. Instance
#   brief : Write a class & instantiate it with the given methods
#
#   source : https://www.hackerrank.com/challenges/30-class-vs-instance/problem


class Person:
    def __init__(self, initialAge):
        if initialAge >= 0:
            self.age = initialAge
        else:
            self.age = 0
            print('Age is not valid, setting age to 0.')

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
