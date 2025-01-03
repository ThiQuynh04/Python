# Bài 13: Đổi số từ thập phân sang nhị phân
n = int(input("Nhập số tự nhiên N (N > 0): "))
binary = bin(n)[2:]
print(f"Hệ nhị phân của {n}: {binary}")