import numpy as np

# Đọc dữ liệu từ file Data_BMI.txt
data = np.loadtxt('C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt')

# Tách dữ liệu chiều cao (Height) và cân nặng (Weight)
v_height = data[:, 0] / 100  # Chuyển đổi chiều cao từ cm sang m
v_weight = data[:, 1]       # Cân nặng (kg)

# Tính chỉ số BMI
v_bmi = np.round(v_weight / np.square(v_height), 1)  # Làm tròn tới 1 chữ số

# In kết quả
print("Vector BMI:", v_bmi)
