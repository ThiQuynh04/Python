from PyQt6.QtWidgets import QApplication, QMainWindow

class UserManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()

# Chạy ứng dụng PyQt6
app = QApplication([])
window = UserManagementWindow()
window.show()
app.exec()
