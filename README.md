# ImageToPDF_python

## exeビルド

```commandline
cd python
# EXE作成
pyinstaller -F -w --icon=../resources/icon.ico --add-data "../resources/icon.ico;." --name ImageToPDF.exe main.py
# SPEC設定反映
pyinstaller main.spec
```