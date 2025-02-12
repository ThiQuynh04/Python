import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from main_window import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Đăng nhập")
        self.setGeometry(400, 200, 300, 200)

        # Label và ô nhập
        self.label_user = QLabel("Tài khoản:")
        self.input_user = QLineEdit(self)
        self.label_pass = QLabel("Mật khẩu:")
        self.input_pass = QLineEdit(self)
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

        # Nút đăng nhập
        self.btn_login = QPushButton("Đăng nhập", self)
        self.btn_login.clicked.connect(self.check_login)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.input_pass)
        layout.addWidget(self.btn_login)
        self.setLayout(layout)

    def check_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        # Kết nối MySQL
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="quanly"
            )
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
                self.close()  # Đóng cửa sổ đăng nhập
                self.main_window = MainWindow()  # Mở trang chính
                self.main_window.show()
            else:
                QMessageBox.warning(self, "Lỗi", "Sai tài khoản hoặc mật khẩu!")

            cursor.close()
            conn.close()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối MySQL: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
