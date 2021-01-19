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
        Form.resize(670, 438)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTelemetry = QtWidgets.QWidget()
        self.tabTelemetry.setObjectName("tabTelemetry")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabTelemetry)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tabTelemetry)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 251))
        self.groupBox.setMaximumSize(QtCore.QSize(999999, 16777215))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblTelecommandData = QtWidgets.QLabel(self.groupBox)
        self.lblTelecommandData.setObjectName("lblTelecommandData")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandData)
        self.inputTelecommandData = QtWidgets.QLineEdit(self.groupBox)
        self.inputTelecommandData.setObjectName("inputTelecommandData")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandData)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonSendPcTime = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSendPcTime.sizePolicy().hasHeightForWidth())
        self.pushButtonSendPcTime.setSizePolicy(sizePolicy)
        self.pushButtonSendPcTime.setObjectName("pushButtonSendPcTime")
        self.gridLayout_5.addWidget(self.pushButtonSendPcTime, 0, 0, 1, 1)
        self.pushButtonSendThisTime = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSendThisTime.sizePolicy().hasHeightForWidth())
        self.pushButtonSendThisTime.setSizePolicy(sizePolicy)
        self.pushButtonSendThisTime.setObjectName("pushButtonSendThisTime")
        self.gridLayout_5.addWidget(self.pushButtonSendThisTime, 1, 0, 1, 1)
        self.dateEditSendThisTime = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEditSendThisTime.setObjectName("dateEditSendThisTime")
        self.gridLayout_5.addWidget(self.dateEditSendThisTime, 1, 1, 1, 1)
        self.dateTimeEditSendThisTime = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEditSendThisTime.setObjectName("dateTimeEditSendThisTime")
        self.gridLayout_5.addWidget(self.dateTimeEditSendThisTime, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 1, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_6.setHorizontalSpacing(15)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.gridLayout_4.addLayout(self.formLayout_6, 0, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout_4.setContentsMargins(-1, -1, 15, -1)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.gridLayout_4.addLayout(self.formLayout_4, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 8, 0, 1, 3)
        self.comboBoxTelemetry = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxTelemetry.sizePolicy().hasHeightForWidth())
        self.comboBoxTelemetry.setSizePolicy(sizePolicy)
        self.comboBoxTelemetry.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBoxTelemetry.setCurrentText("")
        self.comboBoxTelemetry.setObjectName("comboBoxTelemetry")
        self.comboBoxTelemetry.addItem("")
        self.comboBoxTelemetry.addItem("")
        self.comboBoxTelemetry.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxTelemetry, 0, 2, 1, 1)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSendTCReq.sizePolicy().hasHeightForWidth())
        self.pushButtonSendTCReq.setSizePolicy(sizePolicy)
        self.pushButtonSendTCReq.setObjectName("pushButtonSendTCReq")
        self.gridLayout_3.addWidget(self.pushButtonSendTCReq, 2, 1, 1, 1)
        self.checkBoxTelemetryContinuous = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxTelemetryContinuous.setEnabled(True)
        self.checkBoxTelemetryContinuous.setCheckable(True)
        self.checkBoxTelemetryContinuous.setChecked(False)
        self.checkBoxTelemetryContinuous.setObjectName("checkBoxTelemetryContinuous")
        self.gridLayout_3.addWidget(self.checkBoxTelemetryContinuous, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tabTelemetry, "")
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
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.formLayoutTLMCH.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.formLayoutTLMCH.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_9)
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
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setObjectName("label_14")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.gridLayout_6.addLayout(self.formLayout_10, 0, 6, 1, 1)
        self.lineEditChannel = QtWidgets.QLineEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditChannel.sizePolicy().hasHeightForWidth())
        self.lineEditChannel.setSizePolicy(sizePolicy)
        self.lineEditChannel.setObjectName("lineEditChannel")
        self.gridLayout_6.addWidget(self.lineEditChannel, 0, 2, 1, 1)
        self.checkBoxLastReqContinuous = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBoxLastReqContinuous.setObjectName("checkBoxLastReqContinuous")
        self.gridLayout_6.addWidget(self.checkBoxLastReqContinuous, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 3, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tabTelecommanding, "")
        self.tabFileTransfer = QtWidgets.QWidget()
        self.tabFileTransfer.setObjectName("tabFileTransfer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabFileTransfer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tabFileTransfer)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_5.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.lblTelecommandN_2 = QtWidgets.QLabel(self.groupBox_7)
        self.lblTelecommandN_2.setObjectName("lblTelecommandN_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandN_2)
        self.inputTelecommandNUploadTo = QtWidgets.QLineEdit(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTelecommandNUploadTo.sizePolicy().hasHeightForWidth())
        self.inputTelecommandNUploadTo.setSizePolicy(sizePolicy)
        self.inputTelecommandNUploadTo.setObjectName("inputTelecommandNUploadTo")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandNUploadTo)
        self.lblTelecommandData_2 = QtWidgets.QLabel(self.groupBox_7)
        self.lblTelecommandData_2.setObjectName("lblTelecommandData_2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandData_2)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.inputTelecommandDataUploadFrom = QtWidgets.QLineEdit(self.groupBox_7)
        self.inputTelecommandDataUploadFrom.setObjectName("inputTelecommandDataUploadFrom")
        self.horizontalLayout_24.addWidget(self.inputTelecommandDataUploadFrom)
        self.pushButtonOpenFileUploadFrom = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButtonOpenFileUploadFrom.setObjectName("pushButtonOpenFileUploadFrom")
        self.horizontalLayout_24.addWidget(self.pushButtonOpenFileUploadFrom)
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_24)
        self.verticalLayout_6.addLayout(self.formLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_7)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tabFileTransfer)
        self.groupBox_12.setObjectName("groupBox_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_8.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_8.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_8.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_8.setObjectName("formLayout_8")
        self.lblTelecommandN_3 = QtWidgets.QLabel(self.groupBox_12)
        self.lblTelecommandN_3.setObjectName("lblTelecommandN_3")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandN_3)
        self.inputTelecommandNUploadTo_2 = QtWidgets.QLineEdit(self.groupBox_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTelecommandNUploadTo_2.sizePolicy().hasHeightForWidth())
        self.inputTelecommandNUploadTo_2.setSizePolicy(sizePolicy)
        self.inputTelecommandNUploadTo_2.setObjectName("inputTelecommandNUploadTo_2")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputTelecommandNUploadTo_2)
        self.lblTelecommandData_3 = QtWidgets.QLabel(self.groupBox_12)
        self.lblTelecommandData_3.setObjectName("lblTelecommandData_3")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblTelecommandData_3)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.inputTelecommandDataUploadFrom_2 = QtWidgets.QLineEdit(self.groupBox_12)
        self.inputTelecommandDataUploadFrom_2.setObjectName("inputTelecommandDataUploadFrom_2")
        self.horizontalLayout_26.addWidget(self.inputTelecommandDataUploadFrom_2)
        self.pushButtonOpenFileDownloadTo = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButtonOpenFileDownloadTo.setObjectName("pushButtonOpenFileDownloadTo")
        self.horizontalLayout_26.addWidget(self.pushButtonOpenFileDownloadTo)
        self.formLayout_8.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_26)
        self.verticalLayout_8.addLayout(self.formLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_3.addWidget(self.pushButton_15)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_12)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_8.addWidget(self.progressBar_2)
        self.gridLayout_2.addWidget(self.groupBox_12, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabFileTransfer, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tabConfig)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tabConfig)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_23 = QtWidgets.QLabel(self.groupBox_9)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_25 = QtWidgets.QLabel(self.groupBox_9)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_8.addWidget(self.label_25)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_24 = QtWidgets.QLabel(self.groupBox_9)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.horizontalLayout_9.setStretch(0, 1)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem5)
        self.gridLayout_10.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_9, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabConfig, "")
        self.tabTest = QtWidgets.QWidget()
        self.tabTest.setMinimumSize(QtCore.QSize(640, 0))
        self.tabTest.setObjectName("tabTest")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tabTest)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tabTest)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_7.setObjectName("formLayout_7")
        self.newFrameDelimiterLabel = QtWidgets.QLabel(self.groupBox_11)
        self.newFrameDelimiterLabel.setObjectName("newFrameDelimiterLabel")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.newFrameDelimiterLabel)
        self.newFrameDelimiterLineEdit = QtWidgets.QLineEdit(self.groupBox_11)
        self.newFrameDelimiterLineEdit.setMinimumSize(QtCore.QSize(40, 0))
        self.newFrameDelimiterLineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.newFrameDelimiterLineEdit.setObjectName("newFrameDelimiterLineEdit")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.newFrameDelimiterLineEdit)
        self.reservedBytesLabel = QtWidgets.QLabel(self.groupBox_11)
        self.reservedBytesLabel.setObjectName("reservedBytesLabel")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.reservedBytesLabel)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.newFrameDelimiterLineEdit_3 = QtWidgets.QLineEdit(self.groupBox_11)
        self.newFrameDelimiterLineEdit_3.setMinimumSize(QtCore.QSize(40, 0))
        self.newFrameDelimiterLineEdit_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.newFrameDelimiterLineEdit_3.setObjectName("newFrameDelimiterLineEdit_3")
        self.horizontalLayout_22.addWidget(self.newFrameDelimiterLineEdit_3)
        self.newFrameDelimiterLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_11)
        self.newFrameDelimiterLineEdit_2.setMinimumSize(QtCore.QSize(40, 0))
        self.newFrameDelimiterLineEdit_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.newFrameDelimiterLineEdit_2.setObjectName("newFrameDelimiterLineEdit_2")
        self.horizontalLayout_22.addWidget(self.newFrameDelimiterLineEdit_2)
        self.newFrameDelimiterLineEdit_4 = QtWidgets.QLineEdit(self.groupBox_11)
        self.newFrameDelimiterLineEdit_4.setMinimumSize(QtCore.QSize(40, 0))
        self.newFrameDelimiterLineEdit_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.newFrameDelimiterLineEdit_4.setObjectName("newFrameDelimiterLineEdit_4")
        self.horizontalLayout_22.addWidget(self.newFrameDelimiterLineEdit_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem6)
        self.formLayout_7.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_22)
        self.dataTypeLabel = QtWidgets.QLabel(self.groupBox_11)
        self.dataTypeLabel.setObjectName("dataTypeLabel")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dataTypeLabel)
        self.newFrameDelimiterLineEdit_5 = QtWidgets.QLineEdit(self.groupBox_11)
        self.newFrameDelimiterLineEdit_5.setMinimumSize(QtCore.QSize(40, 0))
        self.newFrameDelimiterLineEdit_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.newFrameDelimiterLineEdit_5.setObjectName("newFrameDelimiterLineEdit_5")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.newFrameDelimiterLineEdit_5)
        self.dataLengthLabel = QtWidgets.QLabel(self.groupBox_11)
        self.dataLengthLabel.setObjectName("dataLengthLabel")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dataLengthLabel)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.newFrameDelimiterLineEdit_6 = QtWidgets.QLineEdit(self.groupBox_11)
        self.newFrameDelimiterLineEdit_6.setMinimumSize(QtCore.QSize(40, 0))
        self.newFrameDelimiterLineEdit_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.newFrameDelimiterLineEdit_6.setObjectName("newFrameDelimiterLineEdit_6")
        self.horizontalLayout_23.addWidget(self.newFrameDelimiterLineEdit_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem7)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_23.addWidget(self.pushButton_11)
        self.formLayout_7.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_23)
        self.dataFieldLabel = QtWidgets.QLabel(self.groupBox_11)
        self.dataFieldLabel.setObjectName("dataFieldLabel")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dataFieldLabel)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_3)
        self.responseLabel = QtWidgets.QLabel(self.groupBox_11)
        self.responseLabel.setObjectName("responseLabel")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.responseLabel)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_4)
        self.gridLayout_11.addLayout(self.formLayout_7, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_11, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabTest, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.lblTelecommandData.setBuddy(self.inputTelecommandData)
        self.label_10.setBuddy(self.dateTimeEditSendThisTime)
        self.lblTelecommandN.setBuddy(self.inputTelecommandN)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        self.comboBoxTelemetry.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OSSAT Platform Computer Comms"))
        self.groupBox.setTitle(_translate("Form", "Telemetry"))
        self.lblTelecommandData.setText(_translate("Form", "Data"))
        self.groupBox_2.setTitle(_translate("Form", "Time Commands"))
        self.pushButtonSendPcTime.setText(_translate("Form", "Send PC Time"))
        self.pushButtonSendThisTime.setText(_translate("Form", "Send this Time :"))
        self.dateTimeEditSendThisTime.setDisplayFormat(_translate("Form", "HH:mm:ss.zzz"))
        self.label_10.setText(_translate("Form", "ms"))
        self.groupBox_3.setTitle(_translate("Form", "Last Response"))
        self.label_3.setText(_translate("Form", "TC #"))
        self.label_4.setText(_translate("Form", "N"))
        self.label_5.setText(_translate("Form", "Response"))
        self.label_6.setText(_translate("Form", "N/A"))
        self.label_7.setText(_translate("Form", "TIMEOUTS :"))
        self.label_8.setText(_translate("Form", "N/A"))
        self.comboBoxTelemetry.setItemText(0, _translate("Form", "String"))
        self.comboBoxTelemetry.setItemText(1, _translate("Form", "Integer"))
        self.comboBoxTelemetry.setItemText(2, _translate("Form", "Floating Point"))
        self.lblTelecommandN.setText(_translate("Form", "TC #"))
        self.pushButtonSendTCReq.setText(_translate("Form", "Send TC REQ"))
        self.checkBoxTelemetryContinuous.setText(_translate("Form", "Continuous?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTelemetry), _translate("Form", "TELECOMMANDING"))
        self.groupBox_4.setTitle(_translate("Form", "Telecommanding"))
        self.label_2.setText(_translate("Form", "TLM CH #"))
        self.label_9.setText(_translate("Form", "N/A"))
        self.groupBox_6.setTitle(_translate("Form", "Last Response"))
        self.label.setText(_translate("Form", "Channel #"))
        self.pushButtonSendTlmReq.setText(_translate("Form", "Send TLM REQ"))
        self.labelTimeOuts.setText(_translate("Form", "TIMEOUTS:"))
        self.label_14.setText(_translate("Form", "N/A"))
        self.checkBoxLastReqContinuous.setText(_translate("Form", "Continuous?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTelecommanding), _translate("Form", "TELEMETRY"))
        self.groupBox_7.setTitle(_translate("Form", "To Upload"))
        self.lblTelecommandN_2.setText(_translate("Form", "Upload to:"))
        self.lblTelecommandData_2.setText(_translate("Form", "Upload from:"))
        self.pushButtonOpenFileUploadFrom.setText(_translate("Form", "..."))
        self.pushButton_8.setText(_translate("Form", "Upload Now"))
        self.pushButton_13.setText(_translate("Form", "Abort Upload"))
        self.groupBox_12.setTitle(_translate("Form", "To Download"))
        self.lblTelecommandN_3.setText(_translate("Form", "Download from:"))
        self.lblTelecommandData_3.setText(_translate("Form", "Download to:"))
        self.pushButtonOpenFileDownloadTo.setText(_translate("Form", "..."))
        self.pushButton_15.setText(_translate("Form", "Request Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFileTransfer), _translate("Form", "FILE TRANSFER"))
        self.groupBox_9.setTitle(_translate("Form", "Config"))
        self.label_23.setText(_translate("Form", "Comms baud"))
        self.comboBox.setItemText(0, _translate("Form", "9600"))
        self.comboBox.setItemText(1, _translate("Form", "19200"))
        self.comboBox.setItemText(2, _translate("Form", "38400"))
        self.comboBox.setItemText(3, _translate("Form", "57600"))
        self.comboBox.setItemText(4, _translate("Form", "115200"))
        self.comboBox.setItemText(5, _translate("Form", "230400"))
        self.comboBox.setItemText(6, _translate("Form", "460800"))
        self.comboBox.setItemText(7, _translate("Form", "921600"))
        self.label_25.setText(_translate("Form", "TC/TLM Timeout (ms)"))
        self.label_24.setText(_translate("Form", "Config file"))
        self.pushButton_2.setText(_translate("Form", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("Form", "CONFIG"))
        self.groupBox_11.setTitle(_translate("Form", "Test"))
        self.newFrameDelimiterLabel.setText(_translate("Form", "New Frame Delimiter"))
        self.reservedBytesLabel.setText(_translate("Form", "RESERVED Bytes"))
        self.dataTypeLabel.setText(_translate("Form", "Data Type"))
        self.dataLengthLabel.setText(_translate("Form", "Data Length"))
        self.pushButton_11.setText(_translate("Form", "Transmit"))
        self.dataFieldLabel.setText(_translate("Form", "Data Field"))
        self.responseLabel.setText(_translate("Form", "Response"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTest), _translate("Form", "TEST"))
