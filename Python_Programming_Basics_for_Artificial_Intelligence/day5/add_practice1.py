def count_vowels(teks):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in teks:
        if char in vowels:
            count += 1
    return count

teks = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(teks)}")
