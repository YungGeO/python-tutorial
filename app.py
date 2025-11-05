from collections import Counter


def separatesssss_letters(text):
    return list(text)


"""Check if input is biger than > 0 and is  string"""


def is_valid_string(s):

    return not s.isdigit() and len(s.strip()) > 0


while True:
    user_input = input("Enter a string (max 30 characters): ")

    if len(user_input) > 30:
        print("Invalid input! Please enter a string with 30 characters or fewer.\n")
        continue  # Ask again

    if not is_valid_string(user_input):
        print("Invalid input! Please enter a non-numeric, non-empty string.\n")
        continue  # Ask again
    letters = [c.lower() for c in user_input if c.isalpha()]
    letters = separatesssss_letters(user_input)
    print("Separated letters:", letters)
    counts = Counter(user_input)
    print("Letter counts:", counts)
    print("\nLetter Frequency:")
    for char, freq in counts.items():
        print(f"'{char}': {freq}")
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write("Separated letters:\n")
        f.write(", ".join(letters) + "\n\n")
        f.write("Letter Frequency:\n")
        for char, freq in counts.most_common():
            f.write(f"{char}: {freq}\n")
        f.write("\n" + "="*30 + "\n\n")  # seperate different inputs

    print("\n✅ Results saved to 'results.txt'.")
    break
