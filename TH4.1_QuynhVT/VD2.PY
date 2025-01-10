#VD25
import numpy as np

# Đọc dữ liệu từ file Diem_2A.txt
path = 'C:\\Users\\Admin\\Documents\\Zalo Received Files\\PythonGit\\Diem_2A.txt'
diem_2a = np.loadtxt(path, delimiter=' ', dtype=np.int_)

print(diem_2a)
print("Kiểu dữ liệu của phần tử trong mảng diem_2a:", diem_2a.dtype)
print("Kích thước của mảng diem_2a:", diem_2a.shape)
print("Số phần tử của mảng diem_2a:", diem_2a.size)
print("Số chiều của mảng diem_2a:", diem_2a.ndim)