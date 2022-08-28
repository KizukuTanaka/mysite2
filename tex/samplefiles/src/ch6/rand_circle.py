from tkinter import *

# ランダムな色を返す関数 --- (*1)
def random_color():
    # ランダムに色の配色を決定
    from random import randint 
    rnd = lambda : randint(0, 255)
    r = rnd()
    g = rnd()
    b = 255
    # HTMLの色形式に変換 --- (*2)
    f = "#{0:02x}{1:02x}{2:02x}"
    color = f.format(r, g, b)
    return color

# たくさんの円を描画する --- (*3)
def draw_circles():
    # 画面を初期化 --- (*4)
    cv.delete("all")
    # 繰り返し円を描画 --- (*5)
    for y in range(20):
        y1 = y * 20
        y2 = y1 + 20
        for x in range(30):
            x1 = x * 20
            x2 = x1 + 20
            # 円を描画
            color = random_color()
            cv.create_oval(x1, y1, x2, y2, 
                    fill=color, width=0)
    # 0.1秒後に再描画 --- (*6)
    win.after(100, draw_circles)

# ウィンドウとキャンバスを作成
win = Tk()
cv = Canvas(win, width=600, height=400)
cv.pack()
win.after(1, draw_circles) # 円を描画
win.mainloop()

