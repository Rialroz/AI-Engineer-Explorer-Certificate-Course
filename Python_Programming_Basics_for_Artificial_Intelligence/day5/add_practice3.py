teks = "saya suka makan nasi goreng dan minum teh manis"
def reverse_words(teks):
    """Fungsi untuk membalikkan urutan kata (bukan huruf) dalam sebuah kalimat."""
    kata_kata = teks.split()
    reverse_kata = kata_kata[::-1]
    return ' '.join(reverse_kata)

result = reverse_words(teks)

print("kaliman asli:", teks)
print("kalimat setelah dibalik:", result)