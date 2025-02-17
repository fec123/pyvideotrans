# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolboxen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QMetaObject

from videotrans.component.component import Textedit
from videotrans.configure import config
from videotrans.configure.config import box_lang


class Ui_peiyin(object):
    def setupUi(self, peiyin):
        if not peiyin.objectName():
            peiyin.setObjectName(u"peiyin")
        peiyin.resize(643, 500)
        peiyin.setWindowModality(QtCore.Qt.NonModal)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(peiyin.sizePolicy().hasHeightForWidth())
        peiyin.setSizePolicy(sizePolicy)


        self.hecheng_files=[]

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(peiyin)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hecheng_layout = QtWidgets.QVBoxLayout()
        self.hecheng_layout.setObjectName("hecheng_layout")


        self.hecheng_plaintext = Textedit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hecheng_plaintext.sizePolicy().hasHeightForWidth())
        self.hecheng_plaintext.setSizePolicy(sizePolicy)
        self.hecheng_plaintext.setMinimumSize(0, 150)
        self.hecheng_plaintext.setPlaceholderText(config.transobj['tuodonghuoshuru'])
        self.hecheng_importbtn = QtWidgets.QPushButton()
        self.hecheng_importbtn.setObjectName("hecheng_importbtn")
        self.hecheng_importbtn.setFixedHeight(150)
        self.hecheng_importbtn.setCursor(Qt.PointingHandCursor)

        self.hecheng_importbtn.setText(config.box_lang['Import text to be translated from a file..'])

        self.hecheng_layout.insertWidget(0, self.hecheng_importbtn)
        self.hecheng_layout.insertWidget(1, self.hecheng_plaintext)
        self.verticalLayout_4.addLayout(self.hecheng_layout)



        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10_1.setObjectName("horizontalLayout_10_1")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.hecheng_language = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hecheng_language.sizePolicy().hasHeightForWidth())
        self.hecheng_language.setSizePolicy(sizePolicy)
        self.hecheng_language.setMinimumSize(QtCore.QSize(0, 30))
        self.hecheng_language.setObjectName("hecheng_language")
        self.hecheng_language.addItems(['-'] + config.langnamelist)



        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hecheng_language)
        self.horizontalLayout_10.addLayout(self.formLayout_3)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setObjectName("label_8")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.tts_type = QtWidgets.QComboBox()
        self.tts_type.setMinimumSize(QtCore.QSize(0, 30))
        self.tts_type.setObjectName("tts_type")
        self.tts_type.addItems([i for i in config.params['tts_type_list']])
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tts_type)
        self.horizontalLayout_10.addLayout(self.formLayout_7)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_11 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.hecheng_role = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hecheng_role.sizePolicy().hasHeightForWidth())
        self.hecheng_role.setSizePolicy(sizePolicy)
        self.hecheng_role.setMinimumSize(QtCore.QSize(0, 30))
        self.hecheng_role.setObjectName("hecheng_role")
        self.hecheng_role.addItems(['No'])
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hecheng_role)
        self.horizontalLayout_10.addLayout(self.formLayout_4)

        self.listen_btn = QtWidgets.QPushButton()
        self.listen_btn.setFixedWidth(80)
        self.listen_btn.setToolTip(config.uilanglist.get("shuoming01"))
        self.listen_btn.setText(config.uilanglist.get("Trial dubbing"))
        self.horizontalLayout_10.addWidget(self.listen_btn)

        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_12 = QtWidgets.QLabel()
        self.label_12.setMinimumSize(QtCore.QSize(0, 30))
        self.label_12.setObjectName("label_12")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.hecheng_rate = QtWidgets.QSpinBox()
        self.hecheng_rate.setMinimumSize(QtCore.QSize(0, 30))
        self.hecheng_rate.setMinimum(-100)
        self.hecheng_rate.setMaximum(100)
        self.hecheng_rate.setObjectName("hecheng_rate")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hecheng_rate)
        self.horizontalLayout_10_1.addLayout(self.formLayout_5)

        self.voice_autorate = QtWidgets.QCheckBox()
        self.voice_autorate.setObjectName("voice_autorate")

        self.horizontalLayout_10_1.addWidget(self.voice_autorate)

        self.edge_volume_layout = QtWidgets.QHBoxLayout()

        self.volume_label = QtWidgets.QLabel()
        self.volume_label.setText("音量+" if config.defaulelang == 'zh' else "Volume+")

        self.volume_rate = QtWidgets.QSpinBox()
        self.volume_rate.setMinimum(-95)
        self.volume_rate.setMaximum(100)
        self.volume_rate.setObjectName("volume_rate")

        self.pitch_label = QtWidgets.QLabel()
        self.pitch_label.setText("音调+" if config.defaulelang == 'zh' else "Pitch+")
        self.pitch_rate = QtWidgets.QSpinBox()
        self.pitch_rate.setMinimum(-100)
        self.pitch_rate.setMaximum(100)
        self.pitch_rate.setObjectName("pitch_rate")

        self.edge_volume_layout.addWidget(self.volume_label)
        self.edge_volume_layout.addWidget(self.volume_rate)
        self.edge_volume_layout.addWidget(self.pitch_label)
        self.edge_volume_layout.addWidget(self.pitch_rate)

        self.horizontalLayout_10_1.addLayout(self.edge_volume_layout)
        self.hecheng_startbtn = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hecheng_startbtn.sizePolicy().hasHeightForWidth())
        self.hecheng_startbtn.setSizePolicy(sizePolicy)
        self.hecheng_startbtn.setMinimumSize(QtCore.QSize(200, 40))
        self.hecheng_startbtn.setObjectName("hecheng_startbtn")
        self.hecheng_startbtn.setCursor(Qt.PointingHandCursor)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10_1)

        self.verticalLayout_4.addWidget(self.hecheng_startbtn)

        self.loglabel=QtWidgets.QLabel()
        self.loglabel.setStyleSheet("""color:#999""")
        self.verticalLayout_4.addWidget(self.loglabel)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setMinimumSize(QtCore.QSize(100, 30))
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.hecheng_out = QtWidgets.QLineEdit()
        self.hecheng_out.setMinimumSize(QtCore.QSize(0, 35))
        self.hecheng_out.setReadOnly(False)
        self.hecheng_out.setObjectName("hecheng_out")
        self.gridLayout_3.addWidget(self.hecheng_out, 0, 1, 1, 1)
        self.hecheng_opendir = QtWidgets.QPushButton()
        self.hecheng_opendir.setObjectName("hecheng_opendir")
        self.hecheng_opendir.setMinimumSize(QtCore.QSize(100,35))
        self.gridLayout_3.addWidget(self.hecheng_opendir, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)


        self.retranslateUi(peiyin)

         # tab-4 语音合成

        QMetaObject.connectSlotsByName(peiyin)

    def retranslateUi(self, peiyin):
        peiyin.setWindowTitle('批量字幕配音' if config.defaulelang=='zh' else 'Batch Subtitle Dubbing')

        self.label_10.setText(box_lang.get("Subtitle lang"))
        self.label_8.setText("TTS" if config.defaulelang!='zh'else'配音渠道')
        self.label_11.setText(box_lang.get("Select role"))
        self.label_12.setText(box_lang.get("Speed change"))
        self.hecheng_rate.setToolTip(box_lang.get("Negative deceleration, positive acceleration"))
        self.voice_autorate.setText(box_lang.get("Automatic acceleration?"))
        self.hecheng_startbtn.setText(box_lang.get("Start"))
        self.label_7.setText(box_lang.get("Output audio name"))
        self.hecheng_out.setPlaceholderText(box_lang.get(
            "Set the name of the generated audio file here. If not filled in, use the time and date command"))
        self.hecheng_opendir.setText(box_lang.get("Open dir"))


