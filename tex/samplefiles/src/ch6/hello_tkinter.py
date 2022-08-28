from tkinter import *

# ウィンドウを作成 --- (*1)
win = Tk()

# 描画のためキャンバスを作成 --- (*2)
cv = Canvas(win, width = 400, height = 300)
cv.pack() # ウィンドウ全体に載せる

# メインループを実行 --- (*3)
win.mainloop()


