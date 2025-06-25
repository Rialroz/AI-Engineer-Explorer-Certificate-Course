def count_occurrences(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()
            occurrences = content.lower().count(word.lower())
            print(f"The word '{word}' occurs {occurrences} times in the file.")
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Example usage
practice2 = r"Python_Programming_Basics_for_Artificial_Intelligence/Day6/practice2.txt"
word = input("Enter the word to count: ")
count_occurrences(practice2, word)
