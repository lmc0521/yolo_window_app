import sys
import time

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidgetItem, QFileDialog

from DetectThread import DetectThread
from ModelThread import ModelThread
from PictureThread import PictureThread
from ui.ui_mainwindow import Ui_MainWindow

class YoloPicture(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.path='C:/pictures'
        self.lblPath.setText(self.path)
        self.lblStatus.setText('載入模型中...')
        self.modelThread=ModelThread()
        self.modelThread.callback.connect(self.modelThreadCallback)
        self.modelThread.start()
        self.btnPath.clicked.connect(self.btnPathClick)
    def btnPathClick(self):
        path=QFileDialog.getExistingDirectory()
        if path!='':
            self.path=path.replace('\\','/')
            self.lblPath.setText(self.path)
            self.pictuerThread.runFlag=False
            time.sleep(0.01)
            self.listWidget.clear()
            self.pictuerThread = PictureThread(self.path)
            self.pictuerThread.callback.connect(self.pictureThreadCallback)
            self.pictuerThread.start()
    def modelThreadCallback(self,model):
        self.lblStatus.setText('載入模型完成')
        self.model=model
        self.pictuerThread=PictureThread(self.path)
        self.pictuerThread.callback.connect(self.pictureThreadCallback)
        self.pictuerThread.start()
    def pictureThreadCallback(self,pix):
        btn=QPushButton()
        btn.setIcon(QIcon(pix))
        btn.setIconSize(QSize(250,187))
        btn.tag=pix.tag
        btn.clicked.connect(self.btnClick)
        item=QListWidgetItem()
        item.setSizeHint(QSize(250,187))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item,btn)

    def btnClick(self):
        btn=self.sender()
        self.lblStatus.setText('yolov8辨識中...')
        self.t1=time.time()
        self.detectThread=DetectThread(self.model,btn.tag)
        self.detectThread.callback.connect(self.detectThreadCallback)
        self.detectThread.start()
        print(btn.tag)

    def detectThreadCallback(self,img):
        self.t2=time.time()
        self.lblStatus.setText(f'花費{self.t2-self.t1:.2f}秒')
        pix=QPixmap(
            QImage(
                img,
                img.shape[1],
                img.shape[0],
                img.shape[1]*3,
                QImage.Format.Format_RGB888
            )
        )
        pr=pix.width()/pix.height()
        lr=self.lblImg.width()/self.lblImg.height()
        if pr>lr:
            pix=pix.scaled(self.lblImg.width(),int(self.lblImg.width()/pr))
        else:
            pix=pix.scaled(int(self.lblImg.height()*lr),self.lblImg.height())
        self.lblImg.setPixmap(pix)
    def closeEvent(self, event):
        if self.pictureThread is not None:
            self.pictuerThread.runFlag=False
            time.sleep(0.01)

app=QApplication(sys.argv)
w=YoloPicture()
w.show()
app.exec()