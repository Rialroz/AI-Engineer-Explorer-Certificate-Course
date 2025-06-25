def read_items_file(filename):
    try:
        with open(filename, "r") as file:
            items = [item.strip() for item in file.readlines()]
            print("Items in the file:")
            for item in items:
                print(item.strip())
            return items
    except FileNotFoundError:
        print(f"File {filename} not found!")

def write_items_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

# Example usage
buah = read_items_file(r"Python_Programming_Basics_for_Artificial_Intelligence/Day6/fruits.txt")
print("Items read from file:", buah)
write_items_file(r"Python_Programming_Basics_for_Artificial_Intelligence/Day6/practice1.txt", buah)
read_items_file(r"Python_Programming_Basics_for_Artificial_Intelligence/Day6/practice1.txt")
# This code reads items from a file, writes them to another file, and then reads from that new file.