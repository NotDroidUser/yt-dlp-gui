# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ytdlp_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(611, 206)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.linkView = QHBoxLayout()
        self.linkView.setObjectName(u"linkView")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.linkView.addWidget(self.label)

        self.link = QLineEdit(Dialog)
        self.link.setObjectName(u"link")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.link.sizePolicy().hasHeightForWidth())
        self.link.setSizePolicy(sizePolicy1)

        self.linkView.addWidget(self.link)


        self.verticalLayout_2.addLayout(self.linkView)

        self.explore = QPushButton(Dialog)
        self.explore.setObjectName(u"explore")

        self.verticalLayout_2.addWidget(self.explore)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.titleLabel)

        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.quality = QComboBox(Dialog)
        self.quality.setObjectName(u"quality")

        self.verticalLayout_3.addWidget(self.quality)

        self.dl = QPushButton(Dialog)
        self.dl.setObjectName(u"dl")

        self.verticalLayout_3.addWidget(self.dl)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Link:", None))
        self.explore.setText(QCoreApplication.translate("Dialog", u"Explorar", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Titulo:", None))
        self.title.setText("")
        self.dl.setText(QCoreApplication.translate("Dialog", u"Descargar", None))
    # retranslateUi

