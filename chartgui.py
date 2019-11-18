# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import matplotlib.style as mplstyle
import sys

class Ui_mainview(object):
    def setupUi(self, mainview):
        mainview.setObjectName("mainview")
        mainview.resize(804, 443)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainview.sizePolicy().hasHeightForWidth())
        mainview.setSizePolicy(sizePolicy)
        mainview.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(mainview)
        self.centralwidget.setObjectName("centralwidget")
        self.myTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.myTabs.setGeometry(QtCore.QRect(0, 10, 801, 431))
        self.myTabs.setMaximumSize(QtCore.QSize(801, 441))
        self.myTabs.setObjectName("myTabs")
        self.histTab = QtWidgets.QWidget()
        self.histTab.setObjectName("histTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.histTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 781, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.histplot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.histplot.setContentsMargins(0, 0, 0, 0)
        self.histplot.setObjectName("histplot")
        self.histobtn = QtWidgets.QPushButton(self.histTab)
        self.histobtn.setGeometry(QtCore.QRect(220, 0, 201, 23))
        self.histobtn.setObjectName("histobtn")
        self.label = QtWidgets.QLabel(self.histTab)
        self.label.setGeometry(QtCore.QRect(120, 0, 84, 23))
        self.label.setObjectName("label")
        self.myTabs.addTab(self.histTab, "")
        self.barTab = QtWidgets.QWidget()
        self.barTab.setObjectName("barTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.barTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 38, 781, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.barplot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.barplot.setContentsMargins(0, 0, 0, 0)
        self.barplot.setObjectName("barplot")
        self.barbtn = QtWidgets.QPushButton(self.barTab)
        self.barbtn.setGeometry(QtCore.QRect(670, 10, 75, 23))
        self.barbtn.setObjectName("barbtn")
        self.label_2 = QtWidgets.QLabel(self.barTab)
        self.label_2.setGeometry(QtCore.QRect(35, 10, 71, 20))
        self.label_2.setObjectName("label_2")
        self.myTabs.addTab(self.barTab, "")
        mainview.setCentralWidget(self.centralwidget)

        self.plotwidget = MplHist(self.histTab)
        self.plotwidget.setObjectName("plotwidget")
        self.histplot.addWidget(self.plotwidget)

        self.histobtn.clicked.connect(self.drawHist)

        self.retranslateUi(mainview)
        self.myTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainview)

    def retranslateUi(self, mainview):
        _translate = QtCore.QCoreApplication.translate
        mainview.setWindowTitle(_translate("mainview", "Chart Window"))
        self.histobtn.setText(_translate("mainview", "push "))
        self.label.setText(_translate("mainview", "Histogramme Gen"))
        self.myTabs.setTabText(self.myTabs.indexOf(self.histTab), _translate("mainview", "Histograme"))
        self.barbtn.setText(_translate("mainview", "push"))
        self.label_2.setText(_translate("mainview", "bar chart gen"))
        self.myTabs.setTabText(self.myTabs.indexOf(self.barTab), _translate("mainview", "Bar Chart"))

    def drawHist(self):
        self.plotwidget.canvas.ax.clear()
        
        axes =[1,2,3,5,6,8,9,10,111,55,22,66,88]
        pos = range(len(axes))

        self.plotwidget.canvas.ax.plot(pos,[e for e in axes],color='b')
        self.plotwidget.canvas.ax.set_xticks(pos)
        self.plotwidget.canvas.ax.set_xticklabels([e for e in pos])
        for label in self.plotwidget.canvas.ax.xaxis.get_ticklabels():
            label.set_rotation(45)
            label.set_fontsize(5)
        self.plotwidget.canvas.ax.grid(True,linestyle='-',linewidth=1)
        self.plotwidget.canvas.ax.legend('positive',loc ='upper right')
        self.plotwidget.canvas.ax.set_title("just an example")
        self.plotwidget.canvas.draw()


# the matplotlib classes section 
# the canvas class used for dispaly the the figure 
class MplCanvas(Canvas):
	def __init__(self):
		self.fig = Figure()
		self.ax = self.fig.add_subplot(111)
		Canvas.__init__(self,self.fig)
		Canvas.setSizePolicy(self,QSizePolicy.Preferred,QSizePolicy.Preferred)
		Canvas.updateGeometry(self)
		#mplstyle.use(['dark_background', 'ggplot', 'fast'])
# the mpl widget class this is used for drawing 
class MplHist(QtWidgets.QWidget):
	def __init__(self,parent=None):
		QtWidgets.QWidget.__init__(self,parent)
		self.canvas = MplCanvas()
		#mplstyle.use([ 'ggplot', 'fast'])
		self.vbl = QVBoxLayout()
		self.vbl.addWidget(self.canvas)
		self.setLayout(self.vbl)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainview = QtWidgets.QMainWindow()
    ui = Ui_mainview()
    ui.setupUi(mainview)
    mainview.show()
    sys.exit(app.exec_())
