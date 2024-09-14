global_variable = 'global'

def add (num1,num2):
    nested_value = "Inside function"
    print(num1+num2)

print(locals())

add(13,20)

