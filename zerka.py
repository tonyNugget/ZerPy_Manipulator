# #Anthony Zerka
# #Abstract: Image manipulation tool

#Imports
import sys
import ctypes	#Used to grab screen resolution
from tkinter import *	#Used for selecting image with GUI
from tkinter.filedialog import askopenfilename	#Used for selecting image with GUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

print(filename)
""" 
# Anthony Zerka / Project
# Features:
# 		* Image filters
# 		* chroma key
# 		* image blur
# 		* image encryption?
		
"""

#Find screen resolution
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


#Create main window with options (choose image, list of effects, exit)



#Main window
class Window():
	def __init__(self, x, y):
	 	self.x = x
	 	self.y = y
        window = QtGui.QWidget()
	def print():
		print("dddd")
	# 	#Set_Window_Title
	# 	window.setWindowTitle('ZERKA  \\Z/')
	# 	#Set Layout
	# 	layout = QVBoxLayout()
	# 	#Set_Background
		
	def show(self):
		self.show()
	# 	table = addToolBar("NIGGER")
		
		
	# 	#Show
	# 	window.show()
	# 	#Exit
	# 	#sys.exit(Application.exec_())


#Main_Loop
# def main():
   
#    window.show()
   


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window(20,50)
	win.show()
	sys.exit(app.exec_())


