import webbrowser
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
        self.ip = QLineEdit(self)
        self.ip.move(10, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 60)

        self.label3 = QLabel("Enter your hostname:", self)
        self.label3.move(0, 90)
        self.host = QLineEdit(self)
        self.host.move(10, 110)
        self.label4 = QLabel("Answer: ", self)
        self.label4.move(10, 140)


        self.label5 = QLabel("Enter your API_KEY:", self)
        self.label5.move(0, 170)
        self.api = QLineEdit(self)
        self.api.move(10, 180)

        self.label6 = QLabel("Answer: ", self)
        self.label6.move(10, 225)

        
        #self.text.move(10, 200)
        self.button = QPushButton("Send", self)
        self.button.move(10, 300)
    
        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.host.text()
        ip = self.ip.text()
        api_key = self.api.text()


        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip, api_key)
            if res:
                self.label6.setText("\n \n Longitude: %s \n Latitude: %s \n" % (res["Longitude"], res["Latitude"]))
                self.label6.adjustSize()
                self.show()
                url2 = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (res["Latitude"], res["Longitude"])
                webbrowser.open_new_tab(url2)

    def __query(self, hostname,ip, api_key):
        url = "http://%s/ip/%s?key=%s" % (hostname,ip, api_key) 
        print(url)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()