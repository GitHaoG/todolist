import sys
import ui
import utilities
import traceback

from PySide6 import QtWidgets
from loguru import logger

# 考虑到程序可能会很大 编写一个建造者
class ToDoAppBuilder:
    def __init__(self):
        self.config = utilities.AppConfig()
        pass

    def add_config(self, file_path: str):
        self.config.add_json_config(file_path)
        return self

    def add_tools(self):
        return self

    def build(self):
        # 先进行配置 数据库连接字符串 大模型api-key 或者其他的一些别的什么东西
        configs = self.config.get_configs()
        # 加载 agent tools

        # 传递给 ToDoApp
        return ToDoApp(configs)

class ToDoApp(QtWidgets.QApplication):
    def __init__(self, configs: dict):
        super().__init__()
        self.config = configs
        pass

    # 这个函数，先定义为同步的 之后再看是不是需要重构为异步的
    def run(self):
        self.exec()

def main() -> None:
    # ui.MaterialStyles.configure_material_style_for_btn()
    # root_window = ui.Tk_MainWindow()
    # root_window.mainloop()
    try:
        logger.info("构建App类")
        app_builder = ToDoAppBuilder()

        app = app_builder.build()

        root = ui.Qt_MainWindow()

        logger.info("启动主窗体")
        root.show()

        logger.info("程序运行")
        app.run()
    except Exception as e:
        logger.error(f"Error: {e}, with: {traceback.format_exc()}")
    return

def chat_demo():
    from agent import chat

    app_config = utilities.AppConfig()
    app_config.add_json_config("appsettings.json")
    logger.remove()
    logger.add(sys.stdout, level="INFO")

    logger.info("加载程序配置")
    # 进行模型配置
    deepseek_api_key = app_config.get_value("models", "deepseek-v4-flash", "api_key")
    chat_client = chat.ChatClient(
        model_name="deepseek-v4-flash",
        api_key=deepseek_api_key,
        base_url="https://api.deepseek.com"
    )

    # 流程像是这样 开一个新对话 -> 进入循环
    # 这个可能放进循环里面更合适
    print("输入提示词 >> ", end=" ")
    input_prompt = input()
    if input_prompt == "q":
        return

    if input_prompt == "":
        return

    res = chat_client.set_prompt(input_prompt)
    logger.info(res)

    while True:
        logger.info("输入内容进行对话，输入q就会结束程序")

        print("请输入内容 >> ", end="")
        input_content = input()
        if input_content == "q":
            break
        response_message = chat_client.user_query(input_content)
        logger.info(response_message)

if __name__ == "__main__":
    chat_demo()
    pass
