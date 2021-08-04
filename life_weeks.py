#life weeks calculator taking life till 90 years
current_age=input("enter your current age: ")
#print(type(current_age))
current_age_int=int(current_age)

years_remaining=90-current_age_int
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
days_remaining=years_remaining*365

print( years_remaining)
print(weeks_remaining)
print(months_remaining)
print(days_remaining)

