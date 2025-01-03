# Bài 12: Hiển thị dãy số nguyên tố từ 2 đến N
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập số N: "))
if n >= 2:
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    print(f"Dãy số nguyên tố từ 2 đến {n}: {primes}")
else:
    print("Vui lòng nhập số N lớn hơn hoặc bằng 2.")
