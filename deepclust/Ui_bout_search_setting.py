# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ezequiel/repos/deepclust/deepclust/bout_search_setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bout_detect_form(object):
    def setupUi(self, bout_detect_form):
        bout_detect_form.setObjectName("bout_detect_form")
        bout_detect_form.resize(1103, 847)
        self.gridLayout = QtWidgets.QGridLayout(bout_detect_form)
        self.gridLayout.setObjectName("gridLayout")
        self.line_in_plot_span = QtWidgets.QLineEdit(bout_detect_form)
        self.line_in_plot_span.setObjectName("line_in_plot_span")
        self.gridLayout.addWidget(self.line_in_plot_span, 14, 5, 1, 1)
        self.plot_bar = QtWidgets.QScrollBar(bout_detect_form)
        self.plot_bar.setMouseTracking(False)
        self.plot_bar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.plot_bar.setOrientation(QtCore.Qt.Horizontal)
        self.plot_bar.setObjectName("plot_bar")
        self.gridLayout.addWidget(self.plot_bar, 11, 1, 1, 5)
        self.label = QtWidgets.QLabel(bout_detect_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.select_bird = QtWidgets.QComboBox(bout_detect_form)
        self.select_bird.setObjectName("select_bird")
        self.gridLayout.addWidget(self.select_bird, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(bout_detect_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.select_file = QtWidgets.QComboBox(bout_detect_form)
        self.select_file.setObjectName("select_file")
        self.gridLayout.addWidget(self.select_file, 5, 0, 1, 1)
        self.select_sess = QtWidgets.QComboBox(bout_detect_form)
        self.select_sess.setObjectName("select_sess")
        self.gridLayout.addWidget(self.select_sess, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(bout_detect_form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.label_start = QtWidgets.QLabel(bout_detect_form)
        self.label_start.setObjectName("label_start")
        self.gridLayout.addWidget(self.label_start, 14, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 14, 3, 1, 1)
        self.dockWidget = QtWidgets.QDockWidget(bout_detect_form)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = CustomWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.gridLayout.addWidget(self.dockWidget, 7, 1, 1, 5)
        self.label_span = QtWidgets.QLabel(bout_detect_form)
        self.label_span.setObjectName("label_span")
        self.gridLayout.addWidget(self.label_span, 14, 4, 1, 1)
        self.line_in_plot_start = QtWidgets.QLineEdit(bout_detect_form)
        self.line_in_plot_start.setObjectName("line_in_plot_start")
        self.gridLayout.addWidget(self.line_in_plot_start, 14, 2, 1, 1)

        self.retranslateUi(bout_detect_form)
        QtCore.QMetaObject.connectSlotsByName(bout_detect_form)

    def retranslateUi(self, bout_detect_form):
        _translate = QtCore.QCoreApplication.translate
        bout_detect_form.setWindowTitle(_translate("bout_detect_form", "Form"))
        self.line_in_plot_span.setToolTip(_translate("bout_detect_form", "span of plot in ms"))
        self.label.setText(_translate("bout_detect_form", "Bird"))
        self.select_bird.setToolTip(_translate("bout_detect_form", "Select Bird"))
        self.label_2.setText(_translate("bout_detect_form", "Sess"))
        self.select_file.setToolTip(_translate("bout_detect_form", "Select example file"))
        self.select_sess.setToolTip(_translate("bout_detect_form", "<html><head/><body><p>Select session</p></body></html>"))
        self.label_3.setText(_translate("bout_detect_form", "File"))
        self.label_start.setText(_translate("bout_detect_form", "start"))
        self.label_span.setText(_translate("bout_detect_form", "span"))
        self.line_in_plot_start.setToolTip(_translate("bout_detect_form", "start (ms)"))

from graph import CustomWidget
