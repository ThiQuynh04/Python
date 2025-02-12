import mysql.connector

def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

def show_databases():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    print("\nDanh sách CSDL:")
    for db in cursor.fetchall():
        print(f"- {db[0]}")
    conn.close()

def show_tables():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    print("\nDanh sách bảng trong student_db:")
    for table in cursor.fetchall():
        print(f"- {table[0]}")
    conn.close()

def show_table_structure(table_name):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute(f"DESC {table_name}")
    print(f"\nCấu trúc bảng {table_name}:")
    for col in cursor.fetchall():
        print(col)
    conn.close()

def show_table_data(table_name):
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"\nDữ liệu trong bảng {table_name}:")
    for row in rows:
        print(row)
    conn.close()

# Gọi các hàm
show_databases()       # Hiển thị danh sách CSDL
show_tables()          # Hiển thị danh sách bảng trong CSDL student_db
show_table_structure("students")  # Hiển thị cấu trúc bảng students
show_table_data("students")       # Hiển thị dữ liệu trong bảng students



# -- Tạo cơ sở dữ liệu student_db
# CREATE DATABASE IF NOT EXISTS student_db;

# -- Sử dụng cơ sở dữ liệu vừa tạo
# USE student_db;

# -- Tạo bảng students
# CREATE TABLE IF NOT EXISTS students (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INT CHECK (age > 0),
#     gender ENUM('Nam', 'Nữ') NOT NULL,
#     grade FLOAT CHECK (grade >= 0 AND grade <= 10)
# );

# -- Chèn dữ liệu vào bảng
# INSERT INTO students (name, age, gender, grade) VALUES
# ('Nguyễn Văn A', 20, 'Nam', 8.5),
# ('Trần Thị B', 22, 'Nữ', 9.2),
# ('Lê Văn C', 21, 'Nam', 7.8),
# ('Phạm Thị D', 19, 'Nữ', 6.4),
# ('Đặng Văn E', 23, 'Nam', 5.9),
# ('Hoàng Minh F', 20, 'Nam', 9.0),
# ('Vũ Thị G', 21, 'Nữ', 7.0),
# ('Lê Thị H', 22, 'Nữ', 8.8),
# ('Ngô Văn I', 20, 'Nam', 4.5),
# ('Bùi Văn J', 24, 'Nam', 6.2);

# -- 1. Hiển thị tất cả dữ liệu trong bảng students
# SELECT * FROM students;

# -- 2. Lọc sinh viên có điểm trung bình lớn hơn 8.0
# SELECT * FROM students WHERE grade > 8.0;

# -- 3. Đếm số lượng sinh viên theo giới tính
# SELECT gender, COUNT(*) AS total FROM students GROUP BY gender;

# -- 4. Sắp xếp danh sách sinh viên theo điểm số giảm dần
# SELECT * FROM students ORDER BY grade DESC;

# -- 5. Cập nhật điểm của sinh viên có ID = 1
# UPDATE students SET grade = 9.0 WHERE id = 1;

# -- 6. Xóa sinh viên có điểm dưới 5.0
# DELETE FROM students WHERE grade < 5.0;

# -- 7. Tìm sinh viên có tên chứa 'Nguyễn'
# SELECT * FROM students WHERE name LIKE '%Nguyễn%';

# -- 8. Tính điểm trung bình của tất cả sinh viên
# SELECT AVG(grade) AS avg_grade FROM students;

# -- 9. Lấy 3 sinh viên có điểm cao nhất
# SELECT * FROM students ORDER BY grade DESC LIMIT 3;

# -- 10. Kiểm tra số lượng sinh viên theo độ tuổi
# SELECT age, COUNT(*) AS total FROM students GROUP BY age;

# -- 11. Lấy danh sách sinh viên có độ tuổi từ 20 đến 25
# SELECT * FROM students WHERE age BETWEEN 20 AND 25;

# -- 12. Lấy danh sách sinh viên theo giới tính và sắp xếp theo tên
# SELECT * FROM students WHERE gender = 'Nữ' ORDER BY name;

# -- 13. Lấy danh sách sinh viên có điểm cao nhất theo giới tính
# SELECT * FROM students WHERE grade = (SELECT MAX(grade) FROM students);

# -- 14. Hiển thị số lượng sinh viên có điểm trên mức trung bình
# SELECT COUNT(*) FROM students WHERE grade > (SELECT AVG(grade) FROM students);

# -- 15. Hiển thị danh sách tất cả các bảng trong cơ sở dữ liệu student_db
# SHOW TABLES;


