# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bob.ui'
#
# Created: Tue Jan 14 11:26:06 2014
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
        MainWindow.resize(1506, 943)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 0, 1441, 901))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.qwtPlot_tab1 = Qwt5.QwtPlot(self.tab)
        self.qwtPlot_tab1.setEnabled(False)
        self.qwtPlot_tab1.setGeometry(QtCore.QRect(20, 20, 1371, 831))
        self.qwtPlot_tab1.setObjectName(_fromUtf8("qwtPlot_tab1"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.qwtPlot_8 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_8.setEnabled(False)
        self.qwtPlot_8.setGeometry(QtCore.QRect(1260, 20, 181, 171))
        self.qwtPlot_8.setObjectName(_fromUtf8("qwtPlot_8"))
        self.qwtPlot_13 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_13.setEnabled(False)
        self.qwtPlot_13.setGeometry(QtCore.QRect(720, 190, 181, 171))
        self.qwtPlot_13.setObjectName(_fromUtf8("qwtPlot_13"))
        self.qwtPlot_21 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_21.setEnabled(False)
        self.qwtPlot_21.setGeometry(QtCore.QRect(720, 360, 181, 171))
        self.qwtPlot_21.setObjectName(_fromUtf8("qwtPlot_21"))
        self.qwtPlot_24 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_24.setEnabled(False)
        self.qwtPlot_24.setGeometry(QtCore.QRect(1260, 360, 181, 171))
        self.qwtPlot_24.setObjectName(_fromUtf8("qwtPlot_24"))
        self.qwtPlot_14 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_14.setEnabled(False)
        self.qwtPlot_14.setGeometry(QtCore.QRect(900, 190, 181, 171))
        self.qwtPlot_14.setObjectName(_fromUtf8("qwtPlot_14"))
        self.qwtPlot_22 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_22.setEnabled(False)
        self.qwtPlot_22.setGeometry(QtCore.QRect(900, 360, 181, 171))
        self.qwtPlot_22.setObjectName(_fromUtf8("qwtPlot_22"))
        self.qwtPlot_25 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_25.setEnabled(False)
        self.qwtPlot_25.setGeometry(QtCore.QRect(0, 530, 181, 171))
        self.qwtPlot_25.setObjectName(_fromUtf8("qwtPlot_25"))
        self.qwtPlot_26 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_26.setEnabled(False)
        self.qwtPlot_26.setGeometry(QtCore.QRect(180, 530, 181, 171))
        self.qwtPlot_26.setObjectName(_fromUtf8("qwtPlot_26"))
        self.qwtPlot_27 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_27.setEnabled(False)
        self.qwtPlot_27.setGeometry(QtCore.QRect(360, 530, 181, 171))
        self.qwtPlot_27.setObjectName(_fromUtf8("qwtPlot_27"))
        self.qwtPlot_28 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_28.setEnabled(False)
        self.qwtPlot_28.setGeometry(QtCore.QRect(540, 530, 181, 171))
        self.qwtPlot_28.setObjectName(_fromUtf8("qwtPlot_28"))
        self.qwtPlot_31 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_31.setEnabled(False)
        self.qwtPlot_31.setGeometry(QtCore.QRect(1080, 530, 181, 171))
        self.qwtPlot_31.setObjectName(_fromUtf8("qwtPlot_31"))
        self.qwtPlot_29 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_29.setEnabled(False)
        self.qwtPlot_29.setGeometry(QtCore.QRect(720, 530, 181, 171))
        self.qwtPlot_29.setObjectName(_fromUtf8("qwtPlot_29"))
        self.qwtPlot_32 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_32.setEnabled(False)
        self.qwtPlot_32.setGeometry(QtCore.QRect(1260, 530, 181, 171))
        self.qwtPlot_32.setObjectName(_fromUtf8("qwtPlot_32"))
        self.qwtPlot_30 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_30.setEnabled(False)
        self.qwtPlot_30.setGeometry(QtCore.QRect(900, 530, 181, 171))
        self.qwtPlot_30.setObjectName(_fromUtf8("qwtPlot_30"))
        self.qwtPlot_2 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_2.setEnabled(False)
        self.qwtPlot_2.setGeometry(QtCore.QRect(180, 20, 181, 171))
        self.qwtPlot_2.setObjectName(_fromUtf8("qwtPlot_2"))
        self.qwtPlot_3 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_3.setEnabled(False)
        self.qwtPlot_3.setGeometry(QtCore.QRect(360, 20, 181, 171))
        self.qwtPlot_3.setObjectName(_fromUtf8("qwtPlot_3"))
        self.qwtPlot_4 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_4.setEnabled(False)
        self.qwtPlot_4.setGeometry(QtCore.QRect(540, 20, 181, 171))
        self.qwtPlot_4.setObjectName(_fromUtf8("qwtPlot_4"))
        self.qwtPlot_5 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_5.setEnabled(False)
        self.qwtPlot_5.setGeometry(QtCore.QRect(720, 20, 181, 171))
        self.qwtPlot_5.setObjectName(_fromUtf8("qwtPlot_5"))
        self.qwtPlot_7 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_7.setEnabled(False)
        self.qwtPlot_7.setGeometry(QtCore.QRect(1080, 20, 181, 171))
        self.qwtPlot_7.setObjectName(_fromUtf8("qwtPlot_7"))
        self.qwtPlot_16 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_16.setEnabled(False)
        self.qwtPlot_16.setGeometry(QtCore.QRect(1260, 190, 181, 171))
        self.qwtPlot_16.setObjectName(_fromUtf8("qwtPlot_16"))
        self.qwtPlot_6 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_6.setEnabled(False)
        self.qwtPlot_6.setGeometry(QtCore.QRect(900, 20, 181, 171))
        self.qwtPlot_6.setObjectName(_fromUtf8("qwtPlot_6"))
        self.qwtPlot_9 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_9.setEnabled(False)
        self.qwtPlot_9.setGeometry(QtCore.QRect(0, 190, 181, 171))
        self.qwtPlot_9.setObjectName(_fromUtf8("qwtPlot_9"))
        self.qwtPlot_17 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_17.setEnabled(False)
        self.qwtPlot_17.setGeometry(QtCore.QRect(0, 360, 181, 171))
        self.qwtPlot_17.setObjectName(_fromUtf8("qwtPlot_17"))
        self.qwtPlot_15 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_15.setEnabled(False)
        self.qwtPlot_15.setGeometry(QtCore.QRect(1080, 190, 181, 171))
        self.qwtPlot_15.setObjectName(_fromUtf8("qwtPlot_15"))
        self.qwtPlot_10 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_10.setEnabled(False)
        self.qwtPlot_10.setGeometry(QtCore.QRect(180, 190, 181, 171))
        self.qwtPlot_10.setObjectName(_fromUtf8("qwtPlot_10"))
        self.qwtPlot_18 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_18.setEnabled(False)
        self.qwtPlot_18.setGeometry(QtCore.QRect(180, 360, 181, 171))
        self.qwtPlot_18.setObjectName(_fromUtf8("qwtPlot_18"))
        self.qwtPlot_1 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_1.setEnabled(False)
        self.qwtPlot_1.setGeometry(QtCore.QRect(0, 20, 181, 171))
        self.qwtPlot_1.setObjectName(_fromUtf8("qwtPlot_1"))
        self.qwtPlot_11 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_11.setEnabled(False)
        self.qwtPlot_11.setGeometry(QtCore.QRect(360, 190, 181, 171))
        self.qwtPlot_11.setObjectName(_fromUtf8("qwtPlot_11"))
        self.qwtPlot_19 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_19.setEnabled(False)
        self.qwtPlot_19.setGeometry(QtCore.QRect(360, 360, 181, 171))
        self.qwtPlot_19.setObjectName(_fromUtf8("qwtPlot_19"))
        self.qwtPlot_12 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_12.setEnabled(False)
        self.qwtPlot_12.setGeometry(QtCore.QRect(540, 190, 181, 171))
        self.qwtPlot_12.setObjectName(_fromUtf8("qwtPlot_12"))
        self.qwtPlot_20 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_20.setEnabled(False)
        self.qwtPlot_20.setGeometry(QtCore.QRect(540, 360, 181, 171))
        self.qwtPlot_20.setObjectName(_fromUtf8("qwtPlot_20"))
        self.qwtPlot_23 = Qwt5.QwtPlot(self.tab_2)
        self.qwtPlot_23.setEnabled(False)
        self.qwtPlot_23.setGeometry(QtCore.QRect(1080, 360, 181, 171))
        self.qwtPlot_23.setObjectName(_fromUtf8("qwtPlot_23"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 770, 86, 80))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.initCalibration_sb = QtGui.QSpinBox(self.layoutWidget)
        self.initCalibration_sb.setMaximum(99999)
        self.initCalibration_sb.setProperty("value", 5000)
        self.initCalibration_sb.setObjectName(_fromUtf8("initCalibration_sb"))
        self.verticalLayout.addWidget(self.initCalibration_sb)
        self.initCalibration_bt = QtGui.QPushButton(self.layoutWidget)
        self.initCalibration_bt.setObjectName(_fromUtf8("initCalibration_bt"))
        self.verticalLayout.addWidget(self.initCalibration_bt)
        self.calibration_bt = QtGui.QPushButton(self.layoutWidget)
        self.calibration_bt.setObjectName(_fromUtf8("calibration_bt"))
        self.verticalLayout.addWidget(self.calibration_bt)
        self.showPlot_bt = QtGui.QPushButton(self.tab_2)
        self.showPlot_bt.setGeometry(QtCore.QRect(460, 780, 171, 61))
        self.showPlot_bt.setObjectName(_fromUtf8("showPlot_bt"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 800, 77, 51))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.binaryPlot_dsb = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.binaryPlot_dsb.setMaximum(1000.0)
        self.binaryPlot_dsb.setObjectName(_fromUtf8("binaryPlot_dsb"))
        self.verticalLayout_2.addWidget(self.binaryPlot_dsb)
        self.binaryPlot_bt = QtGui.QPushButton(self.layoutWidget1)
        self.binaryPlot_bt.setObjectName(_fromUtf8("binaryPlot_bt"))
        self.verticalLayout_2.addWidget(self.binaryPlot_bt)
        self.layoutWidget2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(220, 800, 77, 51))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frames_sb = QtGui.QSpinBox(self.layoutWidget2)
        self.frames_sb.setMaximum(9999999)
        self.frames_sb.setProperty("value", 32)
        self.frames_sb.setObjectName(_fromUtf8("frames_sb"))
        self.verticalLayout_3.addWidget(self.frames_sb)
        self.record_bt = QtGui.QPushButton(self.layoutWidget2)
        self.record_bt.setObjectName(_fromUtf8("record_bt"))
        self.verticalLayout_3.addWidget(self.record_bt)
        self.layoutWidget3 = QtGui.QWidget(self.tab_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(310, 770, 123, 74))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.skipFrames_lb = QtGui.QLabel(self.layoutWidget3)
        self.skipFrames_lb.setObjectName(_fromUtf8("skipFrames_lb"))
        self.verticalLayout_4.addWidget(self.skipFrames_lb)
        self.skipFrames_sb = QtGui.QSpinBox(self.layoutWidget3)
        self.skipFrames_sb.setMaximum(2048)
        self.skipFrames_sb.setSingleStep(32)
        self.skipFrames_sb.setObjectName(_fromUtf8("skipFrames_sb"))
        self.verticalLayout_4.addWidget(self.skipFrames_sb)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.showAnyX_lb = QtGui.QLabel(self.layoutWidget3)
        self.showAnyX_lb.setObjectName(_fromUtf8("showAnyX_lb"))
        self.verticalLayout_5.addWidget(self.showAnyX_lb)
        self.showAnyX_sb = QtGui.QSpinBox(self.layoutWidget3)
        self.showAnyX_sb.setMinimum(1)
        self.showAnyX_sb.setMaximum(2048)
        self.showAnyX_sb.setProperty("value", 1)
        self.showAnyX_sb.setObjectName(_fromUtf8("showAnyX_sb"))
        self.verticalLayout_5.addWidget(self.showAnyX_sb)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.showRecord_bt = QtGui.QPushButton(self.layoutWidget3)
        self.showRecord_bt.setObjectName(_fromUtf8("showRecord_bt"))
        self.verticalLayout_6.addWidget(self.showRecord_bt)
        self.openFile_bt = QtGui.QPushButton(self.tab_2)
        self.openFile_bt.setGeometry(QtCore.QRect(680, 720, 121, 51))
        self.openFile_bt.setObjectName(_fromUtf8("openFile_bt"))
        self.loadLearnArray_bt = QtGui.QPushButton(self.tab_2)
        self.loadLearnArray_bt.setGeometry(QtCore.QRect(680, 810, 121, 31))
        self.loadLearnArray_bt.setObjectName(_fromUtf8("loadLearnArray_bt"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(680, 770, 121, 43))
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
        self.skipFramesLA_sb.setMaximum(2048)
        self.skipFramesLA_sb.setSingleStep(1)
        self.skipFramesLA_sb.setObjectName(_fromUtf8("skipFramesLA_sb"))
        self.verticalLayout_7.addWidget(self.skipFramesLA_sb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.arrayIdxLF_lb = QtGui.QLabel(self.layoutWidget_2)
        self.arrayIdxLF_lb.setObjectName(_fromUtf8("arrayIdxLF_lb"))
        self.verticalLayout_8.addWidget(self.arrayIdxLF_lb)
        self.arrayIdxLF_sb = QtGui.QSpinBox(self.layoutWidget_2)
        self.arrayIdxLF_sb.setMinimum(1)
        self.arrayIdxLF_sb.setMaximum(2048)
        self.arrayIdxLF_sb.setProperty("value", 1)
        self.arrayIdxLF_sb.setObjectName(_fromUtf8("arrayIdxLF_sb"))
        self.verticalLayout_8.addWidget(self.arrayIdxLF_sb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.calibration_pb = QtGui.QProgressBar(self.tab_2)
        self.calibration_pb.setGeometry(QtCore.QRect(50, 740, 101, 23))
        self.calibration_pb.setProperty("value", 0)
        self.calibration_pb.setObjectName(_fromUtf8("calibration_pb"))
        self.records_pb = QtGui.QProgressBar(self.tab_2)
        self.records_pb.setGeometry(QtCore.QRect(220, 770, 81, 23))
        self.records_pb.setProperty("value", 0)
        self.records_pb.setObjectName(_fromUtf8("records_pb"))
        self.initKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.initKMeans_bt.setGeometry(QtCore.QRect(830, 760, 91, 23))
        self.initKMeans_bt.setObjectName(_fromUtf8("initKMeans_bt"))
        self.learnKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.learnKMeans_bt.setGeometry(QtCore.QRect(830, 790, 91, 23))
        self.learnKMeans_bt.setObjectName(_fromUtf8("learnKMeans_bt"))
        self.checkKMeans_bt = QtGui.QPushButton(self.tab_2)
        self.checkKMeans_bt.setGeometry(QtCore.QRect(830, 820, 91, 23))
        self.checkKMeans_bt.setObjectName(_fromUtf8("checkKMeans_bt"))
        self.class1_bt = QtGui.QPushButton(self.tab_2)
        self.class1_bt.setGeometry(QtCore.QRect(950, 710, 81, 23))
        self.class1_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class1_bt.setObjectName(_fromUtf8("class1_bt"))
        self.kNumber_sb = QtGui.QSpinBox(self.tab_2)
        self.kNumber_sb.setGeometry(QtCore.QRect(860, 710, 61, 22))
        self.kNumber_sb.setObjectName(_fromUtf8("kNumber_sb"))
        self.k_lb = QtGui.QLabel(self.tab_2)
        self.k_lb.setGeometry(QtCore.QRect(830, 710, 21, 21))
        self.k_lb.setObjectName(_fromUtf8("k_lb"))
        self.maxIteration_sb = QtGui.QSpinBox(self.tab_2)
        self.maxIteration_sb.setGeometry(QtCore.QRect(860, 730, 61, 22))
        self.maxIteration_sb.setObjectName(_fromUtf8("maxIteration_sb"))
        self.k_lb_2 = QtGui.QLabel(self.tab_2)
        self.k_lb_2.setGeometry(QtCore.QRect(830, 730, 31, 21))
        self.k_lb_2.setObjectName(_fromUtf8("k_lb_2"))
        self.class2_bt = QtGui.QPushButton(self.tab_2)
        self.class2_bt.setGeometry(QtCore.QRect(950, 740, 81, 23))
        self.class2_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class2_bt.setObjectName(_fromUtf8("class2_bt"))
        self.class3_bt = QtGui.QPushButton(self.tab_2)
        self.class3_bt.setGeometry(QtCore.QRect(950, 770, 81, 23))
        self.class3_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class3_bt.setObjectName(_fromUtf8("class3_bt"))
        self.class4_bt = QtGui.QPushButton(self.tab_2)
        self.class4_bt.setGeometry(QtCore.QRect(950, 800, 81, 23))
        self.class4_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class4_bt.setObjectName(_fromUtf8("class4_bt"))
        self.class5_bt = QtGui.QPushButton(self.tab_2)
        self.class5_bt.setGeometry(QtCore.QRect(950, 830, 81, 23))
        self.class5_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class5_bt.setObjectName(_fromUtf8("class5_bt"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1506, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.initCalibration_bt.setText(_translate("MainWindow", "initial calibration", None))
        self.calibration_bt.setText(_translate("MainWindow", "calibrate", None))
        self.showPlot_bt.setText(_translate("MainWindow", "show plot", None))
        self.binaryPlot_bt.setText(_translate("MainWindow", "binary plot", None))
        self.record_bt.setText(_translate("MainWindow", "record frames", None))
        self.skipFrames_lb.setText(_translate("MainWindow", "skip frames", None))
        self.showAnyX_lb.setText(_translate("MainWindow", "show any x", None))
        self.showRecord_bt.setText(_translate("MainWindow", "show record", None))
        self.openFile_bt.setText(_translate("MainWindow", "open file", None))
        self.loadLearnArray_bt.setText(_translate("MainWindow", "load array", None))
        self.skipFramesLA_lb.setText(_translate("MainWindow", "skip frames", None))
        self.arrayIdxLF_lb.setText(_translate("MainWindow", "array idx", None))
        self.initKMeans_bt.setText(_translate("MainWindow", "init k-means", None))
        self.learnKMeans_bt.setText(_translate("MainWindow", "learn k-means", None))
        self.checkKMeans_bt.setText(_translate("MainWindow", "check k-means", None))
        self.class1_bt.setText(_translate("MainWindow", "Class 1", None))
        self.k_lb.setText(_translate("MainWindow", "k", None))
        self.k_lb_2.setText(_translate("MainWindow", "max it", None))
        self.class2_bt.setText(_translate("MainWindow", "Class 2", None))
        self.class3_bt.setText(_translate("MainWindow", "Class 3", None))
        self.class4_bt.setText(_translate("MainWindow", "Class 4", None))
        self.class5_bt.setText(_translate("MainWindow", "Class 5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))

from PyQt4 import Qwt5