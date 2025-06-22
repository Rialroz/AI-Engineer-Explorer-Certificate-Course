list1 = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 9, 600, 20, 30, 40, 50, 60, 70, 80, 90, 100]

max_value = list1[0]

for i in list1:
    if i > max_value:
        max_value = i

print("The maximum value in the list is:", max_value)
# This code finds the maximum value in a list of integers.