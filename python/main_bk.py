# This is a sample Python script.


import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
from python import config
import os


def window_menu_about():
    print("メニュー/About ImageToPDF")


# 画面メニュー部/ファイル/開く イベント
def window_menu_open():
    print("メニュー/開く")
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    file_name = tk.filedialog.askdirectory(initialdir=desktop)
    print("window_menu_open select path {0}".format(file_name))


# 画面メニュー部/ファイル/閉じる イベント
def window_menu_quit():
    print("メニュー/閉じる")
    window.destroy()


#
# Windowを設定する
#
c = config.Config()

# メインウインドウ設定
window = tk.Tk()
window.title("{0} version: {1}".format(c.appName, c.version))
window.geometry("{0}x{1}".format(c.windowSizeWidth, c.windowSizeHeight))

# メニューバー
men = tk.Menu(window)
window.config(menu=men)
menuFile = tk.Menu(window, tearoff=0)
men.add_cascade(label='ファイル', menu=menuFile)
menuFile.add_command(label='About ImageToPDF', command=window_menu_about)
menuFile.add_separator()
menuFile.add_command(label='開く', command=window_menu_open)
menuFile.add_separator()
menuFile.add_command(label='閉じる', command=window_menu_quit)

# 左側設定項目フレーム
settingFrameWidth = 200
settingFrameHeight = 600
settingFrame = tk.Frame(window, width=settingFrameWidth, height=settingFrameHeight, bg="black")
settingFrame.grid(column=0, row=0, sticky=tk.N + tk.S)

# ファイルリストフレーム
folderListFrame = tk.Frame(window, width=700, height=settingFrameHeight, bg="blue")
folderListFrame.grid(column=1, row=0, sticky=tk.W + tk.E + tk.N + tk.S)

# progressフレーム
progressFrame = tk.Frame(window, width=settingFrameWidth, height=200, bg="green")
progressFrame.grid(columnspan=2, column=0, row=1, sticky=tk.W + tk.E)

# progressフレーム
addFrame = tk.Frame(window, width=settingFrameWidth, height=300, bg="yellow")
addFrame.grid(columnspan=2, column=0, row=2, sticky=tk.W + tk.E)

# 設定要素の配置
# ファイル名 row=0-1
label1Name = "ファイル名"
label1 = tk.Label(settingFrame, text=label1Name).grid(columnspan=3, row=0, column=0)
entry1 = tk.Entry(settingFrame).grid(columnspan=2, row=1, column=0, sticky=tk.W + tk.E)
chk1 = tk.Checkbutton(settingFrame).grid(row=1, column=2)

# タイトル row 2-3
label2Title = "タイトル"
label2 = tk.Label(settingFrame, text=label2Title).grid(columnspan=3, row=2, column=0)
entry2 = tk.Entry(settingFrame).grid(columnspan=2, row=3, column=0, sticky=tk.W + tk.E)
chk2 = tk.Checkbutton(settingFrame).grid(row=3, column=2)

# 著者 row 4-5
label3Title = "タイトル"
label3 = tk.Label(settingFrame, text=label3Title).grid(columnspan=3, row=4, column=0)
entry3 = tk.Entry(settingFrame).grid(columnspan=2, row=5, column=0, sticky=tk.W + tk.E)
chk3 = tk.Checkbutton(settingFrame).grid(row=5, column=2)

# 作成ソフト row 6-7
label4Title = "作成ソフト"
label4 = tk.Label(settingFrame, text=label4Title).grid(columnspan=3, row=6, column=0)
entry4 = tk.Entry(settingFrame).grid(columnspan=2, row=7, column=0, sticky=tk.W + tk.E)
chk4 = tk.Checkbutton(settingFrame).grid(row=7, column=2)

# 所有者パスワード row 8-9
label5Title = "所有者パスワード"
label5 = tk.Label(settingFrame, text=label5Title).grid(columnspan=3, row=8, column=0)
entry5 = tk.Entry(settingFrame).grid(columnspan=2, row=9, column=0, sticky=tk.W + tk.E)
chk5 = tk.Checkbutton(settingFrame).grid(row=9, column=2)

# 閲覧パスワード row 10-11
label6Title = "閲覧パスワード"
label6 = tk.Label(settingFrame, text=label6Title).grid(columnspan=3, row=10, column=0)
entry6 = tk.Entry(settingFrame).grid(columnspan=2, row=11, column=0, sticky=tk.W + tk.E)
chk6 = tk.Checkbutton(settingFrame).grid(row=11, column=2)

# プリント可否 row 12-13
label7Title = "プリント可否"
radio7TrueLabel = "可"
radio7FalseLabel = "不可"
flag7 = tk.StringVar()
label7 = tk.Label(settingFrame, text=label7Title).grid(columnspan=3, row=12, column=0)
rdo7true = tk.Radiobutton(settingFrame, text=radio7TrueLabel, value=0, variable=flag7).grid(row=13, column=0,
                                                                                            sticky=tk.W + tk.E)
rdo7false = tk.Radiobutton(settingFrame, text=radio7FalseLabel, value=1, variable=flag7).grid(row=13, column=1,
                                                                                              sticky=tk.W + tk.E)
chk7 = tk.Checkbutton(settingFrame).grid(row=13, column=2, sticky=tk.W + tk.E)

# 複製可否 row 14-15
label8Title = "複製可否"
radio8TrueLabel = "可"
radio8FalseLabel = "不可"
flag8 = tk.StringVar()
label8 = tk.Label(settingFrame, text=label8Title).grid(columnspan=3, row=14, column=0)
rdo8true = tk.Radiobutton(settingFrame, text=radio8TrueLabel, value=0, variable=flag8).grid(row=15, column=0,
                                                                                            sticky=tk.W + tk.E)
rdo8false = tk.Radiobutton(settingFrame, text=radio8FalseLabel, value=1, variable=flag8).grid(row=15, column=1,
                                                                                              sticky=tk.W + tk.E)
chk8 = tk.Checkbutton(settingFrame).grid(row=15, column=2, sticky=tk.W + tk.E)

# 元ファイル削除 row 16
label9Title = "全て成功した場合、元ファイルを削除する"
label9 = tk.Label(settingFrame, text=label9Title).grid(columnspan=2, row=16, column=0)
chk9 = tk.Checkbutton(settingFrame).grid(row=16, column=2)

# ファイルリストテーブル
fileTree = ttk.Treeview(folderListFrame)
fileTree["columns"] = (1, 2, 3)
fileTree["show"] = "headings"
fileTree.column(1, width=75)
fileTree.column(2, width=75)
fileTree.column(3, width=200)
fileTree.heading(1, text="ファイル名")
fileTree.heading(2, text="フォルダ名")
fileTree.heading(3, text="パス")
fileTree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# プログレスバーとスタートボタン
progressBar = ttk.Progressbar(progressFrame, orient=tk.HORIZONTAL, mode='determinate')
progressBar.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
startButton = ttk.Button(progressFrame, text="Start")
startButton.pack(side=tk.LEFT, fill=tk.BOTH)

# windowサイズ変更時の対応
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=2)

window.mainloop()

#
# window設定終了
#



if __name__ == '__main__':
    print("__main__")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
