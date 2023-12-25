print("hello world bitch ")


class Person: 
    def __init__(blub, name, age, flag):
        blub.name = name 
        blub.age = age  
        blub.flag = flag 

p1 = Person("JHON", 45, "France")

p2 = Person("Ellen", 55, "Austria")

def print_person(person): 
   print(person.name, person.age, person.flag)

print(print_person(p1))
print(print_person(p2))
