#VD13
import numpy as np

# Tạo mảng 1 chiều (1D)
a = np.array([1, 2, 5, 7, 0, 8])

# In mảng
print(a)

# In thông tin về mảng44
print("Loại dữ liệu của biến a:", type(a))
print("Kiểu dữ liệu của phần tử trong mảng a:", a.dtype)
print("Kích thước của mảng a:", a.shape)
print("Số phần tử của mảng a:", a.size)
print("Số chiều của mảng a:", a.ndim)

#VD14 
import numpy as np

# Tạo mảng 2 chiều (2D - Ma trận)
b = np.array([(4, 5, 6.0), (1, 2, 3.5)])

# In mảng
print(b)

# In thông tin về mảng
print("Loại dữ liệu của biến b:", type(b))
print("Kiểu dữ liệu của phần tử trong mảng b:", b.dtype)
print("Kích thước của mảng b:", b.shape)
print("Số phần tử của mảng b:", b.size)
print("Số chiều của mảng b:", b.ndim)

#VD1515
import numpy as np

c = np.array([[(2,4,0,6), (4,7,5,6)],
              [(0,3,2,1), (9,4,5,6)],
              [(5,8,6,4), (1,4,6,8)]]) # mảng 3 chiều (3D)

print(c)
print("Phần tử đầu tiên của mảng c:", c[0,0,0])
print("Kiểu dữ liệu của phần tử trong mảng c:", c.dtype)
print("Kích thước của mảng c:", c.shape)
print("Số phần tử của mảng c:", c.size)
print("Số chiều của mảng c:", c.ndim)

#VD18
import numpy as np

array_zeros = np.zeros((5, 3))

print(array_zeros)
print("Kiểu dữ liệu trong mảng array_zeros:", array_zeros.dtype)
print("Kích thước của mảng array_zeros:", array_zeros.shape)
print("Số phần tử của mảng array_zeros:", array_zeros.size)
print("Số chiều của mảng array_zeros:", array_zeros.ndim)

import numpy as np

array_one = np.ones((5, 3), dtype=np.int)

print(array_one)
print("Kiểu dữ liệu trong mảng array_one:", array_one.dtype)
print("Kích thước của mảng array_one:", array_one.shape)
print("Số phần tử của mảng array_one:", array_one.size)
print("Số chiều của mảng array_one:", array_one.ndim)

#VD19
import numpy as np

array_eye = np.eye(5)

print(array_eye)
print("Kiểu dữ liệu của phần tử trong mảng array_eye:", array_eye.dtype)
print("Kích thước của mảng array_eye:", array_eye.shape)
print("Số phần tử của mảng array_eye:", array_eye.size)
print("Số chiều của mảng array_eye:", array_eye.ndim)

#VD20
import numpy as np

array_random = np.random.random((7,5))

print(array_random)
print("Kiểu dữ liệu của phần tử trong mảng array_random:", array_random.dtype)
print("Kích thước của mảng array_random:", array_random.shape)
print("Số phần tử của mảng array_random:", array_random.size)
print("Số chiều của mảng array_random:", array_random.ndim)

#VD21 
import numpy as np

# Nhập vào giá trị low và high cho phạm vi ngẫu nhiên
while True:
    try:
        low = int(input("Nhập giá trị thấp nhất (low): "))
        high = int(input("Nhập giá trị cao nhất (high): "))
        if low >= high:
            print("Giá trị low phải nhỏ hơn high. Vui lòng nhập lại.")
        else:
            break  # Nếu giá trị hợp lệ, thoát khỏi vòng lặp
    except ValueError:
        print("Giá trị nhập vào phải là số nguyên. Vui lòng nhập lại.")

# Nhập kích thước ma trận n và m
while True:
    try:
        n = int(input("Nhập số hàng (n): "))
        m = int(input("Nhập số cột (m): "))
        if n <= 0 or m <= 0:
            print("Số hàng và số cột phải lớn hơn 0. Vui lòng nhập lại.")
        else:
            break 
    except ValueError:
        print("Giá trị nhập vào phải là số nguyên. Vui lòng nhập lại.")

# Tạo ma trận ngẫu nhiên với các giá trị trong khoảng (low, high)
matrix = np.random.randint(low, high, size=(n, m))

# In ma trận ngẫu nhiên
print("Ma trận ngẫu nhiên:")
print(matrix)
#VD22
# Phương thức arange(a, b, steps):
# Tạo vector:
#   Phần tử đầu tiên = a,
#   kết thúc < b,
#   mỗi phần tử cách nhau một khoảng = steps

d = np.arange(1, 15, 2)
print("Vector d:", d)
print("Số phần tử của vector d:", d.size)

print()

# Phương thức linspace(a, b, num)
# Tạo vector:
#   Phần tử đầu tiên = a,
#   Phần tử kết thúc = b,
#   Số phần tử của ma trận = num

f = np.linspace(1, 15, 11)
print("Vector f:", f)
print("Số phần tử của vector f:", f.size)

#VD25
import numpy as np

# Đọc dữ liệu từ file Diem_2A.txt
path = 'Data_Exercise/Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=',', dtype=np.int)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
print("Kích thước của mảng diem_2a:", diem_2a.shape)
print("Số phần tử của mảng diem_2a:", diem_2a.size)
print("Số chiều của mảng diem_2a:", diem_2a.ndim)

#VDVD28
a_float = np.linspace(0,15,11)
print(a_float)
print('Kiểu Dữ liệu: ', a_float.dtype)

a_int = a_float.astype(np.int16)
print(a_int)
print('Dữ liệu sau khi chuyển: ', a_int.dtype)
#----------
# Chuyển từ kiểu float --> int
a_str = a_int.astype(np.str)
print(a_str)
print('Dữ liệu sau khi chuyển: ', a_str.dtype)

# Chuyển từ kiểu float --> boolean
a_bol = a_int.astype(np.bool)
print(a_bol)
print('Dữ liệu sau khi chuyển:', a_bool.dtype)
#
#---------------------------------------------------
#VD31
import numpy as np

# Tạo một mảng NumPy
a = np.array([3, 5, 10, 19, 8, 1, 9, 8, 3, 1])
# In ra các phần tử của mảng
print("Các phần tử của vector 'a':\n", a)
# Truy cập phần tử đầu tiên
print("Phần tử đầu tiên:", a[0])
# Truy cập phần tử thứ 3 (vị trí index là 2)
print("Phần tử thứ 3:", a[2])
# Truy cập phần tử cuối cùng
print("Phần tử cuối cùng:", a[-1])

#-------------

# Truy cập nhiều phần tử của vector 'a'
print("Các phần tử của vector 'a':\n", a)
# 3 phần tử đầu tiên
print("3 phần tử đầu tiên:", a[:3])
# Từ phần tử thứ 5 tới hết
print("Từ phần tử thứ 5 tới hết:", a[5:])
# Từ phần tử thứ 2 đến phần tử thứ 6 (không bao gồm phần tử thứ 6)
print("Từ phần tử thứ 2 đến phần tử thứ 6 của vector:", a[2:6])
#
#---------------------------------------------------
#VD32
# Truy cập tới 1 phần tử của ma trận (2D): a[index_row, index_col]
print('Điểm môn học đầu tiên, của học sinh đầu tiên:', diem_2a[0,0])
print('Điểm môn học thứ 1, của học sinh thứ 3:', diem_2a[2,1])
print('Điểm môn cuối cùng, của học sinh cuối cùng:', diem_2a[-1,-1])
print()

print('Bảng điểm lớp 2A:\n', diem_2a)
#
#---------------------------------------------------
#VD33
# Truy cập tới nhiều phần tử trong ma trận: a[index_row1:index_row2, index_col1:index_col2]
# Lấy điểm tất cả các môn (tất cả các hàng) của học sinh 5:
diem_hs5 = diem_2a[:, 5]
print("Điểm các môn của học sinh 5:", diem_hs5)
# Lấy điểm môn học cuối cùng của tất cả học sinh (tất cả các cột)
diem_mon = diem_2a[-1, :]
print("Điểm môn học cuối cùng của tất cả học sinh: \n", diem_mon)
# Lấy điểm 5 môn học đầu tiên của 10 học sinh đầu tiên
diem5_hs10 = diem_2a[:5, :10]
print("Bảng điểm 5 môn học đầu tiên của 10 học sinh đầu của lớp: \n", diem5_hs10)
#
#---------------------------------------------------

