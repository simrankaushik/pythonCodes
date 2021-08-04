""""#there are 4 modes in this - read,write,create, append
#read mode

f=open("file_handling.txt","r")
print(f.read())
#specifies the number of character u want to read
f=open("file_handling.txt","r")
print(f.read(25))
#to read lines
f=open("file_handling.txt","r")
print(f.readline())
print(f.readline())
# another way
f=open("file_handling.txt","r")
for x in f:
    print(x)

f.close()
"""
"""#append function

f=open("file_handling.txt","a")
f.write("\na new through append mode")
f.close()

f=open("file_handling.txt","r")
print(f.read())

f=open("new.txt","x")"""
# used to remove the newly created file
"""import os
os.remove("new.txt")"""
#another way
import os
if os.path.exists("new.txt"):
    os.remove("new.txt")
else:
    print("file doesnot exist")


