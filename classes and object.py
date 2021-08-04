#classes and object
"""
class human:
    x=5

h1= human()
print(h1.x)

class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        def methods(self):
            print("hi my name is " + self.name)

h1 = human("simran", 19)

h1.methods()

#print(h1.name)
#print(h1.age)

# def methods(self):
 #       print("hi my name is " + self.name)


h1.methods"""

# if want to run an empty class
# class human:
# pass

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even number".format(num))
else:
   print("{0} is Odd number".format(num))
