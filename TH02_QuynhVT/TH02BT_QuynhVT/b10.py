# Bài 10: Tính điểm học tập
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
average_10 = sum(scores) / len(scores)
average_4 = average_10 / 10 * 4

print("Điểm hệ 10:", scores)
print("Điểm chữ tương ứng:", letter_grades)
print("Điểm trung bình hệ 10:", round(average_10, 2))
print("Điểm trung bình hệ 4:", round(average_4, 2))