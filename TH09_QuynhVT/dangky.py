import sys
import mysql
import hashlib
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from loginapp import LoginApp 

# Thông tin kết nối MySQL
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "test"

# Kết nối đến cơ sở dữ liệu
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )

class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Đăng ký tài khoản")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_username = QLabel("Tên đăng nhập:")
        self.input_username = QLineEdit()

        self.label_email = QLabel("Email:")
        self.input_email = QLineEdit()

        self.label_password = QLabel("Mật khẩu:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_confirm_password = QLabel("Xác nhận mật khẩu:")
        self.input_confirm_password = QLineEdit()
        self.input_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_register = QPushButton("Đăng ký")
        self.btn_register.clicked.connect(self.register_user)

        self.btn_back = QPushButton("Quay lại đăng nhập")
        self.btn_back.clicked.connect(self.go_to_login)

        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)

        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)

        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)

        layout.addWidget(self.label_confirm_password)
        layout.addWidget(self.input_confirm_password)

        layout.addWidget(self.btn_register)
        layout.addWidget(self.btn_back)

        self.setLayout(layout)

    def register_user(self):
        username = self.input_username.text().strip()
        email = self.input_email.text().strip()
        password = self.input_password.text().strip()
        confirm_password = self.input_confirm_password.text().strip()

        if not username or not email or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        # Mã hóa mật khẩu bằng SHA-256
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            conn = connect_db()
            cursor = conn.cursor()

            # Kiểm tra username hoặc email đã tồn tại chưa
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            existing_user = cursor.fetchone()
            if existing_user:
                QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc email đã tồn tại!")
                return

            # Thêm người dùng vào database
            cursor.execute("INSERT INTO users (username, password_hash, email, role) VALUES (%s, %s, %s, %s)",
                           (username, password_hash, email, 'customer'))
            conn.commit()
            QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
            self.go_to_login()

        except mysql.Error as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối cơ sở dữ liệu: {str(e)}")
        finally:
            if conn:
                conn.close()

    def go_to_login(self):
        self.login_form = LoginApp()
        self.login_form.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register_form = RegisterForm()
    register_form.show()
    sys.exit(app.exec())
