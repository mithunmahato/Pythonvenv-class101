# Addtion
def addition(a,b):
    value = a+b
    return value
# Greetings
def char(name):
    print(f"Hello,{name}")
# Default Greet    
def defaArgs(name='World'):
    print(f"Hello,{name}")

# Variable-Length Arguments
def print_arg(*args):
    for arg in args:
        print(arg)
        
# Variable-Length Keyword Args
def print_kwarg(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

# Recursive Function:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
    
x = addition(2,3) # Calling Addition
print(x)

char("Pravin") # Calling Greeting

defaArgs() # Calling defaArgs

print_arg(1,2,3,"a")

print_kwarg(name="Pravin",age=34,
            Nationality="Indian",
            Sex='Male')

print_kwarg(router_name="Cisco",ip="10.1.1.1",
            type="L3",
            PS='2')

value = factorial(5)
print(value)



