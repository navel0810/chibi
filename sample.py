import sys
from tkinter import Tk,ttk

root = Tk()
btnframe = ttk.Frame(root)
def button1_clicked():
    print('大吉')
    root.quit()

btn = ttk.Button(btnframe,text='占い結果')


btnframe.grid()
btn.grid()
