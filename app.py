def multiply(*numbers):
    total = 1
    for number in numbers:
        if isinstance(number, (int, float)):

            total *= number
            print(number)
        else:
            print(f"skipping non-numeric value : {number}")
    return total


print(multiply(2, 3, 4, 5, "test", 7))
