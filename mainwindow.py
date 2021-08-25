from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Image_box import ImageBox
from diag import Ui_dialog_3


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Image_box import ImageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        # 使窗口在屏幕中间
        desktop = QtWidgets.QApplication.desktop()
        MainWindow.resize(1200, 800)
        MainWindow.move((desktop.width()-MainWindow.width())/2, (desktop.height()-MainWindow.height())/2)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # 布局上方四个空白位置 可伸缩
        spacerItem = QtWidgets.QSpacerItem(450, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        # 左上角框
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, self.scrollArea.width(), self.scrollArea.height()))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        # 左下角框
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, self.scrollArea_2.width(), self.scrollArea_2.height()))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        #右侧大框
        # self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea_3.setWidgetResizable(True)
        # self.scrollArea_3.setObjectName("scrollArea_3")
        # self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 815, 556))
        # self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        # self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        # self.gridLayout.addWidget(self.scrollArea_3, 1, 1, 2, 3)

        self.scrollArea_3 = ImageBox()
        self.gridLayout.addWidget(self.scrollArea_3, 1, 1, 2, 3)


        MainWindow.setCentralWidget(self.centralwidget)
        # set MenuBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 20))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuDEMO = QtWidgets.QMenu(self.menubar)
        self.menuDEMO.setObjectName("menuDEMO")
        self.menuFunction = QtWidgets.QMenu(self.menubar)
        self.menuFunction.setObjectName("menuFunction")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        # set StatusBar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # set ToolBar
        self.loadimage = QtWidgets.QToolBar(MainWindow)
        self.loadimage.setObjectName("loadimage")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.loadimage)
        # add Action
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.action_linemeasurement = QtWidgets.QAction(MainWindow)
        self.action_linemeasurement.setObjectName("action_linemeasurement")
        self.action_cyrvemeasurement = QtWidgets.QAction(MainWindow)
        self.action_cyrvemeasurement.setObjectName("action_cyrvemeasurement")
        self.actionQuick_Start = QtWidgets.QAction(MainWindow)
        self.actionQuick_Start.setObjectName("actionQuick_Start")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.action_saveas = QtWidgets.QAction(MainWindow)
        self.action_saveas.setObjectName("action_saveas")
        self.action_planemeasurement = QtWidgets.QAction(MainWindow)
        self.action_planemeasurement.setObjectName("action_planemeasurement")
        self.action_automeasurement = QtWidgets.QAction(MainWindow)
        self.action_automeasurement.setObjectName("action_automeasurement")
        self.actionAdaptive_Gaussian_filtering = QtWidgets.QAction(MainWindow)
        self.actionAdaptive_Gaussian_filtering.setObjectName("actionAdaptive_Gaussian_filtering")
        self.actionNon_local_mean_filtering = QtWidgets.QAction(MainWindow)
        self.actionNon_local_mean_filtering.setObjectName("actionNon_local_mean_filtering")
        self.actionComponent_area_detection_and_recognition = QtWidgets.QAction(MainWindow)
        self.actionComponent_area_detection_and_recognition.setObjectName("actionComponent_area_detection_and_recognition")
        self.actionThreshold_segmentation = QtWidgets.QAction(MainWindow)
        self.actionThreshold_segmentation.setObjectName("actionThreshold_segmentation")
        self.actionU_net_segmentation = QtWidgets.QAction(MainWindow)
        self.actionU_net_segmentation.setObjectName("actionU_net_segmentation")
        self.actionGan_segmentation = QtWidgets.QAction(MainWindow)
        self.actionGan_segmentation.setObjectName("actionGan_segmentation")
        # 设置图标
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/zoom_in.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/zoom_out.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon1)
        self.actionZoom_out.setObjectName("actionZoom_out")

        self.actionOriginalimage = QtWidgets.QAction(MainWindow)
        self.actionOriginalimage.setObjectName("actionOriginalimage")
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionloadimage = QtWidgets.QAction(MainWindow)
        self.actionloadimage.setObjectName("actionloadimage")
        # 设置边框的下拉功能
        self.menuDEMO.addAction(self.actionloadimage)
        self.menuDEMO.addSeparator()   # 这是个分割线
        self.menuDEMO.addAction(self.actionOpen_Folder)
        self.menuDEMO.addSeparator()
        self.menuDEMO.addAction(self.actionSave)
        self.menuDEMO.addSeparator()
        self.menuDEMO.addAction(self.action_saveas)
        self.menuDEMO.addSeparator()
        self.menuFunction.addSeparator()
        self.menuFunction.addAction(self.actionAdaptive_Gaussian_filtering)
        self.menuFunction.addSeparator()
        self.menuFunction.addAction(self.actionNon_local_mean_filtering)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.action_linemeasurement)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.action_cyrvemeasurement)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.action_planemeasurement)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.action_automeasurement)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionComponent_area_detection_and_recognition)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionThreshold_segmentation)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionU_net_segmentation)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionGan_segmentation)
        self.menuHelp.addAction(self.actionQuick_Start)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        # 将功能都加入到menubar中
        self.menubar.addAction(self.menuDEMO.menuAction())
        self.menubar.addAction(self.menuFunction.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        # 将下边第二栏中的功能都加入到loadimage中
        self.loadimage.addAction(self.actionloadimage)
        self.loadimage.addSeparator()
        self.loadimage.addAction(self.actionOpen_Folder)
        self.loadimage.addSeparator()
        self.loadimage.addAction(self.actionSave)
        self.loadimage.addSeparator()
        self.loadimage.addAction(self.actionOriginalimage)
        self.loadimage.addSeparator()
        self.loadimage.addAction(self.actionZoom_out)
        self.loadimage.addSeparator()
        self.loadimage.addAction(self.actionZoom_in)
        self.loadimage.addSeparator()

        # diag弹窗测试
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget.setObjectName("widget")


        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem_1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem_1, 0, 0, 1, 1)
        spacerItem_2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem_2, 0, 1, 1, 1)
        spacerItem_3 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem_3, 0, 2, 1, 1)
        spacerItem_4 = QtWidgets.QSpacerItem(60, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem_4, 1, 0, 1, 1)
        spacerItem_5 = QtWidgets.QSpacerItem(60, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem_5, 2, 0, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.gridLayout_2.addItem(self.verticalLayout, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 1)
        self.pushButton.setObjectName("pushButton")

        self.widget.close()
        #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionconnect()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuDEMO.setTitle(_translate("MainWindow", "Open"))
        self.menuFunction.setTitle(_translate("MainWindow", "Image Filtering"))
        self.menuWindow.setTitle(_translate("MainWindow", "Attribute measurement"))
        self.menuView.setTitle(_translate("MainWindow", "Defect detection"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.loadimage.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_linemeasurement.setText(_translate("MainWindow", "Straight line measurement"))
        self.action_cyrvemeasurement.setText(_translate("MainWindow", "Curve measurement"))
        self.actionQuick_Start.setText(_translate("MainWindow", "Quick Start"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.action_saveas.setText(_translate("MainWindow", "Save As"))
        self.action_planemeasurement.setText(_translate("MainWindow", "Plane measurement"))
        self.action_automeasurement.setText(_translate("MainWindow", "Auto measurement"))
        self.actionAdaptive_Gaussian_filtering.setText(_translate("MainWindow", "Adaptive Gaussian filtering"))
        self.actionNon_local_mean_filtering.setText(_translate("MainWindow", "Non-local mean filtering"))
        self.actionComponent_area_detection_and_recognition.setText(_translate("MainWindow", "Component area detection and recognition"))
        self.actionThreshold_segmentation.setText(_translate("MainWindow", "Threshold segmentation"))
        self.actionU_net_segmentation.setText(_translate("MainWindow", "U-net segmentation"))
        self.actionGan_segmentation.setText(_translate("MainWindow", "Gan segmentation"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom_out"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom_in"))
        self.actionOriginalimage.setText(_translate("MainWindow", "Original image"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Import Folder"))
        self.actionOpen_Folder.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionloadimage.setText(_translate("MainWindow", "Import Image"))
        self.actionloadimage.setShortcut(_translate("MainWindow", "Ctrl+O"))

        self.pushButton.setText(_translate("MainWindow", "应用"))
        self.pushButton_1.setText(_translate("dialog_2", "model1（应用于SIC）"))
        self.pushButton_2.setText(_translate("dialog_2", "model2（应用于其他）"))
    def actionconnect(self):
        self.actionloadimage.triggered.connect(self.openfile)  # 返回原始图片的路径
        self.actionOpen_Folder.triggered.connect(self.get_folder)  # 获得要输入的文件夹路径
        self.action_saveas.triggered.connect(self.saveAs)  # 保存文件
        self.actionZoom_out.triggered.connect(self.large_click)  # 放大box
        self.actionZoom_in.triggered.connect(self.small_click)  # 缩小box

        self.actionNon_local_mean_filtering.triggered.connect(self.show_diag)
        self.pushButton.clicked.connect(self.submit)  # 关联槽submit

    def openfile(self):
        fname = QFileDialog.getOpenFileName(None, "Open File", "./", "All (*.*)")
        # 打开文件 返回一个字符串第一个是路径， 第二个是要打开文件的类型
        # 如果用户主动关闭文件对话框，则返回值为空

        # input_image = QtGui.QPixmap(fname[0])
        # self.scrollArea.set_image(input_image)
        self.image = QtGui.QPixmap(fname[0])
        self.scrollArea_3.set_image(self.image)
        self.scrollArea_3.update()

    def get_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.file_folder = directory

    def display(self):
        self.scrollArea_3.set_image(self.image)
        self.scrollArea_3.update()

    def saveAs(self):
        path, _ = QFileDialog.getSaveFileName(None, 'Save As', "./", "Image Files(*.jpg *.png *.bmp)")
        if not path:
            return
        img = QPixmap(self.image)
        img.save(path)

    def large_click(self):
        """
        used to enlarge image
        :return:
        """
        if self.scrollArea_3.scale < 2:
            self.scrollArea_3.scale += 0.01
            self.scrollArea_3.adjustSize()
        self.scrollArea_3.update()

    def small_click(self):
        """
        used to reduce image
        :return:
        """
        if self.scrollArea_3.scale > 0.1:
            self.scrollArea_3.scale -= 0.01
            self.scrollArea_3.adjustSize()
        self.scrollArea_3.update()

    def show_diag(self):
        self.widget.show()

    def submit(self):
        self.widget.close()