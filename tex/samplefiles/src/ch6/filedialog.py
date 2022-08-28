# 必要なモジュールの取り込み
from tkinter import *
import tkinter.filedialog as filedlg
import tkinter.messagebox as msgbox

# ウィンドウを表示しないようにする
win = Tk()
win.withdraw()

# ファイルダイアログ(開く)
path = filedlg.askopenfilename()
msgbox.showinfo(message=path) # 読み取ったパス

# ファイルダイアログ(保存)
path = filedlg.asksaveasfilename()
msgbox.showinfo(message=path) # 読み取ったパス
quit()


