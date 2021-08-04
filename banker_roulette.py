#who gonna pay using randomisation

import random
names_string=input("enter the names separated by a comma: ");
names=names_string.split(",");
num_items=(len(names))
random_choice=random.randint(0,num_items-1)
print(random_choice)
person_who_will_pay= names[random_choice]
print(person_who_will_pay + " will going to pay today")