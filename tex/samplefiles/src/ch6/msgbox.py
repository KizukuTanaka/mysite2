from tkinter import *
import tkinter.messagebox as msgbox # 取り込む

# ウィンドウを表示しないようにする
win = Tk()
win.withdraw()

# ダイアログを表示
msgbox.showinfo(
        title="挨拶", 
        message="こんにちは。")

quit()
