print("WELCOME TO THE LOVE CALCULATOR")
name1=input("enter your name:\n")
name2=input("enter their name:\n")
combined_name= name1 + name2
lowercase= combined_name.lower()
print(lowercase)

t=lowercase.count("t")
u=lowercase.count("u")
r=lowercase.count("r")
e=lowercase.count("e")
total = t+r+u+e
l=lowercase.count("l")
o=lowercase.count("o")
v=lowercase.count("v")
e=lowercase.count("e")
total2 = l+o+v+e

love_score=str(total)+str(total2)
#point to note here is that ki abhi they are in int and to print them together they need to be in string
print(love_score)




