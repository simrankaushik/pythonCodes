# map function is an inbuild function
#map(function,iterable)
#doesnt require boolean
# suppose find out the squares
def square(x):
    return x*x

numbers=[1,2,3,4,5]
list_of_squares = map(square,numbers)
print(list(list_of_squares))
