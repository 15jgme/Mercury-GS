# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'platform-comms-app.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(670, 443)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTelecommanding = QtWidgets.QWidget()
        self.tabTelecommanding.setObjectName("tabTelecommanding")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabTelecommanding)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabTelecommanding)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 251))
        self.groupBox_4.setMaximumSize(QtCore.QSize(999999, 16777215))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.formLayoutTLMCH = QtWidgets.QFormLayout()
        self.formLayoutTLMCH.setObjectName("formLayoutTLMCH")
        self.labelTlmChOne = QtWidgets.QLabel(self.groupBox_4)
        self.labelTlmChOne.setObjectName("labelTlmChOne")
        self.formLayoutTLMCH.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTlmChOne)
        self.labelTlmChOneValue = QtWidgets.QLabel(self.groupBox_4)
        self.labelTlmChOneValue.setObjectName("labelTlmChOneValue")
        self.formLayoutTLMCH.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTlmChOneValue)
        self.labelTlmChTwo = QtWidgets.QLabel(self.groupBox_4)
        self.labelTlmChTwo.setObjectName("labelTlmChTwo")
        self.formLayoutTLMCH.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelTlmChTwo)
        self.labelTlmChThree = QtWidgets.QLabel(self.groupBox_4)
        self.labelTlmChThree.setObjectName("labelTlmChThree")
        self.formLayoutTLMCH.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelTlmChThree)
        self.labelTlmChTwoValue = QtWidgets.QLabel(self.groupBox_4)
        self.labelTlmChTwoValue.setObjectName("labelTlmChTwoValue")
        self.formLayoutTLMCH.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelTlmChTwoValue)
        self.labelTlmChThreeValue = QtWidgets.QLabel(self.groupBox_4)
        self.labelTlmChThreeValue.setObjectName("labelTlmChThreeValue")
        self.formLayoutTLMCH.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelTlmChThreeValue)
        self.verticalLayout_5.addLayout(self.formLayoutTLMCH)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 1, 1, 1)
        self.pushButtonSendTlmReq = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButtonSendTlmReq.setObjectName("pushButtonSendTlmReq")
        self.gridLayout_6.addWidget(self.pushButtonSendTlmReq, 0, 0, 1, 1)
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.labelTimeOuts = QtWidgets.QLabel(self.groupBox_6)
        self.labelTimeOuts.setObjectName("labelTimeOuts")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelTimeOuts)
        self.labelTLMTimeouts = QtWidgets.QLabel(self.groupBox_6)
        self.labelTLMTimeouts.setObjectName("labelTLMTimeouts")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTLMTimeouts)
        self.gridLayout_6.addLayout(self.formLayout_10, 0, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 5, 1, 1)
        self.lineEditChannel = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEditChannel.setObjectName("lineEditChannel")
        self.gridLayout_6.addWidget(self.lineEditChannel, 0, 2, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.labelTlmErrChannel = QtWidgets.QLabel(self.groupBox_9)
        self.labelTlmErrChannel.setGeometry(QtCore.QRect(90, 40, 60, 16))
        self.labelTlmErrChannel.setObjectName("labelTlmErrChannel")
        self.label_6 = QtWidgets.QLabel(self.groupBox_9)
        self.label_6.setGeometry(QtCore.QRect(180, 40, 60, 16))
        self.label_6.setObjectName("label_6")
        self.labelTlmErrReason = QtWidgets.QLabel(self.groupBox_9)
        self.labelTlmErrReason.setGeometry(QtCore.QRect(230, 40, 60, 16))
        self.labelTlmErrReason.setObjectName("labelTlmErrReason")
        self.gridLayout_6.addWidget(self.groupBox_9, 5, 1, 2, 6)
        self.checkBoxLastReqContinuous = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBoxLastReqContinuous.setObjectName("checkBoxLastReqContinuous")
        self.gridLayout_6.addWidget(self.checkBoxLastReqContinuous, 5, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tabTelecommanding, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 251))
        self.groupBox.setMaximumSize(QtCore.QSize(999999, 16777215))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblTelecommandN = QtWidgets.QLabel(self.groupBox)
        self.lblTelecommandN.setObjectName("lblTelecommandN")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandN)
        self.inputTelecommandN = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTelecommandN.sizePolicy().hasHeightForWidth())
        self.inputTelecommandN.setSizePolicy(sizePolicy)
        self.inputTelecommandN.setObjectName("inputTelecommandN")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandN)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.pushButtonSendTCReq = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSendTCReq.setObjectName("pushButtonSendTCReq")
        self.gridLayout_3.addWidget(self.pushButtonSendTCReq, 5, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonSendPcTime = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonSendPcTime.setGeometry(QtCore.QRect(9, 29, 128, 32))
        self.pushButtonSendPcTime.setObjectName("pushButtonSendPcTime")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 377, 38))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonSendThisTime = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSendThisTime.setObjectName("pushButtonSendThisTime")
        self.horizontalLayout_4.addWidget(self.pushButtonSendThisTime)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateEditSendThisTime = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEditSendThisTime.setObjectName("dateEditSendThisTime")
        self.horizontalLayout_2.addWidget(self.dateEditSendThisTime, 0, QtCore.Qt.AlignLeft)
        self.dateTimeEditSendThisTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEditSendThisTime.setObjectName("dateTimeEditSendThisTime")
        self.horizontalLayout_2.addWidget(self.dateTimeEditSendThisTime)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayoutTCN = QtWidgets.QFormLayout()
        self.formLayoutTCN.setObjectName("formLayoutTCN")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayoutTCN.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelTCRes = QtWidgets.QLabel(self.groupBox_3)
        self.labelTCRes.setObjectName("labelTCRes")
        self.formLayoutTCN.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTCRes)
        self.gridLayout_5.addLayout(self.formLayoutTCN, 0, 0, 1, 1)
        self.formLayoutTimeOuts = QtWidgets.QFormLayout()
        self.formLayoutTimeOuts.setObjectName("formLayoutTimeOuts")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayoutTimeOuts.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.labelTCResTimeouts = QtWidgets.QLabel(self.groupBox_3)
        self.labelTCResTimeouts.setObjectName("labelTCResTimeouts")
        self.formLayoutTimeOuts.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTCResTimeouts)
        self.gridLayout_5.addLayout(self.formLayoutTimeOuts, 0, 1, 1, 1)
        self.formLayoutResponse = QtWidgets.QFormLayout()
        self.formLayoutResponse.setObjectName("formLayoutResponse")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayoutResponse.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.labelTCResStatus = QtWidgets.QLabel(self.groupBox_3)
        self.labelTCResStatus.setObjectName("labelTCResStatus")
        self.formLayoutResponse.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelTCResStatus)
        self.gridLayout_5.addLayout(self.formLayoutResponse, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 6, 0, 1, 3)
        self.checkBoxTelemetryContinuous = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxTelemetryContinuous.setObjectName("checkBoxTelemetryContinuous")
        self.gridLayout_3.addWidget(self.checkBoxTelemetryContinuous, 1, 1, 1, 1)
        self.comboBoxTelemetry = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxTelemetry.setObjectName("comboBoxTelemetry")
        self.gridLayout_3.addWidget(self.comboBoxTelemetry, 0, 2, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblTelecommandData = QtWidgets.QLabel(self.groupBox)
        self.lblTelecommandData.setObjectName("lblTelecommandData")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandData)
        self.inputTelecommandData = QtWidgets.QLineEdit(self.groupBox)
        self.inputTelecommandData.setObjectName("inputTelecommandData")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandData)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 251))
        self.groupBox_5.setMaximumSize(QtCore.QSize(999999, 16777215))
        self.groupBox_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_12 = QtWidgets.QFormLayout()
        self.formLayout_12.setObjectName("formLayout_12")
        self.lblTelecommandData_2 = QtWidgets.QLabel(self.groupBox_5)
        self.lblTelecommandData_2.setObjectName("lblTelecommandData_2")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandData_2)
        self.inputTelecommandDataUploadFrom = QtWidgets.QLineEdit(self.groupBox_5)
        self.inputTelecommandDataUploadFrom.setObjectName("inputTelecommandDataUploadFrom")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandDataUploadFrom)
        self.gridLayout_4.addLayout(self.formLayout_12, 1, 0, 1, 1)
        self.pushButtonUploadSendTcReq = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButtonUploadSendTcReq.setObjectName("pushButtonUploadSendTcReq")
        self.gridLayout_4.addWidget(self.pushButtonUploadSendTcReq, 5, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.lblTelecommandN_2 = QtWidgets.QLabel(self.groupBox_5)
        self.lblTelecommandN_2.setObjectName("lblTelecommandN_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandN_2)
        self.inputTelecommandNUploadTo = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTelecommandNUploadTo.sizePolicy().hasHeightForWidth())
        self.inputTelecommandNUploadTo.setSizePolicy(sizePolicy)
        self.inputTelecommandNUploadTo.setObjectName("inputTelecommandNUploadTo")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandNUploadTo)
        self.gridLayout_4.addLayout(self.formLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_6.setGeometry(QtCore.QRect(9, 29, 128, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 60, 377, 38))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_3.addWidget(self.dateEdit_2, 0, QtCore.Qt.AlignLeft)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.layoutWidget_2)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.formLayoutUploadTC = QtWidgets.QFormLayout()
        self.formLayoutUploadTC.setObjectName("formLayoutUploadTC")
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.formLayoutUploadTC.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setObjectName("label_11")
        self.formLayoutUploadTC.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.gridLayout_7.addLayout(self.formLayoutUploadTC, 0, 0, 1, 1)
        self.formLayoutUploadTimeOuts = QtWidgets.QFormLayout()
        self.formLayoutUploadTimeOuts.setObjectName("formLayoutUploadTimeOuts")
        self.label_12 = QtWidgets.QLabel(self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.formLayoutUploadTimeOuts.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_15 = QtWidgets.QLabel(self.groupBox_8)
        self.label_15.setObjectName("label_15")
        self.formLayoutUploadTimeOuts.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_15)
        self.gridLayout_7.addLayout(self.formLayoutUploadTimeOuts, 0, 1, 1, 1)
        self.formLayoutUploadRes = QtWidgets.QFormLayout()
        self.formLayoutUploadRes.setObjectName("formLayoutUploadRes")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setObjectName("label_16")
        self.formLayoutUploadRes.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_8)
        self.label_17.setObjectName("label_17")
        self.formLayoutUploadRes.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.gridLayout_7.addLayout(self.formLayoutUploadRes, 1, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_8)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 6, 0, 1, 2)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.widget, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 20, 401, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OSSAT Platform Computer Comms"))
        self.groupBox_4.setTitle(_translate("Form", "Telemetry"))
        self.labelTlmChOne.setText(_translate("Form", "TLM CH 1"))
        self.labelTlmChOneValue.setText(_translate("Form", "N/A"))
        self.labelTlmChTwo.setText(_translate("Form", "TLM CH 2"))
        self.labelTlmChThree.setText(_translate("Form", "TLM CH 3"))
        self.labelTlmChTwoValue.setText(_translate("Form", "N/A"))
        self.labelTlmChThreeValue.setText(_translate("Form", "N/A"))
        self.groupBox_6.setTitle(_translate("Form", "Ad-hoc Request"))
        self.label.setText(_translate("Form", "Channel #"))
        self.pushButtonSendTlmReq.setText(_translate("Form", "Send TLM REQ"))
        self.labelTimeOuts.setText(_translate("Form", "TIMEOUTS:"))
        self.labelTLMTimeouts.setText(_translate("Form", "N/A"))
        self.groupBox_9.setTitle(_translate("Form", "Last Failure"))
        self.label_2.setText(_translate("Form", "Channel #"))
        self.labelTlmErrChannel.setText(_translate("Form", "N/A"))
        self.label_6.setText(_translate("Form", "Reason"))
        self.labelTlmErrReason.setText(_translate("Form", "N/A"))
        self.checkBoxLastReqContinuous.setText(_translate("Form", "Continuous?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTelecommanding), _translate("Form", "TELEMETRY"))
        self.groupBox.setTitle(_translate("Form", "Telecommanding"))
        self.lblTelecommandN.setText(_translate("Form", "TC #"))
        self.pushButtonSendTCReq.setText(_translate("Form", "Send TC REQ"))
        self.groupBox_2.setTitle(_translate("Form", "Time Commands"))
        self.pushButtonSendPcTime.setText(_translate("Form", "Send PC Time"))
        self.pushButtonSendThisTime.setText(_translate("Form", "Send this Time :"))
        self.dateTimeEditSendThisTime.setDisplayFormat(_translate("Form", "HH:mm:ss.zzz"))
        self.groupBox_3.setTitle(_translate("Form", "Last Response"))
        self.label_3.setText(_translate("Form", "TC #"))
        self.labelTCRes.setText(_translate("Form", "N"))
        self.label_7.setText(_translate("Form", "TIMEOUTS :"))
        self.labelTCResTimeouts.setText(_translate("Form", "N/A"))
        self.label_5.setText(_translate("Form", "Response"))
        self.labelTCResStatus.setText(_translate("Form", "N/A"))
        self.checkBoxTelemetryContinuous.setText(_translate("Form", "Continuous?"))
        self.lblTelecommandData.setText(_translate("Form", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "TELECOMMANDING"))
        self.groupBox_5.setTitle(_translate("Form", "To Upload"))
        self.lblTelecommandData_2.setText(_translate("Form", "Upload from:"))
        self.pushButtonUploadSendTcReq.setText(_translate("Form", "Send TC REQ"))
        self.lblTelecommandN_2.setText(_translate("Form", "Upload to:"))
        self.groupBox_7.setTitle(_translate("Form", "Time Commands"))
        self.pushButton_6.setText(_translate("Form", "Send PC Time"))
        self.pushButton_7.setText(_translate("Form", "Send this Time :"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("Form", "HH:mm:ss.zzz"))
        self.groupBox_8.setTitle(_translate("Form", "Last Response"))
        self.label_10.setText(_translate("Form", "TC #"))
        self.label_11.setText(_translate("Form", "N"))
        self.label_12.setText(_translate("Form", "TIMEOUTS :"))
        self.label_15.setText(_translate("Form", "N/A"))
        self.label_16.setText(_translate("Form", "Response"))
        self.label_17.setText(_translate("Form", "N/A"))
        self.pushButton_8.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "FILE TRANSFER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "LOG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "CONFIG"))
