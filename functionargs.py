def add_to_list(number,x):
    number.append(x)
    
mylist = [1,2,3,4]

def square(x):
    x = x**2
    return x

add_to_list(mylist,5)
re = 5
square(re)
print(re)

print(mylist)