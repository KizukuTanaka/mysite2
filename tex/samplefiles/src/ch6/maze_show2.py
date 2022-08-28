from tkinter import *
from maze_show import create_window

# CSV(タブ区切り)を読み込む
def load_map_from_tsv(filename):
    # ファイルを開く --- (*1)
    fp = open(filename, "rt", encoding="utf-8")
    tsv = fp.read()
    # TSVファイルを解析する
    rows = tsv.split("\n") # 改行で区切る --- (*2)
    result = []
    for line in rows:
        cols = line.split("\t") # タブで区切る --- (*3)
        if len(cols) <= 1: break
        cols = list(map(int, cols)) # ---(*4)
        result.append(cols)
    return result

if __name__ == "__main__":
    map_data = load_map_from_tsv("maze2.tsv")
    create_window(map_data)

