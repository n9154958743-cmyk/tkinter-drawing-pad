from tkinter import *

top = Tk()
top.geometry("700x500")
top.title("Drawing Pad")

brush_colour = "black"
brush_size = 3
mode = "draw"

# --- Left Frame for Colors ---
color_frame = Frame(top)
color_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

def set_colour(col):
    global brush_colour, mode
    brush_colour = col
    mode = "draw"
    status.config(text=f"Brush: {brush_colour}, Size: {brush_size}")

Button(color_frame, text="Red", command=lambda: set_colour("red")).pack(pady=5)
Button(color_frame, text="Blue", command=lambda: set_colour("blue")).pack(pady=5)
Button(color_frame, text="Green", command=lambda: set_colour("green")).pack(pady=5)
Button(color_frame, text="Yellow", command=lambda: set_colour("yellow")).pack(pady=5)
Button(color_frame, text="Eraser", command=lambda: set_colour("white")).pack(pady=5)

# --- Right Frame for Sizes ---
size_frame = Frame(top)
size_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)

def set_size(sz):
    global brush_size
    brush_size = sz
    status.config(text=f"Brush: {brush_colour}, Size: {brush_size}")

Button(size_frame, text="Small", command=lambda: set_size(3)).pack(pady=5)
Button(size_frame, text="Medium", command=lambda: set_size(6)).pack(pady=5)
Button(size_frame, text="Large", command=lambda: set_size(10)).pack(pady=5)
Button(size_frame, text="Clear All", command=lambda: c_obj.delete("all")).pack(pady=5)

# --- Canvas in the middle ---
c_obj = Canvas(top, bg="white", width=500, height=350)
c_obj.pack(pady=10)

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    c_obj.create_oval(x1, y1, x2, y2, fill=brush_colour, outline=brush_colour)

c_obj.bind("<B1-Motion>", paint)

# --- Exit button at bottom ---
Button(top, text="EXIT", command=top.destroy).pack(side=BOTTOM, pady=10)

# --- Status bar ---
status = Label(top, text=f"Brush: {brush_colour}, Size: {brush_size}", anchor="w")
status.pack(side=BOTTOM, fill=X)

top.mainloop()
