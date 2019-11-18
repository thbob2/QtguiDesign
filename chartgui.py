# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainview = QtWidgets.QMainWindow()
    ui = Ui_mainview()
    ui.setupUi(mainview)
    mainview.show()
    sys.exit(app.exec_())
