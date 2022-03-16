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
        self.label3 = QLabel("Enter your hostname:", self)
        self.label4 = QLabel("Enter your Api key:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 60)
        self.text = QLineEdit(self)
        self.text.move(10, 120)
        self.label3.move(10, 100)
        self.label3 = QLabel("Answer:", self)
        self.label3.move(10, 150)
        self.label4.move(10, 180)
        self.text = QLineEdit(self)
        self.text.move(10, 200)
        self.button = QPushButton("Send", self)
        self.button.move(10, 300)
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 225)
    
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname):
        url = "http://%s" % (hostname)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()