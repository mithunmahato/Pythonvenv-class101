print(globals())


global_variable = 'global'

def print_global():
    global_variable = 'nested global'
    nested_variable = 'nested value'


print(globals())