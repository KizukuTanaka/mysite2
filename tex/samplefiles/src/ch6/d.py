from tkinter import *

title_size = 20

def load_map_data():
    from maze_data import data
    return data

def draw_map(cv, data):
    rows = len(data)
    cols = len(data[0])
    for y in range(rows):
        y1 = y * title_size
        y2 = y1 * title_size
    for x in range(cols):
        y1 = y * title_size
        y2 = y1 * title_size

        p = data[y][x]

        if p == 0: color="white"
        if p == 1: color="#404040"
        if p == 2: color="red"
        if p == 3: color="blue"

        cv.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline="black",width=2)
def create_window(map_data, events = []):
    win = Tk()
    win.title("迷路")
    rows = len(map_data)
    cols = len(map_data[0])
    cv = Canvas(win,
                width=(cols*title_size),
                height=(rows*title_size))
    cv.pack()
    draw_map(cv, map_data)
    for func in events: func(cv, map_data)
    win.mainloop()
if __name__=="__main__":
    map_data = load_map_data()
    create_window(map_data)
         
        
        
        
        
