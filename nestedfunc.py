def outer_function():
    def inner_function():
        print("This is a inner function")
    inner_function()

outer_function()

def outer_function():
    def inner_function():
        print("This is a inner function")
    return inner_function()

outer_function()