# works on key and value like "name" is a key and "raj" is a value

dictt={"name":"raj",
       "age": 25,
        "area":"haryana",
       "city":"faridabad"}
print(dictt)
print(len(dictt))
print(type(dictt))

u=dictt["area"]
print(u)
#another way
x=dictt.get("area")
print(x)
#to change
dictt["area"]="india"
print(dictt)

dictt.update({"name":"anamika"})
print(dictt)

#to add a value
dictt["colour"]="black"
print(dictt)

#to remove
dictt.pop("area")
print(dictt)