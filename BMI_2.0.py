height = input("enter your height in cm: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height**2)
bmi_as_int = int(bmi)
print(bmi_as_int)

'''#g = round(bmi, 2)
print(bmi)'''
# telling the body type
'''if g < 18.5:
    print("you are underweight")
elif bmi < 25:
    print("you have a normal weight")
elif bmi < 30:
    print("you are overweight")
elif bmi < 35:
    print("you are an obese")
else:
    print("you are clinically obese")
'''