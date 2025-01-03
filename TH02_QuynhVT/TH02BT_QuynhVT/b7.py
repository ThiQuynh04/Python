# Nhập vào chiều cao (m) và cân nặng (kg)
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

# Tính chỉ số BMI
bmi = weight / (height ** 2)

# Hiển thị kết quả BMI
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")

# Đưa ra nhận xét về cơ thể
if bmi < 18.5:
    print("Bạn đang thiếu cân (Underweight).")
elif 18.5 <= bmi <= 24.9:
    print("Bạn có cân nặng bình thường (Normal weight).")
elif 25 <= bmi <= 29.9:
    print("Bạn thừa cân (Overweight).")
else:
    print("Bạn béo phì (Obese).")
