import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit
from PyQt5 import uic


class MyWidget(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('UI.ui', self)
		self.btn.clicked.connect(self.run)

	def run(self):
		self.gragh.clear()
		self.gragh.plot([eval(self.line.text()) for x in range(int(self.lineEdit.text()), int(self.lineEdit_2.text()) + 1)])


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())