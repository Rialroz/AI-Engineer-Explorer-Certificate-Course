def checknumber_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def print_checknumber_odd_even(num):
    result = checknumber_odd_even(num)
    print(f"The number {num} is {result}")

num = int(input("Enter a number: "))
print_checknumber_odd_even(num)