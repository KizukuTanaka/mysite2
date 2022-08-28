from tkinter import *
import tkinter.messagebox as msgbox

def main():
    # ウィンドウとキャンバスを作成 --- (*1)
    win = Tk()
    cv = Canvas(win, width=400, height=300)
    cv.pack()
    # イベントを設定 --- (*2)
    cv.bind("<1>", canvas_click)
    win.mainloop()

# クリックした時に実行するイベント --- (*3)
def canvas_click(e):
    mx = e.x # マウスのX座標
    my = e.y # マウスのY座標
    # 円を描画
    cv.create_oval(
            mx - 10, my - 10, mx + 10, my + 10,
            fill="red")
main()
