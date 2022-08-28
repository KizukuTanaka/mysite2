from tkinter import *

# ウィンドウを作成 --- (*1)
win = Tk()

# 描画のためキャンバスを作成 --- (*2)
cv = Canvas(win, width=380, height=380)
cv.pack() # ウィンドウ全体に載せる

# 碁盤を描画する --- (*3)
for i in range(19):
    # 縦の線
    y = i * 20
    cv.create_line(0, y, 380, y, fill="black", width=2)
    # 横の線
    x = i * 20
    cv.create_line(x, 0, x, 380, fill="black", width=2)

# メインループを実行 --- (*4)
win.mainloop()


