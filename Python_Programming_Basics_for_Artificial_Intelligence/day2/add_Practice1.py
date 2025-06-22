num = int(input("Enter a number: "))

while True:
    if num < 0:
        print("Negative number entered. Exiting the program.")
        break
    elif num == 0 or num == 1:
        print("The factorial of", num, "is 1.")
        break
    else:
        factorial = 1
        for i in range(2, int(num) + 1):
            factorial *= i
        print("The factorial of", num, "is", factorial)
        break