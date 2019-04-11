import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit, QPushButton, QAction, QMessageBox, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'POS Tagger - HINDI'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()
	 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		#self.statusBar().showMessage('Message in statusbar.')
		self.textbox = QLineEdit(self)
		self.textbox.move(20, 20)
		self.textbox.resize(280,40)
		
		self.createHorizontalLayout()
		windowLayout = QVBoxLayout()
		windowLayout.addWidget(self.horizontalGroupBox)
		self.setLayout(windowLayout)
		
		self.show()
		 
	def createHorizontalLayout(self):
		self.horizontalGroupBox = QGroupBox("Enter the Text to be POS Tagged")
		layout = QHBoxLayout()
		
		self.horizontalGroupBox.setLayout(layout)
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
