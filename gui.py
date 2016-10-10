# @Author: j
# @Date:   10-Oct-2016
# @Email:  jtara@tuta.io
# @Last modified by:   j
# @Last modified time: 10-Oct-2016

import sys, os
# from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

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
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        width, height = 650, 300
        mWidth, mHeight = 400, 300
        Dialog.setMinimumSize(mWidth, mHeight)
        Dialog.resize(width, height)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(width - 390, height - 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, width - 100, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, width - 100, 40))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 100, width - 100, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.getFileUi)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog, filename="example.data.csv"):
        Dialog.setWindowTitle(_translate("Dialog", "Create Histogram", None))
        self.lineEdit.setText(_translate("Dialog", filename, None))
        self.label.setText(_translate("Dialog", "Data File:", None))
        self.pushButton.setText(_translate("Dialog", "Browse", None))


    def getFileUi(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getcwd())
        filename = os.path.relpath(str(filename))
        self.retranslateUi(self, filename = filename)
        return filename


# # Create an PyQT4 application object.
# a = QApplication(sys.argv)
#
# # The QWidget widget is the base class of all user interface objects in PyQt4.
# w = QWidget()
#
# # Set window size.
# w.resize(320, 240)
#
# # Set window title
# w.setWindowTitle("Hello World!")
#
# # Get filename using QFileDialog
# filename = QFileDialog.getOpenFileName(w, 'Open File', os.getcwd())
# print filename
#
# # print file contents
# with open(filename, 'r') as f:
#     print(f.read())

# Show window

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
