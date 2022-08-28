from drivegame_info import ginfo
from drivegame_map import create_map_line
from drivegame_draw import *
import tkinter.messagebox as msgbox

# ゲームの初期化処理 --- (*1)
def init_game():
    global win
    # ウィンドウやキャンバスの生成と、走行コースも生成
    win = create_window(ginfo)
    # キーボードイベントを設定 --- (*2)
    win.bind("<Left>", key_event_left)
    win.bind("<Right>", key_event_right)
    # ゲームを開始する --- (*3)
    game_loop()
    win.mainloop()

# カーソルキーを押した時の処理 --- (*4)
def key_event_left(e):
    if ginfo["car"] > 0:
        ginfo["car"] -= 1
def key_event_right(e):
    if ginfo["car"] <= ginfo["cols"] - 1:
        ginfo["car"] += 1

# ゲームループ --- (*5)
def game_loop():
    # 走行コースと自動車の描画
    draw_map(ginfo)
    win.title("ドライブゲーム スコア=" + str(ginfo["score"]))
    # ゲームオーバー判定 --- (*6)
    map_data = ginfo["map_data"]
    v = map_data[ginfo["rows"] - 2][ginfo["car"]]
    if v != 0: # 道路ではない
        msgbox.showinfo(
            title="ゲームオーバー",
            message="コースアウトしました\n" +
                    "スコア=" + str(ginfo["score"]))
        quit()
    # スコアを加算
    ginfo["score"] += 10
    # 過ぎた道路を消して上に新たな道路を足す --- (*7)
    del(map_data[ginfo["rows"] - 1])
    line = create_map_line(ginfo)
    map_data.insert(0, line)
    # 一定時間後に、再びこの関数を実行 --- (*8)
    win.after(100, game_loop)

if __name__ == "__main__": init_game()
