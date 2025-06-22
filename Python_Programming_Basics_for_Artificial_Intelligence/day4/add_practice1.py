list1 = list()
# Adding elements to the list
for i in range(1, 20, 2):
    list1.append(i)

#addition of elements
for i in range(1, 20, 3):
    list1.append(i)


def reverse_list(lst):
    """Reverses the given list."""
    return lst[::-1]

def remove_duplicates(lst):
    """Removes duplicates from the given list."""
    return  list(set(lst))

print("Original List:", list1)
print("Reversed List:", reverse_list(list1))
print("List without duplicates:", remove_duplicates(list1))

