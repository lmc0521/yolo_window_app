from PySide6.QtCore import QThread, Signal
from ultralytics import YOLO


class ModelThread(QThread):
    callback=Signal(object)
    def init(self,parent=None):
        super().__init__(parent)
    def run(self):
        model=YOLO('./yolov8n.pt')
        self.callback.emit(model)