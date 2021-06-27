import random
import string
from PyQt5 import QtWidgets
import sys


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.uzunluk =  QtWidgets.QLineEdit()
        self.label = QtWidgets.QLabel("Parola uzunluğunu giriniz.")
        self.olustur = QtWidgets.QPushButton("Oluştur")
        self.label2 = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.uzunluk)
        v_box.addWidget(self.label)
        v_box.addWidget(self.olustur)
        v_box.addWidget(self.label2)

        

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Password Generator")

        self.olustur.clicked.connect(self.generator)
        
        self.show()

    def generator(self):

        uzunluk = int(self.uzunluk.text())

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = lower + upper + num + symbols

        temp = random.sample(all,uzunluk)
        password = "".join(temp)

        with open ("şifre.txt","a") as file:
          file.write(f"{password}\n")

        password_label = self.label2.setText(password)
        
        

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())