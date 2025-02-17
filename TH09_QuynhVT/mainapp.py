import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QMessageBox
from PyQt6.uic import loadUi

class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("TH09_QuynhVT/main_ui.ui", self)

        # Thêm các ô nhập vào layout
        # Lấy các widget từ UI thay vì tạo mới
        self.txtID = self.findChild(QLineEdit, "txtID")
        self.txtName = self.findChild(QLineEdit, "txtTen")
        self.txtDescription = self.findChild(QLineEdit, "txtMoTa")
        self.txtPrice = self.findChild(QLineEdit, "txtGia")
        self.txtCategory = self.findChild(QLineEdit, "txtLoai")
        self.txtStatus = self.findChild(QLineEdit, "txtTrangThai")


        # Kết nối sự kiện
        self.btnAdd.clicked.connect(self.add_menu)
        self.btnEdit.clicked.connect(self.edit_menu)
        self.btnDelete.clicked.connect(self.delete_menu)
        self.btnRefresh.clicked.connect(self.reset_form)

        # Load dữ liệu lên bảng
        self.load_data()

    def connect_db(self):
        """Kết nối MySQL"""
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )

    def load_data(self):
        """Load dữ liệu từ MySQL vào bảng tableMenu"""
        db = self.connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM menu")
        rows = cursor.fetchall()
        db.close()

        self.tableMenu.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                self.tableMenu.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def add_menu(self):
        """Thêm món mới từ dữ liệu nhập"""
        name = self.txtName.text()
        description = self.txtDescription.text()
        price = self.txtPrice.text()
        category = self.txtCategory.text()
        status = self.txtStatus.text()

        if not name or not description or not price or not category or not status:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        db = self.connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO menu (name, description, price, category, availability) VALUES (%s, %s, %s, %s, %s)",
                       (name, description, float(price), category, int(status)))
        db.commit()
        db.close()
        self.load_data()
        self.reset_form()  # Làm mới form

    def edit_menu(self):
        """Chỉnh sửa mục đã chọn từ dữ liệu nhập"""
        row = self.tableMenu.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một mục để sửa!")
            return

        menu_id = self.tableMenu.item(row, 0).text()
        name = self.txtName.text()
        description = self.txtDescription.text()
        price = self.txtPrice.text()
        category = self.txtCategory.text()
        status = self.txtStatus.text()

        if not name or not description or not price or not category or not status:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        db = self.connect_db()
        cursor = db.cursor()
        cursor.execute("UPDATE menu SET name=%s, description=%s, price=%s, category=%s, availability=%s WHERE menu_id=%s",
                       (name, description, float(price), category, int(status), menu_id))
        db.commit()
        db.close()
        self.load_data()
        self.reset_form()  # Làm mới form

    def reset_form(self):
        """Xóa trắng toàn bộ các ô nhập liệu"""
        self.txtID.clear()
        self.txtName.clear()
        self.txtDescription.clear()
        self.txtPrice.clear()
        self.txtCategory.clear()
        self.txtStatus.clear()
        

    def delete_menu(self):
        """Xóa mục đã chọn"""
        row = self.tableMenu.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một mục để xóa!")
            return

        menu_id = self.tableMenu.item(row, 0).text()

        db = self.connect_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM menu WHERE menu_id=%s", (menu_id,))
        db.commit()
        db.close()
        self.load_data()
        self.reset_form()  # Làm mới form

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuApp()
    window.show()
    sys.exit(app.exec())
