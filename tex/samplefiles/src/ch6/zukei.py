from tkinter import *

# ウィンドウとキャンバスを作成 
win = Tk()
cv = Canvas(win, width=400, height=300)
cv.pack()

# 円を描画 --- (*1)
cv.create_oval(
        120, 120, 240, 240, # 座標
        fill="red", # 塗色
        outline="green", width=2) # 枠線

# 多角形を描画 --- (*2)
cv.create_polygon(
        210, 290, 390, 290, 390, 140, # 座標
        fill="blue", # 塗色
        outline="red", width=2) # 枠線

# 長方形を描画 --- (*3)
cv.create_rectangle(
        10, 10, 130, 110, # 座標
        fill="green", # 塗色
        outline="red", width=2) # 枠線

# メインループを実行
win.mainloop()


