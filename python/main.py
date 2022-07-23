import os
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, BooleanProperty
import pathlib
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

import pdfCreater
import config

CONF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.resource_path("window.kv"))
Builder.load_file(CONF_PATH)

FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.resource_path("YuGothM.ttc"))
LabelBase.register(DEFAULT_FONT, FONT_PATH)


class WindowWidget(Widget):
    isAllFileRemove = BooleanProperty(None)
    fileNames = []
    folderNames = []
    folderPaths = []

    dropParentPath = None

    pbStep = 0.0

    def __init__(self, **kwargs):
        super(WindowWidget, self).__init__(**kwargs)
        self._file = Window.bind(on_dropfile=self.folderDropEvent)

        # ファイルリストビュー初期化
        self.rv.data = []
        # プログレスバー初期化
        self.pb.value = 0.0

    # スタートボタンクリック
    def startButtonClicked(self):
        print("startButtonClicked")
        pc = pdfCreater.PdfCreater()
        for i in range(len(self.fileNames)):
            pc.createPDF(self.folderPaths[i], self.dropParentPath)
            self.pb.value += self.pbStep

    # フォルダードラッグアンドドロップイベント
    def folderDropEvent(self, window, file_path):
        plib = pathlib.Path(file_path.decode())
        dirs = plib.glob("**/")

        c = config.Config()
        chekImgFormatList = c.imgFormats.split(',')

        self.dropParentPath = plib.parent

        self.rv.data = []

        self.fileNames = []
        self.folderNames = []
        self.folderPaths = []

        for f in dirs:
            files = []
            for ext in chekImgFormatList:
                files.extend(f.glob(f"*.{ext}"))

            if len(files) > 0:
                self.fileNames.append(f.name)
                self.folderNames.append(f.name)
                self.folderPaths.append(f)

        self.pbStep = 1 / len(self.fileNames)

        for i in range(len(self.fileNames)):
            self.rv.data.append({
                'fileName': self.fileNames[i],
                'folderName': self.folderNames[i],
                'folderPath': str(self.folderPaths[i]),
            })


class RecycleViewRow(RecycleDataViewBehavior, BoxLayout):
    print("RecycleViewRow")
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    # インデックスの取得とRowの更新
    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super(RecycleViewRow, self).refresh_view_attrs(rv, index, data)

    # Rowのクリックイベント取得
    def on_touch_down(self, touch):
        if super(RecycleViewRow, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    # Row選択状態の入れ替え
    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    print("SelectableRecycleBoxLayout")


class ImageToPDF(App):
    def __init__(self, **kwargs):
        super(ImageToPDF, self).__init__(**kwargs)
        self.title = 'ImageToPDF'

    def build(self):
        return WindowWidget()


if __name__ == '__main__':
    ImageToPDF().run()
