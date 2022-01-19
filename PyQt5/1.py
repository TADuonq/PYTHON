import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtGui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # Khai báo nút ấn chạy
        self.uic.Button_start.clicked.connect(self.showscreen)
        # Khai báo nút dừng chương trình
        self.uic.Button_stop.clicked.connect(self.main_win.close)
    
    # def showscreen(self):
    #     # Đổi text trên màn hình screen
    #     self.uic.Screen.setText('Xin chào các bạn')
        
    def copytext(self):
        copy = self.uic.Screen_1.toPlainText()
        self.uic.Screen_2.setText(copy)
    
    def show(self):
        self.main_win.show()
        
if __name__ == "__main":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
        