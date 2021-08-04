num = int(input("enter the number: "))
print(num)

if num % 2 == 0:
    if num in range(2, 5):
        print("Not Weird")
    elif num in range(6, 20):
        print("Weird")
    elif num > 20:
        print("Not Weird")
else:
    print("weird")
n = int(input())
if n % 2:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")