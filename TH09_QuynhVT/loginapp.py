import sys
import mysql.connector
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import subprocess

# Kết nối đến cơ sở dữ liệu
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TH09_QuynhVT/login_ui.ui", self)  # Load giao diện từ file UI
        
        self.pushButton.clicked.connect(self.login)  # Gán sự kiện cho nút Đăng nhập

    def login(self):
        email = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        
        if not email or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s AND password_hash = %s", (email, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")
                self.open_main_app()
            else:
                QMessageBox.warning(self, "Lỗi", "Email hoặc mật khẩu không đúng!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối CSDL: {e}")
    
    def open_main_app(self):
        self.close()
        subprocess.Popen([sys.executable, "TH09_QuynhVT/mainapp.py"])  # Mở ứng dụng chính

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())  # Đổi exec_() thành exec()
