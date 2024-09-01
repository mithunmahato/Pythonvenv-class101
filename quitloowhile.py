while True:
    user_input = input("Enter a number or type quit to exit:")
    if user_input == "quit":
        break
    elif user_input.isdigit():
        print('Your entered:' , user_input)
    else:
        print("Invalid input, please try again")