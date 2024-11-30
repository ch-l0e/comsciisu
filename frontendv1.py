import tkinter as tk

root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("600x400")

def exitbutton():
    def closeapp():
        root.destroy()
    close = tk.Button(root, text = "exit", command = closeapp)
    close.place(relx = 0.5, rely = 0.9, anchor = "center")

def clearwindow():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == "exit":
            continue
        if isinstance(widget, tk.Button) and widget.cget("text") == "next":
            continue
        widget.destroy()

def colorschemes():
    q1 = tk.Label(root, text = "Analogous or Complementary colours?", font = ("Times New Roman", 10))
    q1.place(relx = 0.0333, rely = 0.1)

    def analogous():
        clearwindow()
        picked = tk.Label(root, text = "Analogous colors selected!")
        picked.pack(side = "top", pady = 20)
    analogous_pick = tk.Button(root, text = "Analogous", command = analogous)
    analogous_pick.place(relx = 0.4, rely = 0.1)

    def complementary():
        clearwindow()
        picked = tk.Label(root, text = "Complementary colors selected!")
        picked.pack(side = "top", pady = 20)
    complementary_pick = tk.Button(root, text = "Complementary", command = complementary)
    complementary_pick.place(relx = 0.53, rely = 0.1)

def variation():
    q2 =tk.Label(root, text = "Vibrant, dull or pastel colors?", font = ("Times New Roman", 10))
    q2.place(relx = 0.0333, rely = 0.1)

    def vibrant():
        clearwindow()
        picked = tk.Label(root, text = "vibrant colors selected!")
        picked.pack(side = "top", pady = 20)
    vibrant_pick = tk.Button(root, text = "Vibrant", command = vibrant)
    vibrant_pick.place(relx = 0.35, rely = 0.1)

    def dull():
        clearwindow()
        picked = tk.Label(root, text = "dull colors selected!")
        picked.pack(side = "top", pady = 20)
    dull_pick = tk.Button(root, text = "Dull", command = dull)
    dull_pick.place(relx = 0.45, rely = 0.1)

    def pastel():
        clearwindow()
        picked = tk.Label(root, text = "pastel colors selected!")
        picked.pack(side = "top", pady = 20)
    pastel_pick = tk.Button(root, text = "Pastel", command = pastel)
    pastel_pick.place(relx = 0.52, rely = 0.1)

    nextbutton.config(command = (clearwindow and colors))

def colors():
    canvas = tk.Canvas(root, width = 600, height = 200)
    canvas.pack(pady = 20)
    red = canvas.create_rectangle(20, 20, 80, 80, fill = "red", outline = "")
    orange = canvas.create_rectangle(100, 20, 160, 80, fill = "orange", outline = "")
    yellow = canvas.create_rectangle(180, 20, 240, 80, fill = "yellow", outline = "")
    green = canvas.create_rectangle(260, 20, 320, 80, fill = "green", outline = "")
    blue = canvas.create_rectangle(340, 20, 400, 80, fill = "blue", outline = "")
    purple = canvas.create_rectangle(420, 20, 480, 80, fill = "purple", outline = "")
    q3 = tk.Label(root, text = "Select favourite:", font = ("Times New Roman", 10))
    q3.place(relx = 0.0333, rely = 0.5,)

    def select_red():
        clearwindow()
        color_picked = tk.Label(root, text = "red selected!", font = ("Times New Roman", 10))
        color_picked.pack(pady = 10)
    pick_red = tk.Button(root, text = "Red", command = select_red)
    pick_red.place(relx = 0.2, rely = 0.5)

    def select_orange():
        clearwindow()
        color_picked = tk.Label(root, text = "Orange selected!", font = ("Times New Roman", 10))
        color_picked.pack(pady = 10)
    pick_orange = tk.Button(root, text = "Orange", command = select_orange)
    pick_orange.place(relx = 0.27, rely = 0.5)

    def select_yellow():
        clearwindow()
        color_picked = tk.Label(root, text = "Yellow selected!", font = ("Times New Roman", 10))
        color_picked.pack(pady = 10)
    pick_yellow = tk.Button(root, text = "Yellow", command = select_yellow)
    pick_yellow.place(relx = 0.37, rely = 0.5)

    def select_green():
        clearwindow()
        color_picked = tk.Label(root, text = "Green selected!", font = ("Times New Roman", 10))
        color_picked.pack(pady = 10)
    pick_green = tk.Button(root, text = "Green", command = select_green)
    pick_green.place(relx = 0.46, rely = 0.5)

    def select_blue():
        clearwindow()
        color_picked = tk.Label(root, text = "Blue selected!", font = ("Times New Roman", 10))
        color_picked.pack(pady = 10)
    pick_blue = tk.Button(root, text = "Blue", command = select_blue)
    pick_blue.place(relx = 0.545, rely = 0.5)

    def select_purple():
        clearwindow()
        color_picked = tk.Label(root, text = "Purple selected!", font = ("Times New Roman", 10))
        color_picked.pack(pady = 10)
    pick_purple = tk.Button(root, text = "Purple", command = select_purple)
    pick_purple.place(relx = 0.62, rely = 0.5)

exitbutton()
nextbutton = tk.Button(root, text = "next", command = (clearwindow and variation))
nextbutton.place(relx = 0.85, rely = 0.9, anchor = "e")
colorschemes()

root.mainloop()