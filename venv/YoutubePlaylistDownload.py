# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venv\YoutubePlaylistDownload.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject,pyqtSlot

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 859)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(150, 30))
        self.label.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dir_text = QtWidgets.QLineEdit(self.centralwidget)
        self.dir_text.setObjectName("dir_text")
        self.horizontalLayout.addWidget(self.dir_text)
        self.browse_Button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_Button.setObjectName("browse_Button")
        self.horizontalLayout.addWidget(self.browse_Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.url_text = QtWidgets.QLineEdit(self.centralwidget)
        self.url_text.setObjectName("url_text")
        self.horizontalLayout_2.addWidget(self.url_text)
        self.resolve_Button = QtWidgets.QPushButton(self.centralwidget)
        self.resolve_Button.setObjectName("resolve_Button")
        self.horizontalLayout_2.addWidget(self.resolve_Button)
        self.download_Button = QtWidgets.QPushButton(self.centralwidget)
        self.download_Button.setObjectName("download_Button")
        self.horizontalLayout_2.addWidget(self.download_Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setMinimumSize(QtCore.QSize(0, 600))
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.browse_Button.clicked.connect(self.browse_slot)
        self.dir_text.returnPressed.connect(self.dir_pressed_return_slot)
        self.url_text.returnPressed.connect(self.url_return_pressed_slot)
        self.resolve_Button.clicked.connect(self.resolve_playlist_slot)
        self.download_Button.clicked.connect(self.download_subs_slot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Playlist Subtitles Download"))
        self.label.setText(_translate("MainWindow", "选择目录(默认当前目录):"))
        self.browse_Button.setText(_translate("MainWindow", "游览"))
        self.label_2.setText(_translate("MainWindow", "粘贴 playlist url:"))
        self.resolve_Button.setText(_translate("MainWindow", "解析"))
        self.download_Button.setText(_translate("MainWindow", "下载"))
        self.label_3.setText(_translate("MainWindow", "日志:"))

    @pyqtSlot()
    def browse_slot(self):
        pass

    @pyqtSlot()
    def dir_pressed_return_slot(self):
        pass

    @pyqtSlot()
    def url_return_pressed_slot(self):
        pass

    @pyqtSlot()
    def resolve_playlist_slot(self):
        pass

    @pyqtSlot()
    def download_subs_slot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
