import numpy as np

# Đọc dữ liệu từ file
file_path = 'C:\\Users\\TV\\Documents\\BTTH_Python\\TH5.1_TrangTTH\\TH5.1BT\\Data_BMI.txt'
data = np.loadtxt(file_path)

# Tách chiều cao và cân nặng
heights_cm = data[:, 0]  # Cột 1: Chiều cao (cm)
weights_kg = data[:, 1]  # Cột 2: Cân nặng (kg)

# Chuyển đổi chiều cao từ cm sang mét
heights_m = heights_cm / 100.0

# Tính chỉ số BMI
bmi_values = weights_kg / (heights_m ** 2)

# Phân loại BMI
categories = []
for bmi in bmi_values:
    if bmi < 18.5:
        categories.append("Underweight")
    elif 18.5 <= bmi < 25:
        categories.append("Normal")
    elif 25 <= bmi < 30:
        categories.append("Overweight")
    elif 30 <= bmi < 35:
        categories.append("Obese")
    else:
        categories.append("Extremely Obese")

for i, (height, weight, bmi, category) in enumerate(zip(heights_cm, weights_kg, bmi_values, categories)):
    print(f"Person {i+1}: Height = {height} cm, Weight = {weight} kg, BMI = {bmi:.2f}, Category = {category}")
