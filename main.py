# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget , QMessageBox, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import urllib.request



class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.btn_1.clicked.connect(self.browse)
        self.ui.btn_2.clicked.connect(self.download)
        self.ui.setWindowTitle('Downloader!')
        self.ui.show()

    def download(self):
        url = self.ui.ln_1.text()
        file = self.ui.ln_2.text()

        try:
            urllib.request.urlretrieve(url, file, self.report)
            QMessageBox.information(self, 'Done!', 'Download Complete')
            self.ui.pg_1.setValue(0)
            self.ui.ln_1.setText('')
            self.ui.ln_2.setText('')
        except:
            msg_box = QMessageBox()
            msg_box.setText('Download Error!')
            msg_box.exec_()

    def browse(self):
        loc = QFileDialog.getSaveFileName(self, caption='Download location', filter='All Files (*.*)')
        self.ui.ln_2.setText(loc[0])

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize>0:
            percent = readsofar * 100 / totalsize
            self.ui.pg_1.setValue(int(percent))

if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
