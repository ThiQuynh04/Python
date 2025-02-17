import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from user_management import UserManagementWindow
from report_window import ReportWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Trang Chủ - Quản Lý")
        self.setGeometry(300, 150, 500, 400)
        
        # Tạo biến để giữ cửa sổ UserManagementWindow
        self.user_window = None  

        # Tạo layout chính
        layout = QVBoxLayout()

        # Tiêu đề trang chủ
        self.label = QLabel("Chào mừng bạn đến với hệ thống quản lý", self)
        layout.addWidget(self.label)

        # Các nút chức năng
        self.btn_users = QPushButton("Quản lý người dùng", self)
        self.btn_users.clicked.connect(self.open_user_management)
   


        self.btn_reports = QPushButton("Báo cáo thống kê", self)
        self.btn_exit = QPushButton("Thoát", self)
        self.btn_reports.clicked.connect(self.open_report_window)

        # Thêm vào layout
        layout.addWidget(self.btn_users)
        layout.addWidget(self.btn_reports)
        layout.addWidget(self.btn_exit)

        # Sự kiện nút bấm
        self.btn_exit.clicked.connect(self.close)

        # Cấu hình giao diện chính
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_user_management(self):
        print("Mở cửa sổ Quản lý người dùng...")  # Debug
        if self.user_window is None or not self.user_window.isVisible():
            self.user_window = UserManagementWindow()  # Giữ tham chiếu
            self.user_window.show()
            self.user_window.activateWindow()  # Đảm bảo cửa sổ xuất hiện trên màn hình
    
    def open_report_window(self):
        self.report_window = ReportWindow()
        self.report_window.show()
        
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
