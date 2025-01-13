import numpy as np

def create_random_matrix(n):
    # Tạo ma trận ngẫu nhiên với số nguyên trong khoảng 0-100
    matrix = np.random.randint(0, 101, size=(n, n))
    
    # In thông tin về ma trận
    print("Kiểu dữ liệu của phần tử trong ma trận:", matrix.dtype)
    print("Kích thước của mảng ma trận:", matrix.shape)
    print("Số phần tử của mảng ma trận:", matrix.size)
    print("Số chiều của mảng ma trận:", matrix.ndim)
    
    # In ma trận
    print("\nMa trận:")
    print(matrix)
    
    return matrix

def get_diagonals(matrix):
    # Lấy đường chéo chính
    v_chinh = np.diag(matrix)
    
    # Lấy đường chéo phụ
    v_phu = np.diag(np.fliplr(matrix))
    
    print("\nVector chéo chính (v_chinh):")
    print(v_chinh)
    print("\nVector chéo phụ (v_phu):")
    print(v_phu)
    
    return v_chinh, v_phu

def count_comparison(matrix, x):
    # Đếm số phần tử bằng x
    equal_count = np.sum(matrix == x)
    
    # Đếm số phần tử lớn hơn x
    greater_count = np.sum(matrix > x)
    
    # Đếm số phần tử nhỏ hơn x
    less_count = np.sum(matrix < x)
    
    print(f"\nKết quả so sánh với x = {x}:")
    print(f"Số phần tử bằng {x}: {equal_count}")
    print(f"Số phần tử lớn hơn {x}: {greater_count}")
    print(f"Số phần tử nhỏ hơn {x}: {less_count}")
    
    return equal_count, greater_count, less_count

# Tạo ma trận với n = 12
n = 12
result_matrix = create_random_matrix(n)

# Lấy các vector chéo
v_chinh, v_phu = get_diagonals(result_matrix)

# Nhập và kiểm tra giá trị x    
while True:
    try:
        x = int(input("\nNhập giá trị x (0-100): "))
        if 0 <= x <= 100:
            break
        else:
            print("Giá trị x phải nằm trong khoảng 0-100")
    except ValueError:
        print("Vui lòng nhập một số nguyên")

# Đếm và so sánh với x
equal_count, greater_count, less_count = count_comparison(result_matrix, x)

#Bai 2.1
# Dữ liệu điểm của lớp 2A
students_scores = [
    {'name': 'Được', 'math': 10, 'literature': 10, 'english':10},
    {'name': 'Yến', 'math': 1, 'literature': 1, 'english': 1},
    {'name': 'Nguyên', 'math': 9, 'literature': 8, 'english': 7},
    {'name': 'Bằng', 'math': 6, 'literature': 5, 'english': 6},
    {'name': 'Hiếu', 'math': 7, 'literature': 7, 'english': 8}
]

# Tính điểm trung bình của từng học sinh
for student in students_scores:
    scores = [score for subject, score in student.items() if subject != 'name']
    student['average'] = sum(scores) / len(scores)

# In bảng điểm và điểm trung bình của từng học sinh
print(f"{'Tên Học Sinh':<15}{'Toán':<8}{'Văn':<8}{'Anh':<8}{'Điểm Trung Bình'}")
print("-" * 50)
for student in students_scores:
    print(f"{student['name']:<15}{student['math']:<8}{student['literature']:<8}{student['english']:<8}{student['average']:.2f}")


# Tìm học sinh có điểm trung bình cao nhất và thấp nhất
highest_avg_student = max(students_scores, key=lambda x: x['average'])
lowest_avg_student = min(students_scores, key=lambda x: x['average'])

# In kết quả
print("\nKết quả:")
print(f"Học sinh có điểm trung bình cao nhất: {highest_avg_student['name']} với điểm trung bình {highest_avg_student['average']:.2f}")
print(f"Học sinh có điểm trung bình thấp nhất: {lowest_avg_student['name']} với điểm trung bình {lowest_avg_student['average']:.2f}")


#Bai 2.2
# Dữ liệu điểm của lớp 2A
students_scores = [
    {'name': 'Được', 'math': 10, 'literature': 10, 'english':10},
    {'name': 'Yến', 'math': 1, 'literature': 1, 'english': 1},
    {'name': 'Nguyên', 'math': 9, 'literature': 8, 'english': 7},
    {'name': 'Bằng', 'math': 6, 'literature': 5, 'english': 6},
    {'name': 'Hiếu', 'math': 7, 'literature': 7, 'english': 8}
]

# Khởi tạo danh sách để lưu điểm của từng môn học
subjects = ['math', 'literature', 'english']
subject_scores = {subject: [] for subject in subjects}

# Lấy điểm của từng môn học từ dữ liệu học sinh
for student in students_scores:
    for subject in subjects:
        subject_scores[subject].append(student[subject])

# Tính điểm trung bình của từng môn học
subject_avg = {subject: sum(scores) / len(scores) for subject, scores in subject_scores.items()}

# In điểm trung bình của từng môn học
print(f"{'Môn học':<12}{'Điểm Trung Bình'}")
print("-" * 30)
for subject, avg in subject_avg.items():
    print(f"{subject.capitalize():<12}{avg:.2f}")

# Tìm môn học có điểm trung bình cao nhất và thấp nhất
highest_avg_subject = max(subject_avg, key=subject_avg.get)
lowest_avg_subject = min(subject_avg, key=subject_avg.get)

# In kết quả
print("\nKết quả:")
print(f"Môn học có điểm trung bình cao nhất: {highest_avg_subject.capitalize()} với điểm trung bình {subject_avg[highest_avg_subject]:.2f}")
print(f"Môn học có điểm trung bình thấp nhất: {lowest_avg_subject.capitalize()} với điểm trung bình {subject_avg[lowest_avg_subject]:.2f}")

#Bai 2.3
students_scores = [
    {'name': 'Được', 'math': 10, 'literature': 10, 'english':10},
    {'name': 'Yến', 'math': 1, 'literature': 1, 'english': 1},
    {'name': 'Nguyên', 'math': 9, 'literature': 8, 'english': 7},
    {'name': 'Bằng', 'math': 6, 'literature': 5, 'english': 6},
    {'name': 'Hiếu', 'math': 7, 'literature': 7, 'english': 8}
]

# Hàm tính độ lệch chuẩn (standard deviation)
def standard_deviation(scores):
    mean = sum(scores) / len(scores)
    variance = sum((score - mean) ** 2 for score in scores) / len(scores)
    return math.sqrt(variance)

# Tính độ lệch chuẩn của điểm các môn của từng học sinh
student_devs = []
for student in students_scores:
    scores = [score for subject, score in student.items() if subject != 'name']
    dev = standard_deviation(scores)
    student_devs.append({'name': student['name'], 'dev': dev})

# In độ lệch chuẩn của từng học sinh
for student in student_devs:
    print(f"{student['name']}: Độ lệch chuẩn = {student['dev']:.2f}")

# Khởi tạo danh sách để lưu điểm của từng môn học
subjects = ['math', 'literature', 'english']
subject_scores = {subject: [] for subject in subjects}

# Lấy điểm của từng môn học từ dữ liệu học sinh
for student in students_scores:
    for subject in subjects:
        subject_scores[subject].append(student[subject])

# Tính độ lệch chuẩn của từng môn học
subject_deviation = {subject: calculate_deviation(scores) for subject, scores in subject_scores.items()}

# Tìm môn học có độ lệch chuẩn thấp nhất và cao nhất
lowest_deviation_subject = min(subject_deviation, key=subject_deviation.get)
highest_deviation_subject = max(subject_deviation, key=subject_deviation.get)

# In kết quả
print("\nKết quả:")
print(f"Môn học có điểm đồng đều nhất: {lowest_deviation_subject.capitalize()} với độ lệch chuẩn {subject_deviation[lowest_deviation_subject]:.2f}")
print(f"Môn học có điểm lệch nhất: {highest_deviation_subject.capitalize()} với độ lệch chuẩn {subject_deviation[highest_deviation_subject]:.2f}")

#Bai 3.1
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Hỗ trợ tiếng Việt

# Dữ liệu 1: Diện tích và Giá
du_lieu_1 = {
    'dien_tich': [1460, 2108, 1743, 1499, 1864, 2391, 1977, 1610, 1530, 1759, 1821, 2216],
    'gia': [288700, 309300, 301400, 291100, 302400, 314900, 305400, 297000, 292400, 298200, 304300, 311700]
}

# Dữ liệu 2: Khoảng cách và Giá
du_lieu_2 = {
    'khoang_cach': [2.6, 0.8, 1.0, 0.6, 1.5, 2.0, 3.4, 1.2, 3.6, 1.7],
    'gia': [214, 376, 280, 362, 200, 190, 236, 244, 128, 165]
}

# Tạo DataFrame
df1 = pd.DataFrame(du_lieu_1)
df2 = pd.DataFrame(du_lieu_2)

# Tính hệ số tương quan Pearson
tuong_quan_1 = stats.pearsonr(df1['dien_tich'], df1['gia'])
tuong_quan_2 = stats.pearsonr(df2['khoang_cach'], df2['gia'])

# Tạo biểu đồ
plt.figure(figsize=(12, 5))

# Biểu đồ 1: Diện tích và Giá
plt.subplot(1, 2, 1)
plt.scatter(df1['dien_tich'], df1['gia'])
plt.xlabel('Diện tích (feet vuông)')
plt.ylabel('Giá ($)')
plt.title(f'Diện tích và Giá\nHệ số tương quan: {tuong_quan_1[0]:.3f}')

# Biểu đồ 2: Khoảng cách và Giá
plt.subplot(1, 2, 2)
plt.scatter(df2['khoang_cach'], df2['gia'])
plt.xlabel('Khoảng cách từ trung tâm (dặm)')
plt.ylabel('Giá (nghìn $)')
plt.title(f'Khoảng cách và Giá\nHệ số tương quan: {tuong_quan_2[0]:.3f}')

# In kết quả
print("Kết quả phân tích tương quan:")
print(f"\nDữ liệu 1 - Diện tích và Giá:")
print(f"Hệ số tương quan: {tuong_quan_1[0]:.3f}")
print(f"Giá trị P: {tuong_quan_1[1]:.3f}")

print(f"\nDữ liệu 2 - Khoảng cách từ trung tâm và Giá:")
print(f"Hệ số tương quan: {tuong_quan_2[0]:.3f}")
print(f"Giá trị P: {tuong_quan_2[1]:.3f}")

#Bai 4.1
import numpy as np

# Đọc dữ liệu từ file Temp.txt vào mảng numpy
data_numpy = np.loadtxt('Temp.txt')

# Kiểm tra thông tin về mảng data_numpy
print("Kích thước của mảng (shape):", data_numpy.shape)
print("Số chiều của mảng (ndim):", data_numpy.ndim)
print("Kiểu dữ liệu của mảng (dtype):", data_numpy.dtype)
print("Số phần tử trong mảng (size):", data_numpy.size)

#Bai 4.2 và 4.3
import numpy as np

# Đọc dữ liệu từ file Temp.txt vào mảng numpy
data_numpy = np.loadtxt('Temp.txt', dtype=float)

# Tính nhiệt độ cao nhất (Max), thấp nhất (Min), và nhiệt độ trung bình cho tất cả các thành phố
max_temp = np.max(data_numpy[:, 1:], axis=1)  # Max theo từng thành phố
min_temp = np.min(data_numpy[:, 1:], axis=1)  # Min theo từng thành phố
avg_temp = np.mean(data_numpy[:, 1:], axis=1)  # Nhiệt độ trung bình theo từng thành phố

# Tính nhiệt độ cao nhất, thấp nhất và trung bình cho cả 6 thành phố
overall_max = np.max(max_temp)
overall_min = np.min(min_temp)
overall_avg = np.mean(avg_temp)

# Hiển thị kết quả
print(f"Nhiệt độ cao nhất toàn bộ: {overall_max}")
print(f"Nhiệt độ thấp nhất toàn bộ: {overall_min}")
print(f"Nhiệt độ trung bình toàn bộ: {overall_avg:.2f}")

#Bai 4.4
import numpy as np

# Đọc dữ liệu từ file Temp.txt vào mảng numpy
data_numpy = np.loadtxt('Temp.txt', dtype=float)

# Tính các giá trị thống kê cho từng thành phố
max_temp = np.max(data_numpy[:, 1:], axis=1)  # Max theo từng thành phố
min_temp = np.min(data_numpy[:, 1:], axis=1)  # Min theo từng thành phố
avg_temp = np.mean(data_numpy[:, 1:], axis=1)  # Nhiệt độ trung bình theo từng thành phố

# Tính giá trị thống kê chung cho tất cả các thành phố
overall_max = np.max(max_temp)
overall_min = np.min(min_temp)
overall_avg = np.mean(avg_temp)

# Tạo ma trận thống kê data_thongke với 3 hàng và 7 cột
data_thongke = np.zeros((3, 7))

# Điền dữ liệu vào ma trận
data_thongke[0, :6] = max_temp  # Hàng 0: Nhiệt độ Max của từng thành phố
data_thongke[1, :6] = np.round(avg_temp, 2)  # Hàng 1: Nhiệt độ trung bình của từng thành phố (làm tròn 2 chữ số)
data_thongke[2, :6] = min_temp  # Hàng 2: Nhiệt độ Min của từng thành phố

# Cập nhật cột cuối cùng với giá trị thống kê chung
data_thongke[0, 6] = overall_max  # Cột cuối: Nhiệt độ Max chung
data_thongke[1, 6] = np.round(overall_avg, 2)  # Cột cuối: Nhiệt độ trung bình chung (làm tròn 2 chữ số)
data_thongke[2, 6] = overall_min  # Cột cuối: Nhiệt độ Min chung

# Lưu ma trận thống kê vào file thongke.txt
np.savetxt('thongke.txt', data_thongke, fmt='%.2f', delimiter='\t', header='Max\tAvg\tMin\tMax\tAvg\tMin\tTotal')

# Hiển thị ma trận để kiểm tra
print("Ma trận thống kê:\n", data_thongke)

#Bai 5.1
import numpy as np

# Đọc dữ liệu từ file Diamonds.txt vào biến data_diamond
data_diamond = np.loadtxt('Diamonds.txt', dtype=float)

# In ra thông tin về kích thước, số chiều, kiểu dữ liệu và số phần tử của biến data_diamond
print("Kích thước của mảng:", data_diamond.shape)
print("Số chiều của mảng:", data_diamond.ndim)
print("Kiểu dữ liệu của mảng:", data_diamond.dtype)
print("Số phần tử của mảng:", data_diamond.size)

#Bai 5.2
import numpy as np

# Đọc dữ liệu từ file Diamonds.txt vào biến data_diamond
data_diamond = np.loadtxt('Diamonds.txt', dtype=float)

# Tách mảng data_diamond thành 2 vector: diamond_size và diamond_price
diamond_size = data_diamond[:, 0]  # Trọng lượng (cột đầu tiên)
diamond_price = data_diamond[:, 2]  # Giá bán (cột thứ ba)

# Hiển thị kết quả
print("Vector trọng lượng của kim cương (diamond_size):")
print(diamond_size)

print("Vector giá bán của kim cương (diamond_price):")
print(diamond_price)

#Bai 5.8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Dữ liệu mẫu (trích xuất từ đồ thị)
data = {
    'trong_luong': [
        0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0, 1.2, 1.5, 1.7, 2.0, 2.2, 2.5, 3.0, 3.5, 4.0
    ],
    'gia': [
        1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 12000, 13000, 14000, 15000, 16000, 16500, 16000, 18000
    ]
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Tính hệ số tương quan
correlation = stats.pearsonr(df['trong_luong'], df['gia'])

# Thiết lập font hỗ trợ tiếng Việt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# Tạo biểu đồ
plt.figure(figsize=(10, 6))
plt.scatter(df['trong_luong'], df['gia'], color='blue', alpha=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

# Đặt tên cho các trục và tiêu đề
plt.xlabel('Trọng lượng (Carat)')
plt.ylabel('Giá bán ($)')
plt.title('Mối tương quan giữa trọng lượng và giá bán kim cương')

# Vẽ đường hồi quy tuyến tính
z = np.polyfit(df['trong_luong'], df['gia'], 1)
p = np.poly1d(z)
plt.plot(df['trong_luong'], p(df['trong_luong']), "r--", alpha=0.8)

# In kết quả
print("Kết quả phân tích tương quan:")
print(f"Hệ số tương quan Pearson: {correlation[0]:.4f}")
print(f"Giá trị P: {correlation[1]:.4f}")
print(f"Hệ số xác định (R²): {correlation[0]**2:.4f}")

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()