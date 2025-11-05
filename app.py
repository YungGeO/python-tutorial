from collections import Counter
from datetime import datetime

# --- Class Definition ---


class LetterAnalyzer:
    def __init__(self, max_length=30):
        self.max_length = max_length
        self.letters = []
        self.counts = Counter()
        self.input_text = ""

    def is_valid_string(self, text):

        return not text.isdigit() and len(text.strip()) > 0

    def get_input(self, text):
        if len(text) > self.max_length:
            raise ValueError(
                f"Input must be {self.max_length} characters or fewer.")
        if not self.is_valid_string(text):
            raise ValueError("Input cannot be numeric only or empty.")
        self.input_text = text

    def process_letters(self):
        """Separate letters, convert to lowercase, count frequency"""
        self.letters = [c.lower() for c in self.input_text if c.isalpha()]
        self.counts = Counter(self.letters)

    def display_results(self):

        result = f"Separated letters: {self.letters}\n\nLetter Frequency:\n"
        for char, freq in self.counts.most_common():
            result += f"{char}: {freq}\n"
        return result

    def save_to_file(self, filename="results.txt"):
        """Append results to a file with timestamp"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write("Input: " + self.input_text + "\n")
            f.write("Separated letters:\n" + ", ".join(self.letters) + "\n\n")
            f.write("Letter Frequency:\n")
            for char, freq in self.counts.most_common():
                f.write(f"{char}: {freq}\n")
            f.write("\n" + "="*30 + "\n\n")


# --- Main Program ---
analyzer = LetterAnalyzer()

while True:
    user_input = input("Enter a string (max 30 characters): ")
    try:
        analyzer.get_input(user_input)      # Validate the users  input
        analyzer.process_letters()          # Process each letters
        print(analyzer.display_results())   # Show results
        analyzer.save_to_file()             # Saves to file
        print("✅ Results saved to 'results.txt'.")

        # Ask if the user wants to analyze another string
        again = input("Analyze another string? (y/yes to continue): ").lower()
        if again not in ['y', 'ye', 'yes']:
            print("Exiting program. Goodbye!")
            break

    except ValueError as e:
        print(f"❌ {e}")
