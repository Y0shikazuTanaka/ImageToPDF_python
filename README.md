# ImageToPDF_python

## 経緯
Macを使っていたけど2022年7月からWindowsへ乗り換えたので、新しく作りました。  
https://github.com/Y0shikazuTanaka/kantanPDF_swift  
Macは売却したので、こっちはもう更新しなくなります。

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