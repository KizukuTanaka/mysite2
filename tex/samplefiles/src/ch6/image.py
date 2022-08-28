from tkinter import *
from PIL import ImageTk, Image # --- (*1)

# ウィンドウとキャンバスを作成
win = Tk()
cv = Canvas(win, width=600, height=450)
cv.pack()

# 画像ファイルを読む --- (*2)
filename = "photo.jpg"
img = Image.open(filename)
print("size={0}x{1}".format(img.width, img.height))

# Tkinterで使えるように変換 --- (*3)
img_tk = ImageTk.PhotoImage(img)

# 画像を表示 --- (*4)
cv.create_image(0, 0, image=img_tk, anchor=NW)

# メインループを実行
win.mainloop()


