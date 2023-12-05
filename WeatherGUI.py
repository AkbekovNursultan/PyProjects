import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height = 600, width = 600)
canvas.pack()

frame = tk.Frame(root, bg = 'gold')
frame.place(relx = 0, rely = 0, relwidth = 0.5, relheight = 0.5)

button = tk.Button(frame, text = 'Wow', bg = 'cyan', fg = 'pink')
button.pack()

label = tk.Label(frame, text = 'Sus', bg = 'yellow')
label.pack()

entry = tk.Entry(frame, bg = 'lime')
entry.pack()

root.mainloop()