import tkinter as tk
import tkinter.ttk as ttk
from .Tk_Styles.ButtonStyles import *

class Tk_InputBox(tk.Frame):
    """一个包含上侧 Text 控件 + 下侧固定高度按钮栏的复合组件。
    - Text 填充剩余空间，随窗口缩放自动调整
    - 底部按钮栏高度固定，不会因窗口缩小而被压缩
    - 还需要能够接收外部窗体的一个流
    """
    def __init__(self, master, **kwargs):
        """
        :param master: 父容器
        :param bottom_height: 底部按钮栏的固定高度（像素）
        :param kwargs: 额外的 Frame 参数（如 bg, width 等）
        """
        super().__init__(master, **kwargs)

        # 使用 Grid 布局：第 0 行（Text）可扩展，第 1 行（按钮栏）固定高度
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, minsize=40)
        self.grid_columnconfigure(0, weight=1)

        # Text 控件
        self.input_box = tk.Text(self)
        self.input_box.grid(row=0, column=0, sticky="nsew")

        # 底部按钮栏
        self.bottom_frame = tk.Frame(self, height=40, bg="lightgray")
        self.bottom_frame.grid(row=1, column=0, sticky="ew")
        self.bottom_frame.grid_propagate(False)  # 保持固定高度，不被内部按钮撑大

        self.input_box.bind('<Return>', self.commit_text)
        self.add_button("提交",self.commit_text_for_btn)
        pass

    def add_button(self, text, command, **btn_kwargs):
        """在底部栏从左至右添加一个按钮。

        :param text: 按钮文本
        :param command: 回调函数
        :param btn_kwargs: 额外的 tk.Button 参数
        :return: 创建的 Button 对象
        """

        btn = ttk.Button(self.bottom_frame, text=text, command=command,
                         style=configure_fluent__style_for_btn(),
                        **btn_kwargs)
        btn.pack(side="right", padx=5, pady=5)
        return btn

    def commit_text_for_btn(self) -> None:
        text_to_commit = self.input_box.get("1.0",tk.END)
        self.input_box.delete("1.0",tk.END)
        self.input_box.mark_set("insert", "1.0")  # 光标回到起点
        self.input_box.focus_set()

        print(repr(text_to_commit))
        # 打断事件向Text中写入文本
        return

    def commit_text(self, event) -> str:
        text_to_commit = self.input_box.get("1.0", tk.END)
        self.input_box.delete("1.0", tk.END)
        self.input_box.mark_set("insert", "1.0")  # 光标回到起点
        self.input_box.focus_set()

        print(repr(text_to_commit))
        # 打断事件向Text中写入文本
        return "break"