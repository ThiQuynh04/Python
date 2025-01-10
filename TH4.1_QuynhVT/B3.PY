import numpy as np

# Kích thước ma trận
n = 12

# Tạo ma trận vuông cấp n với các giá trị ngẫu nhiên trong khoảng từ 0 đến 100
matrix = np.random.randint(0, 101, size=(n, n))

# In ma trận
print("Ma trận vuông:")
print(matrix)

# Lấy các phần tử trên đường chéo chính
v_chinh = np.diagonal(matrix)

# Lấy các phần tử trên đường chéo phụ
v_phu = np.array([matrix[i, n-i-1] for i in range(n)])

# In các vector
print("\nVector v_chinh (đường chéo chính):")
print(v_chinh)
print("--------------------------------------")
print("Vector v_phu (đường chéo phụ):")
print(v_phu)
