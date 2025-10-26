succesful = False

for number in range(3):
    print("Attempt")
    if succesful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
