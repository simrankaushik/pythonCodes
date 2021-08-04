#  filter function is used to filter our results
# using filteration for finding the prime numbers
# filter needs to be true or false
def prime(x):
    for n in range (2,x):
        if x%n == 0:
            return False
        else:
            return True

filtered = filter(prime,range(10))
print("prime numbers are",list(filtered))
