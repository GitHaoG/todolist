from PySide6 import QtWidgets

import ui
import utilities

# 考虑到程序可能会很大 编写一个建造者
class ToDoAppBuilder:
    def __init__(self):

        self.config = utilities.AppConfig()
        pass

    def add_config(self, file_path: str):
        self.config.loadConfig(file_path)
        return self

    def add_tools(self):
        return self

    def build(self):
        # 先进行配置 数据库连接字符串 大模型api-key 或者其他的一些别的什么东西
        configs = self.config.config()
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
    app_builder = ToDoAppBuilder()

    app = app_builder.build()

    root = ui.Qt_MainWindow()

    root.show()
    app.run()
    pass

if __name__ == "__main__":
    main()