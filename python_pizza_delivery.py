print("welcome to the python pizza delivery")
size=input("what size of pizza do u want ( S, M ,L): ")
add_pepp=input("do u want pepperoni ? Y or N: ")
extra_cheese=input("do u want some extra cheese( Y or N): ")

bill =0
if size == "S":
    bill += 15
elif size == "M":
    bill +=20
else:
    bill +=25

if add_pepp == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "Y" :
    bill += 1

print(f"your final bill is {bill}")
