# use to make code small-list comprehension

fruits=["banana","apple","orange","mango","kiwi"]
print(fruits)
newfruits=[]
# now printing the names of the fruits which contain "a" in them
for x in fruits:
    if "a" in x:
        newfruits.append(x)

    else:
        print("none")

print(newfruits)
                    ## using list comprehension
newfruits=[x for x in fruits if "i" in x]
print(newfruits)
print(type(newfruits))

newfruit=[x for x in fruits if x!="banana"]
print(newfruit)

newfruit=[x for x in range(10)]
print(newfruit)

newfruit=[x for x in range(10) if x<=6]
print(newfruit)

simran = [x.upper() for x in fruits]
print(simran)

# to replace one fruit
simran = [x if x!="banana" else "watermelon" for x in fruits]
print(simran)











