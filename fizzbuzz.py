# in case of number which is divisible by 3 it will print fizz
# in 5 it will print buzz
#i both it will print fizzbuzz

for numbers in range (1,101,):
    if numbers%3==0 and numbers%5==0:
        print("fizzbuzz")

    elif numbers % 3 == 0:
        print("fizz")
    elif numbers % 5 == 0:
        print("buzz")
    else:
        print(numbers)

