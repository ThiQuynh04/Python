import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# Kết nối MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="QuanLyThuVien"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Lỗi kết nối", f"Lỗi MySQL: {err}")
        return None

# Hàm lấy danh sách bảng trong CSDL
def get_tables():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        conn.close()
        return tables
    return []

# Dictionary chứa các truy vấn và giải thích
query_explanations = {
    1: {
        "query": "SELECT * FROM SinhVien",
        "explanation": "Hiển thị tất cả thông tin của sinh viên trong thư viện"
    },
    2: {
        "query": "SELECT * FROM Sach WHERE SoLuong > 0",
        "explanation": "Hiển thị danh sách các sách còn trong kho (số lượng > 0)"
    },
    3: {
        "query": """SELECT sv.MaSV, sv.HoTen, s.TenSach, ms.NgayMuon, ms.HanTra 
                   FROM MuonSach ms 
                   JOIN SinhVien sv ON ms.MaSV = sv.MaSV 
                   JOIN Sach s ON ms.MaSach = s.MaSach 
                   WHERE ms.TrangThai = 'Đang mượn'""",
        "explanation": "Hiển thị danh sách sinh viên đang mượn sách, bao gồm thông tin: Mã SV, họ tên, tên sách, ngày mượn và hạn trả"
    },
    4: {
        "query": "SELECT * FROM SinhVien WHERE Lop = 'CNTT'",
        "explanation": "Hiển thị danh sách sinh viên thuộc lớp CNTT"
    },
    5: {
        "query": """SELECT t.TenTheLoai, COUNT(s.MaSach) AS SoLuongSach 
                   FROM Sach s 
                   JOIN TheLoai t ON s.MaTheLoai = t.MaTheLoai 
                   GROUP BY t.TenTheLoai""",
        "explanation": "Thống kê số lượng sách theo từng thể loại"
    },
    6: {
        "query": """SELECT sv.HoTen, s.TenSach, ms.HanTra 
                   FROM MuonSach ms 
                   JOIN SinhVien sv ON ms.MaSV = sv.MaSV 
                   JOIN Sach s ON ms.MaSach = s.MaSach 
                   WHERE ms.HanTra < CURDATE() AND ms.TrangThai = 'Đang mượn'""",
        "explanation": "Hiển thị danh sách sinh viên đang mượn sách quá hạn"
    },
    7: {
        "query": "DELETE FROM Sach WHERE SoLuong = 0",
        "explanation": "Xóa các sách có số lượng bằng 0 khỏi thư viện"
    },
    8: {
        "query": """UPDATE Sach 
                   SET SoLuong = SoLuong - 1 
                   WHERE MaSach = 'S001'""",
        "explanation": "Cập nhật giảm số lượng sách có mã S001 đi 1 đơn vị"
    },
    9: {
        "query": """SELECT sv.MaSV, sv.HoTen, COUNT(ms.MaMuon) AS SoLanMuon 
                   FROM MuonSach ms 
                   JOIN SinhVien sv ON ms.MaSV = sv.MaSV 
                   GROUP BY sv.MaSV, sv.HoTen""",
        "explanation": "Thống kê số lần mượn sách của mỗi sinh viên"
    },
    10: {
        "query": """SELECT * FROM Sach 
                    WHERE MaSach NOT IN (SELECT MaSach FROM MuonSach)""",
        "explanation": "Hiển thị danh sách các sách chưa từng được mượn"
    },
    11: {
        "query": """SELECT sv.MaSV, sv.HoTen, COUNT(ms.MaMuon) AS SoLanMuon 
                    FROM MuonSach ms 
                    JOIN SinhVien sv ON ms.MaSV = sv.MaSV 
                    GROUP BY sv.MaSV, sv.HoTen 
                    HAVING SoLanMuon > 3""",
        "explanation": "Hiển thị danh sách sinh viên đã mượn sách nhiều hơn 3 lần"
    },
    12: {
        "query": """SELECT t.TenTheLoai, COUNT(s.MaSach) AS SoLuongSach 
                    FROM Sach s 
                    JOIN TheLoai t ON s.MaTheLoai = t.MaTheLoai 
                    GROUP BY t.TenTheLoai 
                    HAVING SoLuongSach > 2""",
        "explanation": "Hiển thị các thể loại có nhiều hơn 2 cuốn sách"
    },
    13: {
        "query": """SELECT s.TenSach, COUNT(ms.MaMuon) AS SoLanMuon 
                    FROM MuonSach ms 
                    JOIN Sach s ON ms.MaSach = s.MaSach 
                    GROUP BY s.TenSach 
                    ORDER BY SoLanMuon DESC 
                    LIMIT 1""",
        "explanation": "Hiển thị cuốn sách được mượn nhiều nhất"
    },
    14: {
        "query": """SELECT sv.HoTen, s.TenSach, ms.NgayMuon 
                    FROM MuonSach ms 
                    JOIN SinhVien sv ON ms.MaSV = sv.MaSV 
                    JOIN Sach s ON ms.MaSach = s.MaSach 
                    ORDER BY ms.NgayMuon DESC 
                    LIMIT 1""",
        "explanation": "Hiển thị thông tin về lần mượn sách gần đây nhất"
    },
    15: {
        "query": "SELECT SUM(SoLuong) AS TongSoSach FROM Sach",
        "explanation": "Tính tổng số lượng sách có trong thư viện"
    }
}

# Hàm hiển thị dữ liệu của bảng
def display_table():
    selected_table = table_var.get()
    if not selected_table:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một bảng!")
        return

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {selected_table}")
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        
        clear_frame()
        
        # Hiển thị dữ liệu dạng bảng
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        
        for row in records:
            tree.insert("", "end", values=row)
        
        tree.pack(fill="both", expand=True)
        conn.close()

def clear_frame():
    # Xóa tất cả widgets trong frame
    for widget in frame.winfo_children():
        widget.destroy()

# Hàm thực thi truy vấn
def execute_query(query_id):
    query_info = query_explanations.get(query_id)
    if not query_info:
        messagebox.showerror("Lỗi", "Truy vấn không hợp lệ!")
        return

    clear_frame()

    # Hiển thị câu lệnh SQL và giải thích
    query_label = tk.Label(frame, text="Câu lệnh SQL:", font=("Arial", 10, "bold"))
    query_label.pack(anchor="w", padx=5, pady=5)
    
    query_text = tk.Text(frame, height=4, wrap=tk.WORD)
    query_text.insert(tk.END, query_info["query"])
    query_text.config(state='disabled')
    query_text.pack(fill="x", padx=5, pady=5)

    explanation_label = tk.Label(frame, text="Giải thích:", font=("Arial", 10, "bold"))
    explanation_label.pack(anchor="w", padx=5, pady=5)
    
    explanation_text = tk.Text(frame, height=2, wrap=tk.WORD)
    explanation_text.insert(tk.END, query_info["explanation"])
    explanation_text.config(state='disabled')
    explanation_text.pack(fill="x", padx=5, pady=5)

    # Thực thi truy vấn và hiển thị kết quả
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query_info["query"])
            records = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            result_label = tk.Label(frame, text="Kết quả:", font=("Arial", 10, "bold"))
            result_label.pack(anchor="w", padx=5, pady=5)

            # Hiển thị kết quả dạng bảng
            tree = ttk.Treeview(frame, columns=columns, show="headings")
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=120)
            
            for row in records:
                tree.insert("", "end", values=row)
            
            tree.pack(fill="both", expand=True, padx=5, pady=5)
        except mysql.connector.Error as err:
            messagebox.showerror("Lỗi", f"Lỗi khi thực hiện truy vấn: {err}")
        finally:
            conn.close()

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Quản lý Thư Viện")
root.geometry("800x600")

# Dropdown chọn bảng
table_var = tk.StringVar()
tables = get_tables()
table_menu = ttk.Combobox(root, textvariable=table_var, values=tables)
table_menu.pack(pady=10)
table_menu.set("Chọn bảng")

# Nút hiển thị dữ liệu
btn_show = tk.Button(root, text="Hiển thị dữ liệu", command=display_table)
btn_show.pack(pady=5)

# Khung chứa bảng dữ liệu
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Tạo các nút truy vấn
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# Sắp xếp các nút theo hàng (5 nút mỗi hàng)
for i in range(1, 16):
    btn = tk.Button(btn_frame, text=f"Truy vấn {i}", command=lambda q=i: execute_query(q))
    btn.grid(row=(i - 1) // 5, column=(i - 1) % 5, padx=5, pady=5)

root.mainloop()