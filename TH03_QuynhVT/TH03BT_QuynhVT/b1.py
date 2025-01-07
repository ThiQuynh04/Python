# Bài 15_a: Viết hàm cho các bài đã thực hiện 
# 1) Viết hàm greeting(): Trả về câu chào với tham số truyền vào là chuỗi họ tên và năm sinh
# 2) Viết hàm rabbit_count(): tính số thỏ trong rừng khi truyền vào số tháng
# 3) Viết hàm count_mark(): trả về số sinh viên học lại và tổng số sinh viên trong lớp với tham số 
# truyền vào là một danh sách bảng điểm

def greeting(name: str, year: int) -> str:
    return f"Xin chào {name}, bạn sinh năm  {year}!"

def rabbit_count(months: int) -> str:
    # Số lượng thỏ ban đầu
    initial_rabbits = 2

    # Tính số lượng thỏ sau x tháng
    # Số lượng thỏ tăng gấp đôi mỗi tháng
    total_rabbits = initial_rabbits * (2 ** months)

    # Hiển thị thông báo kết quả
    print(f"Trong rừng có: {total_rabbits} con thỏ")

def count_mark(grades: list[float]) -> tuple[int, int]:
    total_students = len(grades)
    failing_students = sum(1 for grade in grades if grade < 5.0)
    return failing_students, total_students
# Ví dụ sử dụng
if __name__ == "__main__":
    while True:
        print("Chọn chức năng:")
        print("1. Greeting")
        print("2. Rabbit Count")
        print("3. Count Mark")
        print("0. Thoát")
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            name = input("Nhập họ tên: ")
            year_of_birth = int(input("Nhập năm sinh: "))
            print(greeting(name, year_of_birth))

        elif choice == "2":
            months = int(input("Nhập số tháng: "))
            print(rabbit_count(months))

        elif choice == "3":
            grades_input = input("Nhập danh sách điểm, cách nhau bởi dấu phẩy: ")
            grades_list = list(map(float, grades_input.split(",")))
            failing, total = count_mark(grades_list)
            print(f"Số sinh viên học lại: {failing}, Tổng số sinh viên: {total}")

        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
