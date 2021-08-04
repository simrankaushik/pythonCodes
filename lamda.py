x = lambda a,b: a+b
print(x(5,30))
#to double the value

def f1(n):
    return lambda a:a*n

domb = f1(2)

print(domb(11))
