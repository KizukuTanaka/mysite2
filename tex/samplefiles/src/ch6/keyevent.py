from tkinter import *

# イベントを処理する関数
def key_event(e):
    print("キーを押しました")
    print(e)

# ウィンドウを作ってキーを監視
win = Tk()
win.bind("<Key>", key_event)
win.mainloop()

