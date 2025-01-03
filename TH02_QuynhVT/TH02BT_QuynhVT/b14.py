# Bài 14: Tìm số Max – Min - Mean
n = int(input("Nhập số lượng phần tử: "))
heights = []
print("Nhập chiều cao của từng sinh viên (m), nhập -1 để kết thúc:")
for i in range(n):
    while True:
        try:
            height = float(input(f"Nhập chiều cao sinh viên thứ {i+1}: "))
            if height > 0:
                heights.append(height)
                break
            else:
                print("Vui lòng nhập chiều cao lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

if heights:
    max_height = max(heights)
    min_height = min(heights)
    mean_height = sum(heights) / len(heights)
    students_above_mean = len([h for h in heights if h >= mean_height])

    print("Chiều cao cao nhất:", max_height)
    print("Chiều cao thấp nhất:", min_height)
    print("Chiều cao trung bình:", round(mean_height, 2))
    print("Số sinh viên cao hơn hoặc bằng chiều cao trung bình:", students_above_mean)
else:
    print("Không có dữ liệu chiều cao.")