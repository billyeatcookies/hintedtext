import tkinter as tk
from hintedtext import HintedText

root = tk.Tk()
text = HintedText(root, hint="Enter your text here")
text.pack()
root.mainloop()
