from gui import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import matplotlib.style as mplstyle

class ChartWindow(QMainWindow,Ui_mainview):
    def __init__(self,parent=None):
        super(ChartWindow,self).__init__(parent)
        self.plotwidget = MplHist(self.histTab)
        self.plotwidget.setObjectName("plotWidget")
        self.histplot.addWidget(self.plotwidget)
        self.histobtn.clicked.connect(self.drawHist)
    def drawHist(self):
        self.plotWidget.canvas.ax.clear()
        self.plotWidget.canvas.ax.plot(pos,[e['pos'] for e in axes],color='b')
		self.plotWidget.canvas.ax.plot(pos,[e['neg'] for e in axes],color='r')
        self.plotWidget.canvas.ax.set_xticks(pos)
		self.plotWidget.canvas.ax.set_xticklabels([e['date'] for e in axes])
		for label in self.plotWidget.canvas.ax.xaxis.get_ticklabels():
			label.set_rotation(45)
			label.set_fontsize(5)
		self.plotWidget.canvas.ax.grid(True,linestyle='-',linewidth=1)
		self.plotWidget.canvas.ax.legend(['positive','negative'],loc ='upper right')
		self.plotWidget.canvas.ax.set_title("Opinions Evolution of the "+title)
        self.plotWidget.canvas.draw()
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
class MplHist(QWidget):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.canvas = MplCanvas()
		#mplstyle.use([ 'ggplot', 'fast'])
		self.vbl = QVBoxLayout()
		self.vbl.addWidget(self.canvas)
		self.setLayout(self.vbl)