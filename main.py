# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from functools import partial
import random
from PySide6.QtUiTools import QUiLoader


class Main:
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn_standard.clicked.connect(self.standard)
        self.ui.btn_strong.clicked.connect(self.strong)
        self.ui.btn_super.clicked.connect(self.super)

    def standard(self):
        list = []
        number = random.randint(1, 50)
        big = random.choice(
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "Z"])
        special = random.choice(["!", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")"])

        list.append([number, big, special])
        self.ui.tb_standard.setText(str(list))

    def strong(self):
        list = []
        number1 = random.randint(500, 900)
        number2 = random.randint(50, 150)
        big1 = random.choice(
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "Z"])
        big2 = random.choice(
            ["a", "b", "c", "d", "e", "f", "g"])
        special = random.choice(["!", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")"])
        list.append([number1, big1, special, number2, big2])
        self.ui.tb_strong.setText(str(list))

    def super(self):
        list = []
        number1 = random.randint(1000, 2000)
        number2 = random.randint(500, 3000)
        big1 = random.choice(
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "Z"])
        big2 = random.choice(
            ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "z"])
        special1 = random.choice(["!", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")"])
        special2 = random.choice(["!", "@", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")"])
        list.append([number2, big2, special1, number1, big1, special2])
        self.ui.tb_super.setText(str(list))


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec_())
