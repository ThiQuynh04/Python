# Khởi tạo danh sách điểm thi
grades = ['A', 'B', 'C', 'F', 'A', 'D', 'B', 'F', 'C', 'A']

# 1) Số sinh viên trong lớp
num_students = len(grades)
print(f"Số sinh viên trong lớp: {num_students}")

# 2) Số sinh viên phải học lại môn này (điểm F)
num_students_fail = grades.count('F')
print(f"Số sinh viên phải học lại môn này: {num_students_fail}")

# 3) Số sinh viên có điểm từ B trở lên
num_students_pass = sum(1 for grade in grades if grade in ['A', 'B'])
print(f"Số sinh viên có điểm từ B trở lên: {num_students_pass}")

# 4) Tạo bảng điểm mới và loại bỏ điểm của sinh viên đầu tiên và cuối cùng
if num_students > 0:
    # Lấy điểm của sinh viên đầu tiên và cuối cùng
    first_student_grade = grades[0]
    last_student_grade = grades[-1]

    # Tạo bảng điểm mới bằng cách loại bỏ điểm của sinh viên đầu tiên và cuối cùng
    new_grades = [grade for grade in grades if grade != first_student_grade and grade != last_student_grade]

    print("Bảng điểm mới sau khi loại bỏ điểm của sinh viên đầu tiên và cuối cùng:")
    print(new_grades)
else:
    print("Danh sách điểm rỗng.")