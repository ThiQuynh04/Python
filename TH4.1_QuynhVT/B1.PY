import numpy as np

# Kích thước ma trận
n = 12

# Tạo ma trận vuông cấp n với các giá trị ngẫu nhiên trong khoảng từ 0 đến 100
matrix = np.random.randint(0, 101, size=(n, n))

print("Ma trận vuông:")
print(matrix)

while True:
    try:
        # Nhập vào số nguyên x trong khoảng từ 0 đến 100
        x = int(input("Nhập số nguyên x (0 <= x <= 100): "))
        
        # Đảm bảo x nằm trong khoảng (0-100)
        if 0 <= x <= 100:
            break  # Nếu x hợp lệ, thoát khỏi vòng lặp
        else:
            print("Số x phải nằm trong khoảng từ 0 đến 100. Vui lòng nhập lại.")
    except ValueError:
        print("Giá trị nhập vào không phải là số nguyên. Vui lòng nhập lại.")

# Đếm số phần tử trong ma trận
count_equals = np.sum(matrix == x)  # Số phần tử bằng x
count_greater = np.sum(matrix > x)  # Số phần tử lớn hơn x
count_less = np.sum(matrix < x)     # Số phần tử nhỏ hơn x

print(f"Số phần tử bằng {x}: {count_equals}")
print(f"Số phần tử lớn hơn {x}: {count_greater}")
print(f"Số phần tử nhỏ hơn {x}: {count_less}")
