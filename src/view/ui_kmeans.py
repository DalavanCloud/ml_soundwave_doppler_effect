# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_kmeans.ui'
#
# Created: Sun Feb 09 14:16:59 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1378, 827)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1371, 771))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(360, 169, 961, 521))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rightPage_sa = QtGui.QScrollArea(self.groupBox)
        self.rightPage_sa.setGeometry(QtCore.QRect(500, 20, 441, 491))
        self.rightPage_sa.setWidgetResizable(True)
        self.rightPage_sa.setObjectName(_fromUtf8("rightPage_sa"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 439, 489))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.rightPage_sa.setWidget(self.scrollAreaWidgetContents_2)
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 481, 491))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.qwtPlot_page_1 = Qwt5.QwtPlot(self.groupBox)
        self.qwtPlot_page_1.setEnabled(False)
        self.qwtPlot_page_1.setGeometry(QtCore.QRect(30, 30, 461, 481))
        self.qwtPlot_page_1.setObjectName(_fromUtf8("qwtPlot_page_1"))
        self.startRecognition_bt = QtGui.QPushButton(self.tab)
        self.startRecognition_bt.setGeometry(QtCore.QRect(30, 30, 281, 121))
        self.startRecognition_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"}"))
        self.startRecognition_bt.setIconSize(QtCore.QSize(36, 36))
        self.startRecognition_bt.setObjectName(_fromUtf8("startRecognition_bt"))
        self.gesture0_lb = QtGui.QLabel(self.tab)
        self.gesture0_lb.setGeometry(QtCore.QRect(20, 200, 100, 100))
        self.gesture0_lb.setObjectName(_fromUtf8("gesture0_lb"))
        self.gesture1_lb = QtGui.QLabel(self.tab)
        self.gesture1_lb.setGeometry(QtCore.QRect(20, 320, 100, 100))
        self.gesture1_lb.setObjectName(_fromUtf8("gesture1_lb"))
        self.gesture4_lb = QtGui.QLabel(self.tab)
        self.gesture4_lb.setGeometry(QtCore.QRect(20, 580, 100, 100))
        self.gesture4_lb.setObjectName(_fromUtf8("gesture4_lb"))
        self.gesture3_lb = QtGui.QLabel(self.tab)
        self.gesture3_lb.setGeometry(QtCore.QRect(20, 440, 100, 100))
        self.gesture3_lb.setObjectName(_fromUtf8("gesture3_lb"))
        self.gesture4_lb_2 = QtGui.QLabel(self.tab)
        self.gesture4_lb_2.setGeometry(QtCore.QRect(150, 580, 191, 100))
        self.gesture4_lb_2.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.gesture4_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gesture4_lb_2.setObjectName(_fromUtf8("gesture4_lb_2"))
        self.gesture1_lb_2 = QtGui.QLabel(self.tab)
        self.gesture1_lb_2.setGeometry(QtCore.QRect(150, 320, 191, 100))
        self.gesture1_lb_2.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.gesture1_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gesture1_lb_2.setObjectName(_fromUtf8("gesture1_lb_2"))
        self.gesture0_lb_2 = QtGui.QLabel(self.tab)
        self.gesture0_lb_2.setGeometry(QtCore.QRect(150, 200, 191, 100))
        self.gesture0_lb_2.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.gesture0_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gesture0_lb_2.setObjectName(_fromUtf8("gesture0_lb_2"))
        self.gesture3_lb_2 = QtGui.QLabel(self.tab)
        self.gesture3_lb_2.setGeometry(QtCore.QRect(150, 440, 191, 100))
        self.gesture3_lb_2.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.gesture3_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gesture3_lb_2.setObjectName(_fromUtf8("gesture3_lb_2"))
        self.headline_lb = QtGui.QLabel(self.tab)
        self.headline_lb.setGeometry(QtCore.QRect(370, 30, 951, 30))
        self.headline_lb.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.headline_lb.setObjectName(_fromUtf8("headline_lb"))
        self.headline_lb_2 = QtGui.QLabel(self.tab)
        self.headline_lb_2.setGeometry(QtCore.QRect(370, 80, 951, 81))
        self.headline_lb_2.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.headline_lb_2.setObjectName(_fromUtf8("headline_lb_2"))
        self.headline_lb_3 = QtGui.QLabel(self.tab)
        self.headline_lb_3.setGeometry(QtCore.QRect(800, 700, 521, 41))
        self.headline_lb_3.setStyleSheet(_fromUtf8("QLabel {\n"
"    font-size: 18pt;\n"
"    font-family: Courier;\n"
"\n"
"}"))
        self.headline_lb_3.setObjectName(_fromUtf8("headline_lb_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.qwtPlot_6 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_6.setEnabled(False)
        self.qwtPlot_6.setGeometry(QtCore.QRect(850, 10, 171, 150))
        self.qwtPlot_6.setObjectName(_fromUtf8("qwtPlot_6"))
        self.qwtPlot_29 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_29.setEnabled(False)
        self.qwtPlot_29.setGeometry(QtCore.QRect(680, 460, 171, 150))
        self.qwtPlot_29.setObjectName(_fromUtf8("qwtPlot_29"))
        self.qwtPlot_10 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_10.setEnabled(False)
        self.qwtPlot_10.setGeometry(QtCore.QRect(170, 160, 171, 150))
        self.qwtPlot_10.setObjectName(_fromUtf8("qwtPlot_10"))
        self.openFile_bt = QtGui.QPushButton(self.tab_2)
        self.openFile_bt.setGeometry(QtCore.QRect(640, 610, 121, 21))
        self.openFile_bt.setObjectName(_fromUtf8("openFile_bt"))
        self.qwtPlot_1 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_1.setEnabled(False)
        self.qwtPlot_1.setGeometry(QtCore.QRect(0, 10, 171, 150))
        self.qwtPlot_1.setObjectName(_fromUtf8("qwtPlot_1"))
        self.qwtPlot_24 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_24.setEnabled(False)
        self.qwtPlot_24.setGeometry(QtCore.QRect(1190, 310, 171, 150))
        self.qwtPlot_24.setObjectName(_fromUtf8("qwtPlot_24"))
        self.qwtPlot_25 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_25.setEnabled(False)
        self.qwtPlot_25.setGeometry(QtCore.QRect(0, 460, 171, 150))
        self.qwtPlot_25.setObjectName(_fromUtf8("qwtPlot_25"))
        self.qwtPlot_31 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_31.setEnabled(False)
        self.qwtPlot_31.setGeometry(QtCore.QRect(1020, 460, 171, 150))
        self.qwtPlot_31.setObjectName(_fromUtf8("qwtPlot_31"))
        self.qwtPlot_32 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_32.setEnabled(False)
        self.qwtPlot_32.setGeometry(QtCore.QRect(1190, 460, 171, 150))
        self.qwtPlot_32.setObjectName(_fromUtf8("qwtPlot_32"))
        self.initKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.initKMeans_bt.setGeometry(QtCore.QRect(860, 690, 91, 23))
        self.initKMeans_bt.setObjectName(_fromUtf8("initKMeans_bt"))
        self.qwtPlot_22 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_22.setEnabled(False)
        self.qwtPlot_22.setGeometry(QtCore.QRect(850, 310, 171, 150))
        self.qwtPlot_22.setObjectName(_fromUtf8("qwtPlot_22"))
        self.viewCase3_rb = QtGui.QRadioButton(self.tab_2)
        self.viewCase3_rb.setGeometry(QtCore.QRect(460, 660, 101, 17))
        self.viewCase3_rb.setObjectName(_fromUtf8("viewCase3_rb"))
        self.learnKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.learnKMeans_bt.setGeometry(QtCore.QRect(860, 710, 91, 23))
        self.learnKMeans_bt.setObjectName(_fromUtf8("learnKMeans_bt"))
        self.qwtPlot_23 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_23.setEnabled(False)
        self.qwtPlot_23.setGeometry(QtCore.QRect(1020, 310, 171, 150))
        self.qwtPlot_23.setObjectName(_fromUtf8("qwtPlot_23"))
        self.qwtPlot_20 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_20.setEnabled(False)
        self.qwtPlot_20.setGeometry(QtCore.QRect(510, 310, 171, 150))
        self.qwtPlot_20.setObjectName(_fromUtf8("qwtPlot_20"))
        self.perRatio_sb = QtGui.QSpinBox(self.tab_2)
        self.perRatio_sb.setGeometry(QtCore.QRect(1270, 670, 91, 20))
        self.perRatio_sb.setMaximum(99)
        self.perRatio_sb.setProperty("value", 10)
        self.perRatio_sb.setObjectName(_fromUtf8("perRatio_sb"))
        self.qwtPlot_28 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_28.setEnabled(False)
        self.qwtPlot_28.setGeometry(QtCore.QRect(510, 460, 171, 150))
        self.qwtPlot_28.setObjectName(_fromUtf8("qwtPlot_28"))
        self.qwtPlot_5 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_5.setEnabled(False)
        self.qwtPlot_5.setGeometry(QtCore.QRect(680, 10, 171, 150))
        self.qwtPlot_5.setObjectName(_fromUtf8("qwtPlot_5"))
        self.qwtPlot_3 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_3.setEnabled(False)
        self.qwtPlot_3.setGeometry(QtCore.QRect(340, 10, 171, 150))
        self.qwtPlot_3.setObjectName(_fromUtf8("qwtPlot_3"))
        self.viewCase4_rb = QtGui.QRadioButton(self.tab_2)
        self.viewCase4_rb.setGeometry(QtCore.QRect(460, 680, 101, 17))
        self.viewCase4_rb.setObjectName(_fromUtf8("viewCase4_rb"))
        self.class4_bt = QtGui.QPushButton(self.tab_2)
        self.class4_bt.setGeometry(QtCore.QRect(1130, 710, 61, 23))
        self.class4_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class4_bt.setObjectName(_fromUtf8("class4_bt"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(770, 620, 77, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frames_sb = QtGui.QSpinBox(self.layoutWidget)
        self.frames_sb.setMaximum(9999999)
        self.frames_sb.setProperty("value", 24)
        self.frames_sb.setObjectName(_fromUtf8("frames_sb"))
        self.verticalLayout_3.addWidget(self.frames_sb)
        self.record_bt = QtGui.QPushButton(self.layoutWidget)
        self.record_bt.setObjectName(_fromUtf8("record_bt"))
        self.verticalLayout_3.addWidget(self.record_bt)
        self.qwtPlot_2 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_2.setEnabled(False)
        self.qwtPlot_2.setGeometry(QtCore.QRect(170, 10, 171, 150))
        self.qwtPlot_2.setObjectName(_fromUtf8("qwtPlot_2"))
        self.showLearnArray_bt = QtGui.QPushButton(self.tab_2)
        self.showLearnArray_bt.setGeometry(QtCore.QRect(640, 710, 121, 21))
        self.showLearnArray_bt.setObjectName(_fromUtf8("showLearnArray_bt"))
        self.class2_bt = QtGui.QPushButton(self.tab_2)
        self.class2_bt.setGeometry(QtCore.QRect(1130, 670, 61, 23))
        self.class2_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class2_bt.setObjectName(_fromUtf8("class2_bt"))
        self.useInitCentroids_cb = QtGui.QCheckBox(self.tab_2)
        self.useInitCentroids_cb.setGeometry(QtCore.QRect(960, 690, 81, 20))
        self.useInitCentroids_cb.setObjectName(_fromUtf8("useInitCentroids_cb"))
        self.qwtPlot_14 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_14.setEnabled(False)
        self.qwtPlot_14.setGeometry(QtCore.QRect(850, 160, 171, 150))
        self.qwtPlot_14.setObjectName(_fromUtf8("qwtPlot_14"))
        self.n_init_lb = QtGui.QLabel(self.tab_2)
        self.n_init_lb.setGeometry(QtCore.QRect(860, 640, 31, 21))
        self.n_init_lb.setObjectName(_fromUtf8("n_init_lb"))
        self.class1_bt = QtGui.QPushButton(self.tab_2)
        self.class1_bt.setGeometry(QtCore.QRect(1130, 650, 61, 23))
        self.class1_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class1_bt.setObjectName(_fromUtf8("class1_bt"))
        self.loadNoiseFile_bt = QtGui.QPushButton(self.tab_2)
        self.loadNoiseFile_bt.setGeometry(QtCore.QRect(770, 670, 81, 31))
        self.loadNoiseFile_bt.setObjectName(_fromUtf8("loadNoiseFile_bt"))
        self.saveFile_bt = QtGui.QPushButton(self.tab_2)
        self.saveFile_bt.setGeometry(QtCore.QRect(960, 620, 81, 51))
        self.saveFile_bt.setObjectName(_fromUtf8("saveFile_bt"))
        self.n_init_sb = QtGui.QSpinBox(self.tab_2)
        self.n_init_sb.setGeometry(QtCore.QRect(900, 640, 51, 22))
        self.n_init_sb.setMinimum(1)
        self.n_init_sb.setMaximum(9999)
        self.n_init_sb.setProperty("value", 10)
        self.n_init_sb.setObjectName(_fromUtf8("n_init_sb"))
        self.kMeansLoop_bt = QtGui.QPushButton(self.tab_2)
        self.kMeansLoop_bt.setGeometry(QtCore.QRect(1050, 690, 71, 41))
        self.kMeansLoop_bt.setObjectName(_fromUtf8("kMeansLoop_bt"))
        self.maxIteration_sb = QtGui.QSpinBox(self.tab_2)
        self.maxIteration_sb.setGeometry(QtCore.QRect(900, 660, 51, 22))
        self.maxIteration_sb.setMaximum(10000)
        self.maxIteration_sb.setProperty("value", 10)
        self.maxIteration_sb.setObjectName(_fromUtf8("maxIteration_sb"))
        self.qwtPlot_19 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_19.setEnabled(False)
        self.qwtPlot_19.setGeometry(QtCore.QRect(340, 310, 171, 150))
        self.qwtPlot_19.setObjectName(_fromUtf8("qwtPlot_19"))
        self.loadClassArray_bt = QtGui.QPushButton(self.tab_2)
        self.loadClassArray_bt.setGeometry(QtCore.QRect(1200, 682, 61, 51))
        self.loadClassArray_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.loadClassArray_bt.setObjectName(_fromUtf8("loadClassArray_bt"))
        self.qwtPlot_8 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_8.setEnabled(False)
        self.qwtPlot_8.setGeometry(QtCore.QRect(1190, 10, 171, 150))
        self.qwtPlot_8.setObjectName(_fromUtf8("qwtPlot_8"))
        self.mulFiles_cb = QtGui.QCheckBox(self.tab_2)
        self.mulFiles_cb.setGeometry(QtCore.QRect(570, 620, 61, 17))
        self.mulFiles_cb.setObjectName(_fromUtf8("mulFiles_cb"))
        self.cutSides_lb = QtGui.QLabel(self.tab_2)
        self.cutSides_lb.setGeometry(QtCore.QRect(570, 650, 54, 13))
        self.cutSides_lb.setObjectName(_fromUtf8("cutSides_lb"))
        self.cutSides_sb = QtGui.QSpinBox(self.tab_2)
        self.cutSides_sb.setGeometry(QtCore.QRect(570, 670, 61, 20))
        self.cutSides_sb.setMaximum(64)
        self.cutSides_sb.setProperty("value", 20)
        self.cutSides_sb.setObjectName(_fromUtf8("cutSides_sb"))
        self.perRatio_lb = QtGui.QLabel(self.tab_2)
        self.perRatio_lb.setGeometry(QtCore.QRect(1270, 650, 91, 16))
        self.perRatio_lb.setObjectName(_fromUtf8("perRatio_lb"))
        self.segMargin_sb = QtGui.QSpinBox(self.tab_2)
        self.segMargin_sb.setGeometry(QtCore.QRect(1050, 630, 71, 20))
        self.segMargin_sb.setMaximum(99)
        self.segMargin_sb.setProperty("value", 1)
        self.segMargin_sb.setObjectName(_fromUtf8("segMargin_sb"))
        self.qwtPlot_18 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_18.setEnabled(False)
        self.qwtPlot_18.setGeometry(QtCore.QRect(170, 310, 171, 150))
        self.qwtPlot_18.setObjectName(_fromUtf8("qwtPlot_18"))
        self.qwtPlot_21 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_21.setEnabled(False)
        self.qwtPlot_21.setGeometry(QtCore.QRect(680, 310, 171, 150))
        self.qwtPlot_21.setObjectName(_fromUtf8("qwtPlot_21"))
        self.qwtPlot_16 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_16.setEnabled(False)
        self.qwtPlot_16.setGeometry(QtCore.QRect(1190, 160, 171, 150))
        self.qwtPlot_16.setObjectName(_fromUtf8("qwtPlot_16"))
        self.viewCase1_rb = QtGui.QRadioButton(self.tab_2)
        self.viewCase1_rb.setGeometry(QtCore.QRect(460, 620, 82, 17))
        self.viewCase1_rb.setObjectName(_fromUtf8("viewCase1_rb"))
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(20, 620, 431, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 109))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(30, 10, 411, 81))
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(640, 652, 121, 61))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.skipFramesLA_lb = QtGui.QLabel(self.layoutWidget_2)
        self.skipFramesLA_lb.setObjectName(_fromUtf8("skipFramesLA_lb"))
        self.verticalLayout_7.addWidget(self.skipFramesLA_lb)
        self.skipFramesLA_sb = QtGui.QSpinBox(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.skipFramesLA_sb.sizePolicy().hasHeightForWidth())
        self.skipFramesLA_sb.setSizePolicy(sizePolicy)
        self.skipFramesLA_sb.setMaximum(2048)
        self.skipFramesLA_sb.setSingleStep(1)
        self.skipFramesLA_sb.setObjectName(_fromUtf8("skipFramesLA_sb"))
        self.verticalLayout_7.addWidget(self.skipFramesLA_sb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.arrayIdxLF_lb = QtGui.QLabel(self.layoutWidget_2)
        self.arrayIdxLF_lb.setObjectName(_fromUtf8("arrayIdxLF_lb"))
        self.verticalLayout_8.addWidget(self.arrayIdxLF_lb)
        self.arrayIdxLF_sb = QtGui.QSpinBox(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.arrayIdxLF_sb.sizePolicy().hasHeightForWidth())
        self.arrayIdxLF_sb.setSizePolicy(sizePolicy)
        self.arrayIdxLF_sb.setMinimum(0)
        self.arrayIdxLF_sb.setMaximum(2048)
        self.arrayIdxLF_sb.setProperty("value", 0)
        self.arrayIdxLF_sb.setObjectName(_fromUtf8("arrayIdxLF_sb"))
        self.verticalLayout_8.addWidget(self.arrayIdxLF_sb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.viewCase2_rb = QtGui.QRadioButton(self.tab_2)
        self.viewCase2_rb.setGeometry(QtCore.QRect(460, 640, 101, 17))
        self.viewCase2_rb.setObjectName(_fromUtf8("viewCase2_rb"))
        self.k_lb_2 = QtGui.QLabel(self.tab_2)
        self.k_lb_2.setGeometry(QtCore.QRect(860, 660, 31, 21))
        self.k_lb_2.setObjectName(_fromUtf8("k_lb_2"))
        self.class0_bt = QtGui.QPushButton(self.tab_2)
        self.class0_bt.setGeometry(QtCore.QRect(1130, 630, 61, 23))
        self.class0_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class0_bt.setObjectName(_fromUtf8("class0_bt"))
        self.kNumber_sb = QtGui.QSpinBox(self.tab_2)
        self.kNumber_sb.setGeometry(QtCore.QRect(900, 620, 51, 22))
        self.kNumber_sb.setProperty("value", 5)
        self.kNumber_sb.setObjectName(_fromUtf8("kNumber_sb"))
        self.qwtPlot_4 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_4.setEnabled(False)
        self.qwtPlot_4.setGeometry(QtCore.QRect(510, 10, 171, 150))
        self.qwtPlot_4.setObjectName(_fromUtf8("qwtPlot_4"))
        self.showPlot_bt = QtGui.QPushButton(self.tab_2)
        self.showPlot_bt.setGeometry(QtCore.QRect(460, 700, 171, 31))
        self.showPlot_bt.setObjectName(_fromUtf8("showPlot_bt"))
        self.qwtPlot_30 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_30.setEnabled(False)
        self.qwtPlot_30.setGeometry(QtCore.QRect(850, 460, 171, 150))
        self.qwtPlot_30.setObjectName(_fromUtf8("qwtPlot_30"))
        self.class3_bt = QtGui.QPushButton(self.tab_2)
        self.class3_bt.setGeometry(QtCore.QRect(1130, 690, 61, 23))
        self.class3_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class3_bt.setObjectName(_fromUtf8("class3_bt"))
        self.qwtPlot_27 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_27.setEnabled(False)
        self.qwtPlot_27.setGeometry(QtCore.QRect(340, 460, 171, 150))
        self.qwtPlot_27.setObjectName(_fromUtf8("qwtPlot_27"))
        self.loadLearnArray_bt = QtGui.QPushButton(self.tab_2)
        self.loadLearnArray_bt.setGeometry(QtCore.QRect(640, 630, 121, 21))
        self.loadLearnArray_bt.setObjectName(_fromUtf8("loadLearnArray_bt"))
        self.qwtPlot_11 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_11.setEnabled(False)
        self.qwtPlot_11.setGeometry(QtCore.QRect(340, 160, 171, 150))
        self.qwtPlot_11.setObjectName(_fromUtf8("qwtPlot_11"))
        self.testKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.testKMeans_bt.setGeometry(QtCore.QRect(1270, 700, 91, 23))
        self.testKMeans_bt.setObjectName(_fromUtf8("testKMeans_bt"))
        self.qwtPlot_7 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_7.setEnabled(False)
        self.qwtPlot_7.setGeometry(QtCore.QRect(1020, 10, 171, 150))
        self.qwtPlot_7.setObjectName(_fromUtf8("qwtPlot_7"))
        self.checkKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.checkKMeans_bt.setGeometry(QtCore.QRect(1270, 620, 91, 23))
        self.checkKMeans_bt.setObjectName(_fromUtf8("checkKMeans_bt"))
        self.qwtPlot_17 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_17.setEnabled(False)
        self.qwtPlot_17.setGeometry(QtCore.QRect(0, 310, 171, 150))
        self.qwtPlot_17.setObjectName(_fromUtf8("qwtPlot_17"))
        self.k_lb = QtGui.QLabel(self.tab_2)
        self.k_lb.setGeometry(QtCore.QRect(860, 620, 21, 21))
        self.k_lb.setObjectName(_fromUtf8("k_lb"))
        self.loadCentorids_bt = QtGui.QPushButton(self.tab_2)
        self.loadCentorids_bt.setGeometry(QtCore.QRect(960, 710, 81, 23))
        self.loadCentorids_bt.setObjectName(_fromUtf8("loadCentorids_bt"))
        self.class6_bt = QtGui.QPushButton(self.tab_2)
        self.class6_bt.setGeometry(QtCore.QRect(1200, 650, 61, 23))
        self.class6_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class6_bt.setObjectName(_fromUtf8("class6_bt"))
        self.segMargin_lb = QtGui.QLabel(self.tab_2)
        self.segMargin_lb.setGeometry(QtCore.QRect(1050, 619, 54, 10))
        self.segMargin_lb.setObjectName(_fromUtf8("segMargin_lb"))
        self.qwtPlot_9 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_9.setEnabled(False)
        self.qwtPlot_9.setGeometry(QtCore.QRect(0, 160, 171, 150))
        self.qwtPlot_9.setObjectName(_fromUtf8("qwtPlot_9"))
        self.saveCentorids_bt = QtGui.QPushButton(self.tab_2)
        self.saveCentorids_bt.setGeometry(QtCore.QRect(960, 670, 81, 23))
        self.saveCentorids_bt.setObjectName(_fromUtf8("saveCentorids_bt"))
        self.qwtPlot_12 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_12.setEnabled(False)
        self.qwtPlot_12.setGeometry(QtCore.QRect(510, 160, 171, 150))
        self.qwtPlot_12.setObjectName(_fromUtf8("qwtPlot_12"))
        self.class5_bt = QtGui.QPushButton(self.tab_2)
        self.class5_bt.setGeometry(QtCore.QRect(1200, 630, 61, 23))
        self.class5_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class5_bt.setObjectName(_fromUtf8("class5_bt"))
        self.qwtPlot_26 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_26.setEnabled(False)
        self.qwtPlot_26.setGeometry(QtCore.QRect(170, 460, 171, 150))
        self.qwtPlot_26.setObjectName(_fromUtf8("qwtPlot_26"))
        self.reduceDim_bt = QtGui.QPushButton(self.tab_2)
        self.reduceDim_bt.setGeometry(QtCore.QRect(770, 700, 81, 31))
        self.reduceDim_bt.setObjectName(_fromUtf8("reduceDim_bt"))
        self.qwtPlot_13 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_13.setEnabled(False)
        self.qwtPlot_13.setGeometry(QtCore.QRect(680, 160, 171, 150))
        self.qwtPlot_13.setObjectName(_fromUtf8("qwtPlot_13"))
        self.qwtPlot_15 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_15.setEnabled(False)
        self.qwtPlot_15.setGeometry(QtCore.QRect(1020, 160, 171, 150))
        self.qwtPlot_15.setObjectName(_fromUtf8("qwtPlot_15"))
        self.kMeansLoop_sb = QtGui.QSpinBox(self.tab_2)
        self.kMeansLoop_sb.setGeometry(QtCore.QRect(1050, 661, 71, 20))
        self.kMeansLoop_sb.setMaximum(10000)
        self.kMeansLoop_sb.setProperty("value", 50)
        self.kMeansLoop_sb.setObjectName(_fromUtf8("kMeansLoop_sb"))
        self.kMeansLoop_lb = QtGui.QLabel(self.tab_2)
        self.kMeansLoop_lb.setGeometry(QtCore.QRect(1050, 650, 54, 10))
        self.kMeansLoop_lb.setObjectName(_fromUtf8("kMeansLoop_lb"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1378, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "kmeans utility", None))
        self.groupBox.setTitle(_translate("MainWindow", "___", None))
        self.startRecognition_bt.setText(_translate("MainWindow", "START RECOGNITION", None))
        self.gesture0_lb.setText(_translate("MainWindow", "TextLabel", None))
        self.gesture1_lb.setText(_translate("MainWindow", "TextLabel", None))
        self.gesture4_lb.setText(_translate("MainWindow", "TextLabel", None))
        self.gesture3_lb.setText(_translate("MainWindow", "TextLabel", None))
        self.gesture4_lb_2.setText(_translate("MainWindow", "Double Push\n"
"Beginn / End", None))
        self.gesture1_lb_2.setText(_translate("MainWindow", "Top To Bottom\n"
"Page Down", None))
        self.gesture0_lb_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.gesture0_lb_2.setText(_translate("MainWindow", "Bottom To Top\n"
"Page Up", None))
        self.gesture3_lb_2.setText(_translate("MainWindow", "Single Push\n"
"Change Font", None))
        self.headline_lb.setText(_translate("MainWindow", "Machine Learning", None))
        self.headline_lb_2.setText(_translate("MainWindow", "Klassifikationsverfahren zur Gestenerkennung\n"
"mit Hilfe des schallbasierten Doppler-Effekts", None))
        self.headline_lb_3.setText(_translate("MainWindow", "Alexander Baumgärtner & Robert Brylka", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gesture Recognizer", None))
        self.openFile_bt.setText(_translate("MainWindow", "open file", None))
        self.initKMeans_bt.setText(_translate("MainWindow", "init k-means", None))
        self.viewCase3_rb.setText(_translate("MainWindow", "view seg norm", None))
        self.learnKMeans_bt.setText(_translate("MainWindow", "learn k-means", None))
        self.viewCase4_rb.setText(_translate("MainWindow", "view ", None))
        self.class4_bt.setText(_translate("MainWindow", "Class 4", None))
        self.record_bt.setText(_translate("MainWindow", "record frames", None))
        self.showLearnArray_bt.setText(_translate("MainWindow", "show array", None))
        self.class2_bt.setText(_translate("MainWindow", "Class 2", None))
        self.useInitCentroids_cb.setText(_translate("MainWindow", "use init cen", None))
        self.n_init_lb.setText(_translate("MainWindow", "n init", None))
        self.class1_bt.setText(_translate("MainWindow", "Class 1", None))
        self.loadNoiseFile_bt.setText(_translate("MainWindow", "load noise file", None))
        self.saveFile_bt.setText(_translate("MainWindow", "save\n"
"segmented\n"
"data", None))
        self.kMeansLoop_bt.setText(_translate("MainWindow", "learn kMeans\n"
"loop", None))
        self.loadClassArray_bt.setText(_translate("MainWindow", "load\n"
"class\n"
"array", None))
        self.mulFiles_cb.setText(_translate("MainWindow", "mul files", None))
        self.cutSides_lb.setText(_translate("MainWindow", "cut sides", None))
        self.perRatio_lb.setText(_translate("MainWindow", "% ratio class diff", None))
        self.viewCase1_rb.setText(_translate("MainWindow", "view init", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.skipFramesLA_lb.setText(_translate("MainWindow", "skip frames", None))
        self.arrayIdxLF_lb.setText(_translate("MainWindow", "array idx", None))
        self.viewCase2_rb.setText(_translate("MainWindow", "view init norm", None))
        self.k_lb_2.setText(_translate("MainWindow", "max it", None))
        self.class0_bt.setText(_translate("MainWindow", "Class 0", None))
        self.showPlot_bt.setText(_translate("MainWindow", "show plot", None))
        self.class3_bt.setText(_translate("MainWindow", "Class 3", None))
        self.loadLearnArray_bt.setText(_translate("MainWindow", "load array", None))
        self.testKMeans_bt.setText(_translate("MainWindow", "test kMeans", None))
        self.checkKMeans_bt.setText(_translate("MainWindow", "k-means online", None))
        self.k_lb.setText(_translate("MainWindow", "k", None))
        self.loadCentorids_bt.setText(_translate("MainWindow", "load centroids", None))
        self.class6_bt.setText(_translate("MainWindow", "Class 6", None))
        self.segMargin_lb.setText(_translate("MainWindow", "seg margin", None))
        self.saveCentorids_bt.setText(_translate("MainWindow", "save centroids", None))
        self.class5_bt.setText(_translate("MainWindow", "Class 5", None))
        self.reduceDim_bt.setText(_translate("MainWindow", "reduce Dim", None))
        self.kMeansLoop_lb.setText(_translate("MainWindow", "kMeans loop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Advance", None))

from PyQt4 import Qwt5
