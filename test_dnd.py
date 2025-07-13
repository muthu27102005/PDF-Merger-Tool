from tkinterdnd2 import TkinterDnD, DND_FILES
import tkinter as tk

root = TkinterDnD.Tk()
root.title("Drag and Drop Test")
root.geometry("400x200")

entry = tk.Entry(root, width=60)
entry.pack(pady=50)

entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', lambda e: entry.insert(0, e.data))

root.mainloop()
