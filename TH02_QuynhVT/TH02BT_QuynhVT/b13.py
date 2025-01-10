# Bài 13: Đổi số từ thập phân sang nhị phân
try:
    n = int(input("Nhập số tự nhiên N (N > 0): "))
    if n > 0:
        binary = bin(n)[2:]
        print(f"Hệ nhị phân của {n}: {binary}")
    else:
        print("Vui lòng nhập số lớn hơn 0.")
except ValueError:
         print("Vui lòng nhập một số hợp lệ;.")
 