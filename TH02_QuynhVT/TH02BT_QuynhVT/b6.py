# Nhập vào một ký tự chữ cái
char = input("Nhập vào một chữ cái: ").lower()

# Danh sách các nguyên âm trong tiếng Anh (không phân biệt hoa-thường)
vowel_letters = ['a', 'e', 'i', 'o', 'u']

# Kiểm tra xem ký tự nhập vào có phải là nguyên âm không
if char in vowel_letters:
    print("Đây là nguyên âm!")
else:
    print("Đây là phụ âm!")

