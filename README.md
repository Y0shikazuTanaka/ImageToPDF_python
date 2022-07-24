# ImageToPDF_python

## できること
画像が入ったフォルダをドロップアンドドラッグして追加し、Startボタンを押すとPDFファイルへ変換する。  
行を選択し、Delete・BackSpaceで行の削除ができる。

## exeビルド

```commandline
cd python
# EXE作成
pyinstaller --clean --onefile -w --icon=..\resources\icon.ico main.py
# SPEC設定反映
pyinstaller main.spec
```