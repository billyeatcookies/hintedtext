import tkinter as tk
from hintedtext import HintedText
from hintedentry import HintedEntry

root = tk.Tk()
text = HintedText(root, hint="Enter your text here")
text.pack()
entry = HintedEntry(root, hint="Enter your text here")
entry.pack()

root.mainloop()
