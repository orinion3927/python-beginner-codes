import tkinter as tk

WIDTH, HEIGHT = 999, 999
root = tk.Tk()
root.title("test")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
def draw_square(x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
def clear_canvas():
    canvas.delete("all")
root.mainloop()
