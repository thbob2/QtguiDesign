from chartgui import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import matplotlib.style as mplstyle
import sys

class ChartWindow(QMainWindow,Ui_mainview):
    def __init__(self,parent=None):
        super(mainview,self).__init__(parent)
        self.plotwidget = MplHist(self.histTab)
        self.plotwidget.setObjectName("plotwidget")
        self.histplot.addWidget(self.plotwidget)
        self.histobtn.clicked.connect(self.drawHist)

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

    def main(self):
        self.show()
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chartapp = ChartWindow()
    chartapp.main()
    sys.exit(app.exec_())