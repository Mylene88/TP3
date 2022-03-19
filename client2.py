from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        
        self.label1 = QLabel("Enter your IP:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 60)

        self.label3 = QLabel("Enter your hostname:", self)
        self.label3.move(0, 90)
        self.text = QLineEdit(self)
        self.text.move(10, 110)
        self.label4 = QLabel("Answer: ", self)
        self.label4.move(10, 140)


        self.label5 = QLabel("Enter your API_KEY:", self)
        self.label5.move(0, 170)
        self.text = QLineEdit(self)
        self.text.move(10, 180)
        self.label6 = QLabel("Answer: ", self)
        self.label6.move(10, 225)

        
        self.text.move(10, 200)
        self.button = QPushButton("Send", self)
        self.button.move(10, 300)
    
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        IP = self.text.text()
        API_KEY = self.text.text()


        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname, IP, API_KEY)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.label4.setText("Answer%s" % (res["long"]))
                self.label4.adjustSize()
                self.label6.setText("Answer%s" % (res["lat"]))
                self.label6.adjustSize()
                self.show()

    def __query(self, hostname,IP, API_KEY):
        url = "http://ip-API_KEY.com/batch"
        #url = "http://%s%s" % (hostname, IP)
        r = requests.get(url, params=API_KEY)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()