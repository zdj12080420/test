# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'celan.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore,  QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(687, 761)
        self.checkBox = QtWidgets.QCheckBox(Form)             # 设置隐藏选项按钮
        self.checkBox.setGeometry(QtCore.QRect(560, 10, 91, 19))
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(430, 40, 256, 681))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(430, 210, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(560, 210, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)             # 孔隙率展示框组件
        self.label_3.setGeometry(QtCore.QRect(480, 210, 72, 15))
        self.label_3.setStyleSheet("border-width: 2px;\n"
        "\n"
        "border-style: solid;\n"
        "\n"
        "border-color: rgb(3, 3, 3);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)             # 数量展示组件
        self.label_4.setGeometry(QtCore.QRect(590, 210, 72, 15))
        self.label_4.setStyleSheet("border-width: 2px;\n"
        "\n"
        "border-style: solid;\n"
        "\n"
        "border-color: rgb(3, 3, 3);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(440, 50, 231, 141))
        self.label_5.setStyleSheet("border-width: 1px;\n"
        "\n"
        "border-style: dashed;\n"
        "\n"
        "border-color: rgb(3, 3, 3);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(440, 240, 231, 141))
        self.label_6.setStyleSheet("border-width: 1px;\n"
        "\n"
        "border-style: dashed;\n"
        "\n"
        "border-color: rgb(3, 3, 3);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(440, 390, 231, 141))
        self.label_7.setStyleSheet("border-width: 1px;\n"
        "\n"
        "border-style: dashed;\n"
        "\n"
        "border-color: rgb(3, 3, 3);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(440, 540, 231, 141))
        self.label_8.setStyleSheet("border-width: 1px;\n"
        "\n"
        "border-style: dashed;\n"
        "\n"
        "border-color: rgb(3, 3, 3);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        self.checkBox.clicked['bool'].connect(self.listView.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_5.setVisible)
        self.checkBox.clicked['bool'].connect(self.label.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_3.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_2.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_4.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_6.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_7.setVisible)
        self.checkBox.clicked['bool'].connect(self.label_8.setVisible)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "显示/隐藏"))
        self.label.setText(_translate("Form", "孔隙率"))
        self.label_2.setText(_translate("Form", "数量"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())