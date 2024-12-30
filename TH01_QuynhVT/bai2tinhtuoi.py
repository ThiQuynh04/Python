# Nhập họ tên
name = input("Nhập vào họ tên: ")

# Nhập năm sinh
birth_year = int(input("Nhập vào năm sinh: "))

# Lấy năm hiện tại
from datetime import datetime
current_year = datetime.now().year

# Tính tuổi
age = current_year - birth_year

# Hiển thị thông báo kết quả
print(f'Bạn “{name.upper()}” năm nay {age} tuổi.')