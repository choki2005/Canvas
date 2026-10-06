from tkinter import *

window = Tk()


canvas = Canvas(window, width=600, height=500, bg="skyblue")
canvas.pack()

# Ground
canvas.create_rectangle(0, 400, 600, 500, fill="green")

# House body
canvas.create_rectangle(180, 220, 420, 400, fill="lightyellow")

# Roof
canvas.create_polygon(150, 220, 300, 100, 450, 220, fill="red")

# Door
canvas.create_rectangle(270, 300, 330, 400, fill="brown")

# Door knob
canvas.create_oval(315, 350, 323, 358, fill="yellow")

# Left window
canvas.create_rectangle(205, 260, 255, 310, fill="lightblue")
canvas.create_line(230, 260, 230, 310, fill="black")
canvas.create_line(205, 285, 255, 285, fill="black")

# Right window
canvas.create_rectangle(345, 260, 395, 310, fill="lightblue")
canvas.create_line(370, 260, 370, 310, fill="black")
canvas.create_line(345, 285, 395, 285, fill="black")



# Title
canvas.create_text(300, 40, text="MY HOME",
                  font=("Arial", 24, "bold"), fill="darkblue")

window.mainloop()