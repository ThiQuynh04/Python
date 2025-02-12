import sys
import mysql.connector
import pandas as pd
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, 
    QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox
)
from fpdf import FPDF

class ReportWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Báo cáo & Xuất Dữ liệu")
        self.setGeometry(350, 150, 600, 400)

        # Tạo bảng hiển thị dữ liệu
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Tên tài khoản", "Mật khẩu"])
        self.load_data()

        # Các nút chức năng
        self.btn_export_csv = QPushButton("Xuất CSV")
        self.btn_export_excel = QPushButton("Xuất Excel")
        self.btn_export_pdf = QPushButton("Xuất PDF")

        self.btn_export_csv.clicked.connect(self.export_csv)
        self.btn_export_excel.clicked.connect(self.export_excel)
        self.btn_export_pdf.clicked.connect(self.export_pdf)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btn_export_csv)
        layout.addWidget(self.btn_export_excel)
        layout.addWidget(self.btn_export_pdf)

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

    def load_data(self):
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

    def export_csv(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Lưu file CSV", "", "CSV Files (*.csv)", options=options)
        if file_name:
            conn = self.connect_db()
            query = "SELECT * FROM users"
            df = pd.read_sql(query, conn)
            df.to_csv(file_name, index=False)
            conn.close()
            QMessageBox.information(self, "Thành công", "Xuất dữ liệu CSV thành công!")

    def export_excel(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Lưu file Excel", "", "Excel Files (*.xlsx)", options=options)
        if file_name:
            conn = self.connect_db()
            query = "SELECT * FROM users"
            df = pd.read_sql(query, conn)
            df.to_excel(file_name, index=False)
            conn.close()
            QMessageBox.information(self, "Thành công", "Xuất dữ liệu Excel thành công!")

    def export_pdf(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Lưu file PDF", "", "PDF Files (*.pdf)", options=options)
        if file_name:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            conn.close()

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", style="", size=12)
            pdf.cell(200, 10, txt="Báo Cáo Người Dùng", ln=True, align='C')

            for user in users:
                pdf.cell(200, 10, txt=f"ID: {user[0]} - Username: {user[1]} - Password: {user[2]}", ln=True, align='L')

            pdf.output(file_name)
            QMessageBox.information(self, "Thành công", "Xuất dữ liệu PDF thành công!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportWindow()
    window.show()
    sys.exit(app.exec())
