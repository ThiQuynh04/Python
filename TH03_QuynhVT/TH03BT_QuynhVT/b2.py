# Bài 15_b: Viết hàm cho các bài đã thực hiện 
# 4) Viết hàm bmi_show(): Trả về nhận xét dựa vào chỉ số BMI đã tính với 2 tham số truyền vào là chiều 
# cao, cân nặng (Xem lại bài tập số 7) 
# 5) Viết hàm cal_point(): Trả về điểm trung bình hệ 10 và hệ 4 của một học sinh khi truyền vào danh sách 
# điểm (Xem lại bài tập số 10 ý 2) 
# 6) Viết hàm list_prime(): trả danh sách các số nguyên tố trong khoảng tử 1 đến n với tham số truyền 
# vào là n (Xem lại bài tập số 12) 

def bmi_show(height: float, weight: float) -> str:
    try:
        if(height < 0 and weight < 0):
             return f"Chiều cao hoặc cân nặng phải > 0"
        else:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                return f"Chỉ số bmi của bạn là: {bmi}. Bạn đang thiếu cân (Underweight)."
            elif 18.5 <= bmi <= 24.9:
                return f"Chỉ số bmi của bạn là: {bmi}. Bạn có cân nặng bình thường (Normal weight)."
            elif 25 <= bmi <= 29.9:
                return f"Chỉ số bmi của bạn là: {bmi}. Bạn thừa cân (Overweight)."
            else:
                return f"Chỉ số bmi của bạn là: {bmi}. Bạn béo phì (Obese)."
    except ValueError:
        return f"Vui lòng nhập đầu vào hợp lệ"
def cal_point(scores: list[float]) -> tuple[float, float]:
    if not scores:
        return 0.0, 0.0

    average_10 = sum(scores) / len(scores)
    average_4 = average_10 / 10 * 4
    return round(average_10, 2), round(average_4, 2)
def list_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhập số N: "))
if n >= 2:
    primes = [i for i in range(2, n + 1) if list_prime(i)]
    print(f"Dãy số nguyên tố từ 2 đến {n}: {primes}")
else:
    print("Vui lòng nhập số N lớn hơn hoặc bằng 2.")


if __name__ == "__main__":
    n = int(input("Nhập số lượng phần tử: "))
    scores = []
    print("Nhập các điểm hệ 10:")
    for i in range(n):
        while True:
            try:
                score = float(input(f"Nhập điểm thứ {i+1}: "))
                if 0 <= score <= 10:
                    scores.append(score)
                    break
                else:
                    print("Vui lòng nhập điểm trong khoảng 0 đến 10.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

    letter_grades = []
    for score in scores:
        if score >= 9:
            letter_grades.append("A+")
        elif score >= 8.5:
            letter_grades.append("A")
        elif score >= 8:
            letter_grades.append("B+")
        elif score >= 7:
            letter_grades.append("B")
        elif score >= 6.5:
            letter_grades.append("C+")
        elif score >= 5.5:
            letter_grades.append("C")
        elif score >= 5:
            letter_grades.append("D+")
        elif score >= 4:
            letter_grades.append("D")
        else:
            letter_grades.append("F")

    average_10, average_4 = cal_point(scores)

    print("Điểm hệ 10:", scores)
    print("Điểm chữ tương ứng:", letter_grades)
    print("Điểm trung bình hệ 10:", average_10)
    print("Điểm trung bình hệ 4:", average_4)
