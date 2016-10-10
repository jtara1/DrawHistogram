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
    """Inherit from QDialog class to provide GUI to browse for a local file"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)


    def setupUi(self, Dialog):
        """Create main application & all objects of QObject contained inside
        of the application
        """
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
        """Update UI with new values"""
        Dialog.setWindowTitle(_translate("Dialog", "Create Histogram", None))
        self.lineEdit.setText(_translate("Dialog", filename, None))
        self.label.setText(_translate("Dialog", "Data File:", None))
        self.pushButton.setText(_translate("Dialog", "Browse", None))


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


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
