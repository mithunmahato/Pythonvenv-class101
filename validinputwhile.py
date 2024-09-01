valid_input = False

while not valid_input:
    user_input = input("Enter a number:")
    if user_input.isdigit():
        print("You entered:", user_input)
        valid_input = True
    else:
        print("Invalid input, please try again")