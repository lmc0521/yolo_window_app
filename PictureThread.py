import os

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap


class PictureThread(QThread):
    callback = Signal(object)
    def __init__(self,path,parent=None):
        super().__init__(parent)
        self.path=path
        self.runFlag=True
    def run(self):
        files=[]
        for file in os.listdir(self.path):
            tmp=file.lower()
            if tmp.endswith('.jpg') or tmp.endswith('.png'):
                files.append(os.path.join(self.path,file))
        index=0
        total=len(files)
        while index<total and self.runFlag:
            pix=QPixmap(files[index])
            pix=pix.scaled(250,187)
            pix.tag=files[index]
            self.callback.emit(pix)
            index+=1
            QThread.msleep(10)
