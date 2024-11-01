
#import hou

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui


from .qt.ui import Ui_Dialog

class Ui(QtWidgets.QWidget):
	def __init__(self,parent=None):
		QtWidgets.QWidget.__init__(self,parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		# connections
		#self.ui.mybutton.connect(self.myfunction)
