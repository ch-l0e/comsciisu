import tkinter as tk

root = tk.Tk()
root.title("display")
root.geometry("600x400")

def exitbutton():
    def closeapp():
        root.destroy()
    close = tk.Button(root, text = "exit", command = closeapp)
    close.place(relx = 0.5, rely = 0.9, anchor = "center")

def colors():
    canvas = tk.Canvas(root, width = 600, height = 200)
    canvas.pack(pady = 20)
    c1 = canvas.create_rectangle(20, 20, 80, 80, fill = "#3c692d", outline = "")
    c2 = canvas.create_rectangle(100, 20, 160, 80, fill = "#8c3b88", outline = "")
    c3 = canvas.create_rectangle(180, 20, 240, 80, fill = "#4caf50", outline = "")
    c4 = canvas.create_rectangle(260, 20, 320, 80, fill = "#8f5bd2", outline = "")
    c5 = canvas.create_rectangle(340, 20, 400, 80, fill = "#69a4f4", outline = "")

colors()
exitbutton()

root.mainloop()