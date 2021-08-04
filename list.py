# how to change tuple to list to add one or more items beacuse it is unchangeable

z=("car",'bike',True,0.5,30)#to print the list
print(z)

y=list(z)#to change tuple to list
print(type(y))#to check the type
print(len(y))#to count the items

y[1]="oranges"# for replacement
print(y)
              #####list#####
list=["car",'bike',20,0.88,True]
# range
print(list[2:4])
print(list[:4])
#change the value
list[2]="mine"
print(list)
list[1:3]="mine","my","me" #to change multiple values
print(list)

# to insert something
list.insert(3,"simran")
print(list)

list.append("oranges")
print(list)




