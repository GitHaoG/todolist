import tkinter as tk

from enum import Enum


class MessageType(Enum):
    """
    这个枚举是用来 进行不同的List元素进行样式调整
    """
    USER = 1
    AI_AGENT = 2

class Tk_ChatLog(tk.Listbox):
    """
    聊天记录列表控件，根据消息类型为条目配置不同颜色样式，呈现类似聊天对话框的效果。
    TODO: 能否insert一个控件？
    """

    # 预定义消息类型样式：前景色、背景色、选中背景色
    MESSAGE_STYLES = {
        MessageType.USER: {
            'fg': '#000000',  # 纯黑文字
            'bg': '#C8E6C9',  # 较深的淡绿背景
            'selectbackground': '#81C784'  # 选中时的绿色
        },
        MessageType.AI_AGENT: {
            'fg': '#000000',  # 纯黑文字
            'bg': '#BBDEFB',  # 较深的淡蓝背景
            'selectbackground': '#64B5F6'  # 选中时的蓝色
        }
    }

    def __init__(self, master):
        super().__init__(master)
        # 可根据需要在此处添加其他初始化配置，例如字体、宽度等
        self.insert_message("nihao", MessageType.USER)
        self.insert_message("nihao", MessageType.AI_AGENT)
        self.insert_message("nihao", MessageType.USER)
        self.insert_message("nihao", MessageType.AI_AGENT)

    def insert_message(self, content: str, msg_type: MessageType) -> None:
        """
        向聊天日志中插入一条消息，并根据消息类型应用预定义样式。

        :param content: 消息文本
        :param msg_type: 消息类型，使用 MessageType 枚举值
        """
        # 记录插入前的条目数量，该值即为新条目的索引
        index = self.size()
        # 插入文本到末尾
        self.insert(tk.END, content)
        # 获取对应的样式字典
        style = self.MESSAGE_STYLES.get(msg_type, {})
        # 逐项应用样式 (fg, bg, selectbackground 等)
        for key, value in style.items():
            self.itemconfig(index, **{key: value})
