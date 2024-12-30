# Đoạn văn
text = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

# 1. Đếm số ký tự trong đoạn văn
num_characters = len(text)
print(f"Số ký tự trong đoạn văn: {num_characters}")

# 2. Kiểm tra từ không (không phân biệt chữ hoa, chữ thường)
search_terms = ["hồ chí minh", "non sông"]
for term in search_terms:
    if term.lower() in text.lower():
        print(f"Từ '{term}' có trong đoạn văn.")
    else:
        print(f"Từ '{term}' không có trong đoạn văn.")

# 3. Tách đoạn văn thành các câu bằng dấu '.'
sentences = text.split('.')
print("Các câu trong đoạn văn:")
for sentence in sentences:
    print(sentence.strip())

# 4. Kiểm tra có ký tự nào khác ký tự chữ và số hay không
has_special_characters = any(not c.isalnum() and not c.isspace() for c in text)
if has_special_characters:
    print("Đoạn văn có chứa ký tự khác ký tự chữ và số.")
else:
    print("Đoạn văn không có ký tự khác ký tự chữ và số.")

# 5. Thay thế các từ 'Việt Nam' bằng 'VIỆTNAM'
modified_text = text.replace("Việt Nam", "VIỆTNAM")
print("Đoạn văn sau khi thay thế:")
print(modified_text)