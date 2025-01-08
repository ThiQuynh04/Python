#bai17: Đọc/Ghi file
# Đọc dữ liệu từ file dayso1_bai17.txt
with open('C:\\Users\\Admin\\Documents\\Zalo Received Files\\PythonGit\\dayso1.txt', 'r') as file:
    # Giả sử dữ liệu trong file là một dãy số cách nhau bởi dấu phẩy
    data = file.read().strip()
    numbers = list(map(int, data.split(' ')))

# Tìm phần tử lớn nhất và nhỏ nhất
max_value = max(numbers)
min_value = min(numbers)

# Tìm chỉ số của phần tử lớn nhất và nhỏ nhất xuất hiện đầu tiên
max_index = numbers.index(max_value)
min_index = numbers.index(min_value)

# Đổi chỗ phần tử lớn nhất và nhỏ nhất
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

# Lưu dãy mới vào file dayso2_bai17.txt
with open('C:\\Users\\Admin\\Documents\\Zalo Received Files\\PythonGit\\dayso1.txt', 'w') as file:
    file.write(' '.join(map(str, numbers)))

print("Đã đổi chỗ thành công và lưu vào file dayso2.txt")