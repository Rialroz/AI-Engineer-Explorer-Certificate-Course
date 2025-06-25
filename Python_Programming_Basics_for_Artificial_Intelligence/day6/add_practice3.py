import datetime as dt

def append_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")
        print(f"Data '{data}' appended to {filename}.")

# Example usage
practice3 = "practice3.txt"
data = input("Enter the data to append: ") + dt.datetime.now().strftime(" %d-%m-%Y %H:%M:%S")

while True:
    append_to_file(practice3, data)
    cont = input("Do you want to append more data? (yes/no): ").strip().lower()
    if cont != 'yes':
        break
    data = input("Enter the data to append: ") + dt.datetime.now().strftime(" %d-%m-%Y %H:%M:%S")
