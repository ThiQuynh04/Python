# Nhập vào số tháng
x = int(input("Nhập vào số tháng x: "))

# Số lượng thỏ ban đầu
initial_rabbits = 2

# Tính số lượng thỏ sau x tháng
# Số lượng thỏ tăng gấp đôi mỗi tháng
total_rabbits = initial_rabbits * (2 ** x)

# Hiển thị thông báo kết quả
print(f"Trong rừng có: {total_rabbits} con thỏ")