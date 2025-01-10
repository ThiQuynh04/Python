import numpy as np

# Kích thước ma trận
n = 12

# Tạo ma trận vuông cấp n với các giá trị ngẫu nhiên trong khoảng từ 0 đến 100
matrix = np.random.randint(0, 101, size=(n, n))

# In ma trận
def analyze_matrix():
    # Verify matrix properties
    shape = matrix.shape
    total_elements = matrix.size
    dimensions = len(matrix.shape)
    
    # Basic matrix information
    print(matrix)
    print("Phân tích ma trận:")
    print(f"1. Kiểu dữ liệu: {matrix.dtype}")
    print(f"2. Kích thước: {n}")
    print(f"3. Tổng số phần tử: {total_elements}")
    print(f"4. Số chiều: {dimensions}")
    
    # Verify constraints
    print("\nKiểm tra ràng buộc:")
    print(f"- Ma trận vuông cấp n×n: {'Đúng' if shape[0] == shape[1] else 'Sai'}")
    print(f"- n = 12: {'Đúng' if shape[0] == 12 else 'Sai'}")
    in_range = np.all((matrix >= 0) & (matrix <= 100))
    print(f"- Các phần tử trong khoảng [0-100]: {'Đúng' if in_range else 'Sai'}")
    integers = np.all(matrix.astype(int) == matrix)
    print(f"- Các phần tử là số nguyên: {'Đúng' if integers else 'Sai'}")

    # Additional analysis
    print("\nThống kê thêm:")
    print(f"- Giá trị lớn nhất: {np.max(matrix)}")
    print(f"- Giá trị nhỏ nhất: {np.min(matrix)}")
    print(f"- Giá trị trung bình: {np.mean(matrix):.2f}")

# Run the analysis
analyze_matrix()
