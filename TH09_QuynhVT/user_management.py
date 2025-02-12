import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, 
    QTableWidget, QTableWidgetItem, QHBoxLayout, QLineEdit, QMessageBox
)

class UserManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quản lý Người Dùng")
        self.setGeometry(350, 150, 600, 400)

        # Tạo bảng hiển thị danh sách người dùng
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Tên tài khoản", "Mật khẩu"])
        self.load_users()

        # Các ô nhập dữ liệu
        self.input_user = QLineEdit(self)
        self.input_user.setPlaceholderText("Nhập tài khoản")

        self.input_pass = QLineEdit(self)
        self.input_pass.setPlaceholderText("Nhập mật khẩu")

        # Các nút chức năng
        self.btn_add = QPushButton("Thêm")
        self.btn_edit = QPushButton("Sửa")
        self.btn_delete = QPushButton("Xóa")

        # Sự kiện nút bấm
        self.btn_add.clicked.connect(self.add_user)
        self.btn_edit.clicked.connect(self.edit_user)
        self.btn_delete.clicked.connect(self.delete_user)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(QLabel("Tài khoản:"))
        layout.addWidget(self.input_user)
        layout.addWidget(QLabel("Mật khẩu:"))
        layout.addWidget(self.input_pass)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_edit)
        button_layout.addWidget(self.btn_delete)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quanly"
        )

    def load_users(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        self.table.setRowCount(len(users))

        for row_idx, user in enumerate(users):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(user[0])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(user[1]))
            self.table.setItem(row_idx, 2, QTableWidgetItem(user[2]))

        cursor.close()
        conn.close()

    def add_user(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        if username and password:
            conn = self.connect_db()
            cursor = conn.cursor()

            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                conn.commit()
                QMessageBox.information(self, "Thành công", "Thêm người dùng thành công!")
                self.load_users()
            except mysql.connector.Error as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi MySQL: {e}")
            
            cursor.close()
            conn.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ tài khoản và mật khẩu!")

    def edit_user(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một người dùng để sửa!")
            return

        user_id = self.table.item(selected_row, 0).text()
        new_username = self.input_user.text()
        new_password = self.input_pass.text()

        if new_username and new_password:
            conn = self.connect_db()
            cursor = conn.cursor()

            try:
                cursor.execute("UPDATE users SET username=%s, password=%s WHERE id=%s", (new_username, new_password, user_id))
                conn.commit()
                QMessageBox.information(self, "Thành công", "Cập nhật người dùng thành công!")
                self.load_users()
            except mysql.connector.Error as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi MySQL: {e}")

            cursor.close()
            conn.close()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập tài khoản và mật khẩu mới!")

    def delete_user(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một người dùng để xóa!")
            return

        user_id = self.table.item(selected_row, 0).text()

        reply = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xóa người dùng này?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            conn = self.connect_db()
            cursor = conn.cursor()

            try:
                cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
                conn.commit()
                QMessageBox.information(self, "Thành công", "Xóa người dùng thành công!")
                self.load_users()
            except mysql.connector.Error as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi MySQL: {e}")

            cursor.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserManagementWindow()
    window.show()
    sys.exit(app.exec())
