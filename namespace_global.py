import random

first_name = "Harsh"
last_name = "Kumar"

print(globals())

def print_variable():
    random_number = random.randint(0,9)
    print(first_name)
    print(last_name)
    print(random_number)

print_variable()
