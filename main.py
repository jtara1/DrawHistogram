# @Author: j
# @Date:   10-Oct-2016
# @Email:  jtara@tuta.io
# @Last modified by:   j
# @Last modified time: 10-Oct-2016

import sys
from PyQt4 import QtGui

from gui import Gui
from draw_histogram import DrawHistogram

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
