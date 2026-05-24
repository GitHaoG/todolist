import tkinter as tk

class Tk_InputBox(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # 这玩意分两个部分
        # 上面是输入，下面是按钮
        self.input_box = tk.Text(self, font=("微软雅黑", 12), bg="#F0F8FF")
        self.input_box.place(relx=0,rely=0,relwidth=1,relheight=1, in_=self)

        self.input_box.bind('<Return>', self.commit_text)
        pass

    def commit_text(self, event) -> str:
        text_to_commit = self.input_box.get("1.0",tk.END)
        self.input_box.delete("1.0",tk.END)
        self.input_box.mark_set("insert", "1.0")  # 光标回到起点
        self.input_box.focus_set()

        print(text_to_commit)
        # 打断事件向Text中写入文本
        return "break"