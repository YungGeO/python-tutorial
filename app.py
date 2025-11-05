
def separatesssss_letters(text):
    return list(text)


while True:
    user_input = input("Enter a string (max 30 characters): ")

    if len(user_input) > 30:
        print("Invalid input! Please enter a string with 30 characters or fewer.\n")
    else:
        letters = separatesssss_letters(user_input)
        print("Separated letters:", letters)
        break
