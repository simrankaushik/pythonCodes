#functions for inputs
"""name = input("what ia your name: ")

def greet_fun (fun_name):
    print(f"hello {fun_name}")
    print(f"hows u doing {fun_name}")

greet_fun(name)"""
import math
def paint_calc(height, width , cover):
    num_of_cans = math.ceil((height*width)/cover)

    print(f"you will need {num_of_cans} cans")

test_h=int(input("enter the height: "))
test_w=int(input("ebter the width: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)


