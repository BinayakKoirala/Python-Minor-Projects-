import tkinter as tk
from time import strftime

def theme():
    frame = tk.Frame(root, bg="#000000")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    lbl_2 = tk.Label(frame, font=('Arial', 40, 'bold'),
                     background='#000000', foreground='white')
    lbl_2.pack(anchor="center")

    def time():
        string = strftime('%I:%M:%S %p')
        lbl_2.config(text=string)
        lbl_2.after(1000, time)
    time()


root = tk.Tk()
root.title("Binayak's Digital-Clock")
canvas = tk.Canvas(root, height=140, width=400)
canvas.pack()

frame = tk.Frame(root, bg='#000000')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
lbl = tk.Label(frame, font=('Arial', 40, 'italic'),
                     background='#000000', foreground='white')
lbl.pack(anchor="center")

def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
time()

root.mainloop()