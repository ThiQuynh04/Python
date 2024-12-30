# Nhập số kẹo
n = int(input("Nhập vào số kẹo của cô: "))

# Nhập số học sinh
m = int(input("Nhập vào số học sinh trong lớp: "))

# Kiểm tra số học sinh có lớn hơn 0 không
if m > 0:
    # Tính số kẹo mỗi học sinh nhận được
    candies_per_student = n // m
    # Tính số kẹo còn lại
    remaining_candies = n % m

    # In kết quả
    print(f"Mỗi học sinh được nhận {candies_per_student} cái kẹo.")
    print(f"Cô còn lại {remaining_candies} cái kẹo.")
else:
    print("Số học sinh phải lớn hơn 0.")