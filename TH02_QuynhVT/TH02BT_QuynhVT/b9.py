# Bài 9: Hiển thị bảng cửu chương
n = int(input("Nhập bảng cửu chương muốn in (1-10): "))
if 1 <= n <= 10:
    print(f"Bảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
else:
    print("Vui lòng nhập số trong khoảng 1 đến 10.")
