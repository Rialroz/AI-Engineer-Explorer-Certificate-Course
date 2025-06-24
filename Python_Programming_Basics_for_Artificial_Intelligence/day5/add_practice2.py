import re

def find_and_replace(text, pattern, replacement):
    re.findall(pattern, text)
    print(f"Pattern found: {re.findall(pattern, text)}")
    print(f"Replacement: {replacement}")
    return re.sub(pattern, replacement, text)

# Example usage
teks = "Saya suka makan nasi goreng dan minum teh manis. by JohnDoe@gmail.com"
pattern = r"([\w\.\+-]+@\w+\.\w+)"
replacement = "[EMAIL]"
result = find_and_replace(teks, pattern, replacement)
print("Original text:", teks)
print("Modified text:", result) 