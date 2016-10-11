# @Author: j
# @Date:   10-Oct-2016
# @Email:  jtara@tuta.io
# @Last modified by:   j
# @Last modified time: 10-Oct-2016

import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignal
# from PyQt4.QtCore import QEventLoop

from draw_histogram import DrawHistogram

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Gui(QtGui.QDialog):
    """Inherit from QDialog class to provide GUI to browse for a local file"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)


    def setupUi(self, Dialog):
        """Create main application & all objects of QObject contained inside
        of the application
        """
        self.setObjectName(_fromUtf8("Dialog"))
        width, height = 650, 300
        mWidth, mHeight = 400, 300
        self.setMinimumSize(mWidth, mHeight)
        self.resize(width, height)

        self.closeButton = QtGui.QPushButton(self)
        self.closeButton.setGeometry(QtCore.QRect(width - 150, 240, 100, 40))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.closeButton.clicked.connect(self.accept)

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 30, width - 100, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, width - 100, 40))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.browseButton = QtGui.QPushButton(self)
        self.browseButton.setGeometry(QtCore.QRect(50, 100, width - 100, 40))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.browseButton.clicked.connect(self.getFileUi)

        self.createButton = QtGui.QPushButton(self)
        self.createButton.setGeometry(QtCore.QRect(50, 170, width - 100, 40))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.createButton.clicked.connect(self.proceedToDrawHistogram)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, Dialog, filename="example.data.csv"):
        """Update UI with new values"""
        self.setWindowTitle(_translate("Dialog", "Draw Histogram", None))
        self.label.setText(_translate("Dialog", "Data File:", None))
        self.lineEdit.setText(_translate("Dialog", filename, None))
        self.browseButton.setText(_translate("Dialog", "Browse", None))
        self.createButton.setText(_translate("Dialog", "Create Histogram", None))
        self.closeButton.setText(_translate("Dialog", "Close", None))


    def getFileUi(self):
        """Brings up UI to browse and select a file then enters the relative
        path of that file into the lineEdit field text box"""
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getcwd())
        filename = os.path.relpath(str(filename))
        self.retranslateUi(self, filename = filename)
        return filename


    def getFilename(self):
        """Return the absolute path of the text in lineEdit field"""
        filename = str(self.lineEdit.text())
        filename = os.path.abspath(filename)
        # print(filename)
        return filename


    def proceedToDrawHistogram(self):
        hist = DrawHistogram(self.getFilename())
        hist.drawHistogram()


    # @staticmethod
    # def getFilename2(self, parent=None):
    #     gui = Gui(parent)
    #     result = gui.exec_()
    #     filename = self.getFilename()
    #     return (filename, result == QDialog.Accepted)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    gui.show()
    # filename, ok = Gui.getFilename2(app)
    # print(filename, ok)

    sys.exit(app.exec_())
