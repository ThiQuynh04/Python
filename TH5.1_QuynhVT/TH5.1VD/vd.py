# VD5 
# Phương thức a.reshape(m,n)
import numpy as np
vector_a= np.array([5,7,2,9,10,15,2,9,2,17,28,16], dtype=np.int16)
print(vector_a)

print('Số phần tử của vector:', vector_a.size)

# Chuyển đổi vector về matrix (n x m)
# Lưu ý: matrix.size = vector.size

matrix_a = vector_a.reshape((3,4))
print('Reshape về matrix: 3 x 4')
print(matrix_a)

print('Số phần tử của matrix_a:', matrix_a.size)

print('Reshape về matrix: 2 x 6')
matrix_b = vector_a.reshape((2,6))
print(matrix_b)

print('Số phần tử của matrix_b:', matrix_b.size)

# VD7 
# Chuyển đổi từ Matrix -> Vector

a1_2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print('Matrix: \n', a1_2d)

print('--------------------------------')
print('a) ravel by row (default order=\'C\')')
print(a1_2d.ravel())

print('\n b) ravel by column (order=\'F\')')
print(a1_2d.ravel(order='F'))

#VD9
# code1
import numpy as np

x = np.arange(0, 6)
print(x)

# Tách vector x thành 2 vector
# Có số phần tử bằng nhau
x1, x2 = np.split(x, 2)
print(x1, x2)
# code2 
import numpy as np

x = np.arange(1, 10)
print(x)

# Tách vector x thành 3 vector
# Tại các vị trí 2 và 6
x1, x2, x3 = np.split(x, [2, 6])
print(x1, x2, x3)

# VD11 
import numpy as np

# Tạo ma trận mẫu
A = np.array([[1, 2, 3, 4, 5],
              [9, 10, 11, 12, 13],
              [14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23],
              [24, 25, 26, 27, 28]])

# Lật ngược ma trận A theo cột
A1 = np.flip(A, 1)  # Hoặc A1 = np.fliplr(A)
print('Ma trận lật theo cột:\n', A1)

# Lật ngược ma trận A theo hàng
A2 = np.flip(A, 0)  # Hoặc A2 = np.flipud(A)
print('Ma trận lật theo hàng:\n', A2)

# VD16 
# code1 
import numpy as np

# Tạo một mảng từ 0 đến 7
x = np.arange(8)
print("x =", x)

# Sử dụng các hàm toán học của NumPy
print("x + 5 =", np.add(x, 5))  # Cộng từng phần tử của x với 5
print("x - 5 =", np.subtract(x, 5))  # Trừ từng phần tử của x đi 5
print("-x =", np.negative(x))  # Đổi dấu tất cả các phần tử của x
print("x * 2 =", np.multiply(x, 2))  # Nhân từng phần tử của x với 2
print("x / 2 =", np.divide(x, 2))  # Chia từng phần tử của x cho 2 (kết quả là số thực)
print("x // 2 =", np.floor_divide(x, 2))  # Chia lấy phần nguyên của phép chia
print("x % 2 =", np.mod(x, 2))  # Tìm phần dư khi chia cho 2
print("x ** 3 =", np.power(x, 3))  # Tính lũy thừa bậc 3 của từng phần tử

# VD17 
# code1 
import numpy as np

# Tạo một mảng gồm các số nguyên
x = np.array([-2, -1, 0, 1, 2])
print("x =", x)

# Tính giá trị tuyệt đối của các phần tử trong mảng x
print(np.abs(x))

# Sử dụng hàm absolute để tính giá trị tuyệt đối
print(np.absolute(x))
# code2 
import numpy as np

# Tạo một mảng các góc (đơn vị radian)
theta = np.linspace(0, np.pi, 3)
print("theta =", theta)

# Tính sin, cos, tan của các góc
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))

# VD19 
import numpy as np

# Tạo một mảng gồm các số nguyên
x = np.array([1, 2, 3])
print("x =", x)

# Tính hàm mũ tự nhiên (e^x) và lũy thừa cơ số 2
print("e^x =", np.exp(x))
print("2^x =", np.power(2, x))

# Tạo một mảng gồm các số nguyên dương
x = np.array([1, 2, 4, 100])
print("x =", x)

# Tính logarit tự nhiên, cơ số 2 và cơ số 10
print("ln(x) =", np.log(x))
print("log2(x) =", np.log2(x))
print("log10(x) =", np.log10(x))

# VD20 
import numpy as np

# Tạo một mảng gồm các số thực
arr = np.array([20.8999, 67.89899, 54.43409])
print(arr)

# 1) Làm tròn tới 1 số sau dấu phẩy
print(np.around(arr, 1))

# 2) Làm tròn tới 2 số sau dấu phẩy
print(np.around(arr, 2))

# 3) Làm tròn xuống số nguyên gần nhất
print(np.floor(arr))

# 4) Làm tròn lên số nguyên gần nhất
print(np.ceil(arr))

#VD23 
import numpy as np

# Tạo một vector ngẫu nhiên gồm các số nguyên từ 1 đến 15
a = np.random.randint(1, 15, 15)
print("Vector ban đầu:\n", a)

# Sắp xếp vector a tăng dần
a_sort = np.sort(a)

# Sắp xếp vector a giảm dần:
# Cách 1: Lật vector a_sort để sắp xếp giảm dần
b_sort = np.flip(a_sort)
# Cách 2: Sử dụng -np.sort(-x)
b_sort = -np.sort(-a)

print("Vector sắp xếp tăng dần:\n", a_sort)
print("Vector sắp xếp giảm dần:\n", b_sort)

# VD25 
# Tạo một ma trận mẫu
A = np.array([[8, 27, 2, 8, 3, 26],
              [7, 16, 19, 23, 21, 29],
              [14, 1, 3, 20, 5, 2],
              [29, 11, 12, 17, 29, 19],
              [4, 10, 14, 23, 4, 4]])

# a) Sắp xếp theo hàng (axis=0)
a_sort1 = np.sort(A, axis=0)
print("Ma trận 1:\n", a_sort1)

# b) Sắp xếp theo cột (axis=1)
a_sort2 = np.sort(A, axis=1)
print("Ma trận 2:\n", a_sort2)

# c) Chuyển thành vector và sắp xếp các phần tử tăng dần theo hàng
v_sort = np.sort(A, axis=None).reshape(A.shape[0], A.shape[1])
print("Vector:\n", v_sort)
# VD28 
import numpy as np

# Tạo một vector
x = np.array([17, 2, 11, 1, 9, 15, 1, 3, 8, 1, 12, 13, 5])

# 1) Tìm kiếm các phần tử có giá trị == 1
t1 = np.where(x == 1)
print(t1)
print("1. Số phần tử thỏa mãn điều kiện = 1: ", t1[0].size)

# 2) Tìm kiếm các phần tử có giá trị > 10
t2 = np.where(x > 10)
print(t2)
print("2. Số phần tử thỏa mãn điều kiện > 10: ", t2[0].size)

# 3) Tìm kiếm các phần tử có giá trị trong khoảng [5, 12)
t3 = np.where((x >= 5) & (x < 12))
print(t3)
print("3. Số phần tử thỏa mãn điều kiện [5, 10): ", t3[0].size)

# VD29
import numpy as np

# Tạo một ma trận
arr = np.array([[1, 2, 3, 4, 5, 4, 4],
                [7, 3, 4, 8, 9, 6, 7]])

# Tìm kiếm các phần tử lớn hơn 4
x = np.where(arr > 4)

# In ra ma trận và các chỉ số của phần tử thỏa mãn điều kiện
print("Ma trận A:\n", arr)
print(x)
print("Số phần tử thỏa mãn điều kiện > 4:", x[0].size)