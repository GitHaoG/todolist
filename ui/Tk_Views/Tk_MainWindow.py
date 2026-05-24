import tkinter as tk

from .Tk_ChatLog import Tk_ChatLog
from .Tk_InputBox import Tk_InputBox

class Tk_MainWindow(tk.Tk):
    """
    主窗体
    """
    def __init__(self):
        super().__init__()
        # 先初始化窗体所有的资源
        self.minsize(300,600)
        self.geometry("300x600")

        # 这里进行布局

        self.chatlog = Tk_ChatLog(self)
        self.chatlog.place(relx=0,rely=0,relwidth=1,relheight=0.7)

        self.input_box = Tk_InputBox(self)
        self.input_box.place(relx=0,rely=0.71,relwidth=1,relheight=0.29)

        pass


