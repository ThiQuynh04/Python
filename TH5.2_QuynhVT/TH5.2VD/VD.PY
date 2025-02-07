#trang 39
import numpy as np

# Tạo hai ma trận
a = np.array([[1, 3, 1, 4],
              [3, 9, 5, 15],
              [0, 2, 1, 1],
              [0, 4, 2, 3]])

b = np.array([[1, 2, 3, 4],
              [-2, -1, 4, 1],
              [3, -4, -5, 6],
              [1, 2, 3, 4]])

# In các ma trận
print('Ma trận a:\n', a)
print('Ma trận b:\n', b)

# Tính định thức của các ma trận
det_a = np.linalg.det(a)
det_b = np.linalg.det(b)

# In kết quả
print('det(a) = ', det_a)
print('det(b) = ', det_b)

#trang 42
# Lấy các phần tử từ nằm trên đường chéo chính
# của ma trận A 1 phần tử từ trên xuống
d_A1 = A.diagonal(1)
print(d_A1)

# Lấy các phần tử trên đường chéo chính của
# ma trận vuông A
d_A = A.diagonal()
print(d_A)

# Lấy các phần tử nằm dưới đường chéo chính
# của ma trận A 4 phần tử từ trên xuống
d_A1 = A.diagonal(-4)
print(d_A1)

#trang 44
import numpy as np

# Tạo ma trận là các phần tử trên đường chéo chính
# của ma trận vuông A cách đường chéo chính
# về phía trên 2 đường
d_A1 = np.triu(A, 2)
print(d_A1)

# Tạo ma trận là các phần tử trên đường chéo chính
# của ma trận vuông A cách đường chéo chính
# về phía dưới 3 đường
d_A1 = np.triu(A, -3)
print(d_A1)

#trang45

# Tính trace của ma trận vuông A
trace_A = A.trace()
print("Trace of Matrix A: ", trace_A)


# Cách 2: Tính trace của ma trận vuông A
trace_A = A.diagonal().sum()
print("Trace of Matrix A: ", trace_A)

#bai 53
# 1) So sánh 2 ma trận
equal_ab = np.equal(a, b)
# hoặc equal_ab = a == b
print(equal_ab)

#54
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8, 9],
              [10, 11, 12]])

# Phép cộng
C = np.add(A, B)
print(C)

# Phép trừ
D = np.subtract(A, B)
print(D)

#Bai 55
# 3) Tích của 2 ma trận:
multi_ab = np.dot(A, B)
# hoặc multi_ac1 = a @ c
print(multi_ab)

#Bai 61
# Tìm ma trận chuyển vị của A
A_T = A.T
print("Ma trận A:\n", A)
print("Ma trận chuyển vị của A:\n", A_T)

# Tìm ma trận chuyển vị của B
B_T = B.T
print("Ma trận B:\n", B)
print("Ma trận chuyển vị của B:\n", B_T)
