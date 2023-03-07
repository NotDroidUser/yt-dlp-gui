import json
import urllib
from pathlib import Path

import urllib3
from PySide6.QtCore import QProcess, QTimerEvent

# noinspection PyUnresolvedReferences
from urllib3.util import parse_url

import re
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from gui.ytdlp_gui import Ui_Dialog as YTDialogUI
import sys

# future
# class DlProcess:
#     def __init__(self,ytInfo,link,filename):
#         self.link = link
#         self.ytInfo = ytInfo
#         self.process=QProcess()
#         self.filename=""
#
#     def timer():
#         self.



def format_info_yt(ytInfo: dict):
    info = ""

    # debug
    # print(ytInfo)

    info += ytInfo["format_note"] + " "

    if ytInfo["audio_ext"] != "none":
        info += f"{ytInfo['asr']}-"
        info += ytInfo["audio_ext"]

    if ytInfo["video_ext"] != "none":
        info += f'{ytInfo["width"]}x{ytInfo["height"]} '
        info += ytInfo["video_ext"]
        if ytInfo["asr"]:
            info += " with audio"

    if 'filesize' in ytInfo.keys():
        if ytInfo['filesize']:
            info += f" {format_bytes(ytInfo['filesize'])}"
    return info


def format_bytes(size):
    bytesize = ["b", "Kb", "Mb", "Gb", "Tb"]
    count = 0
    filesize = size
    while filesize / 1024 >= 1:
        count += 1
        filesize = filesize / 1024
    return f"%.2f {bytesize[count]}" % filesize


class YTDialog(QDialog,YTDialogUI):
    def  __init__(self):
        super(YTDialog, self).__init__()
        self.dlprocess = None
        self.timerId = None
        self.process = None
        self.setupUi(self)
        self.youtubeInfo=None
        #debug
        self.link.setText("https://www.youtube.com/watch?v=VQ6ytsjB-mk")
        self.explore.clicked.connect(self.exploreFormats)
        self.dl.clicked.connect(self.onDl)

    def exploreFormats(self):
        link=self.link.text()
        if re.match("https://(www|m).youtube.com*.|https://youtu.be*.", link):
            self.explore.setEnabled(False)
            self.explore.setText("Descargando formatos...")
            process = QProcess()
            process.startCommand(f"yt-dlp -j {link}")
            process.finished.connect(lambda: self.async_formats(process.readAllStandardOutput().toStdString()) )


    def async_formats(self,out):
        try:
            self.youtubeInfo = json.JSONDecoder().decode(out)
            # debug
            #print(self.youtubeInfo)
            self.title.setText(self.youtubeInfo["title"])
            self.quality.clear()
            for i in self.youtubeInfo["formats"]:
                format=format_info_yt(i)
                if format!="":
                    self.quality.addItem(format, i["format_id"])
            self.dlSet(True)
        except:
            QMessageBox.critical(self, "Error",
                        "Error al comprobar los formatos disponibles, compruebe su conexion")
        self.process = None
        self.explore.setText("Explorar")
        self.explore.setEnabled(True)

    def dlSet(self,set=False):
        self.dl.setEnabled(set)
        self.title.setEnabled(set)
        self.quality.setEnabled(set)

    def onDl(self):
        ytFormat=self.quality.itemData(self.quality.currentIndex())
        if QMessageBox.question(self,"Descargar", f"Desea descargar {self.title.text()} en el formato {self.quality.itemText(self.quality.currentIndex())} ", QMessageBox.Yes, QMessageBox.No)==QMessageBox.Yes:
            self.dlprocess = QProcess()
            link = self.link.text()
            ytInfo=self.youtubeInfo["formats"][self.quality.currentIndex()]
            # todo
            if 'filesize' in ytInfo.keys():
                if ytInfo['filesize']:
                    self.timerId=self.startTimer(5)
            filename = "".join(i for i in self.youtubeInfo["title"] if i ==" " or i.isalnum())
            ext = ""
            if ytInfo["audio_ext"] != "none":
                ext = ytInfo["audio_ext"]
            if ytInfo["video_ext"] != "none":
                ext = ytInfo["video_ext"]
            print(f"yt-dlp -f {ytFormat} -o {str(Path(filename))+'.'+ext} {link}")
            self.dlprocess.startCommand(f"yt-dlp -f {ytFormat} -o \"{str(Path(filename))+'.'+ext}\" {link}")
            self.dlprocess.finished.connect(self.onDlFinish)

    def onDlFinish(self):
        self.killTimer(self.timerId)
        self.timerId=None
        # todo
        #self.progressBar.setValue(100)
        self.dlprocess=None

    # todo
    def timerEvent(self, event: QTimerEvent) -> None:
        if event.timerId()==self.timerId:
            ytInfo=self.youtubeInfo["formats"][self.quality.currentIndex()]
            if 'filesize' in ytInfo.keys():
                if ytInfo['filesize']:
                    filename = "".join(i for i in self.youtubeInfo["title"] if i ==" " or i.isalnum())
                    ext=""
                    if ytInfo["audio_ext"] != "none":
                        ext = ytInfo["audio_ext"]
                    if ytInfo["video_ext"] != "none":
                        ext = ytInfo["video_ext"]
                    path=Path(".").joinpath(filename+"."+ext+".part")
                    if path.exists():
                        print(path.lstat().st_size)
                        print(ytInfo['filesize'])
                        self.progressBar.setValue(int(path.lstat().st_size/ytInfo['filesize']*100))


if __name__ == '__main__':
    app=QApplication()
    dialog=YTDialog()
    dialog.show()
    sys.exit(app.exec())