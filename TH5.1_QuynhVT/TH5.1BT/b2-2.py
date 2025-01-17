import numpy as np

data = np.loadtxt("C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt")  # Đọc file, dữ liệu dạng ma trận
v_height = data[:, 0] 

v_height_m = v_height / 100

v_height_m2 = v_height_m ** 2

print("Chiều cao (m):", v_height_m)
print("Chiều cao bình phương (m^2):", v_height_m2)
