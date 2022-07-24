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
import dataclasses

CONF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.resource_path("window.kv"))
Builder.load_file(CONF_PATH)

FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), config.resource_path("YuGothM.ttc"))
LabelBase.register(DEFAULT_FONT, FONT_PATH)


@dataclasses.dataclass
class FolderData:
    parent_path: str
    folder_name: str
    folder_path: str


class WindowWidget(Widget):
    isAllFileRemove = BooleanProperty(None)
    folder_data_list: list[FolderData]

    pbStep = 0.0

    def __init__(self, **kwargs):
        super(WindowWidget, self).__init__(**kwargs)
        self._file = Window.bind(on_dropfile=self.folderDropEvent)

        # ファイルリストビュー初期化
        self.rv.data = []
        self.folder_data_list = []
        # プログレスバー初期化
        self.pb.value = 0.0

    # スタートボタンクリック
    def startButtonClicked(self):
        print("startButtonClicked")
        pc = pdfCreater.PdfCreater()
        for folder_data in self.folder_data_list:
            pc.createPDF(folder_data.folder_path, folder_data.parent_path)
            self.pb.value += self.pbStep

    # フォルダードラッグアンドドロップイベント
    def folderDropEvent(self, window, file_path):
        self.rv.data = []
        plib = pathlib.Path(file_path.decode())
        dirs = plib.glob("**/")

        c = config.Config()
        chek_img_format_list = c.imgFormats.split(',')
        parent_path = plib.parent

        for f in dirs:
            files = []
            checklist = [tmp_folder_data for tmp_folder_data in self.folder_data_list if tmp_folder_data.folder_path == str(f)]
            # 重複チェック
            if len(checklist) == 0:
                for ext in chek_img_format_list:
                    files.extend(f.glob(f"*.{ext}"))
                if len(files) > 0:
                    self.folder_data_list.append(FolderData(str(parent_path), f.name, str(f)))

        self.pbStep = 1 / len(self.folder_data_list)

        for folder_data in self.folder_data_list:
            self.rv.data.append({
                'fileName': folder_data.folder_name,
                'folderName': folder_data.folder_name,
                'folderPath': folder_data.folder_path,
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
