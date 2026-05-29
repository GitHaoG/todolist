import json
from json import dumps

# 实现扁平化的 json 配置结果
class AppConfig:
    def __init__(self):
        self.configs = dict()
        return

    def loadConfig(self, file_path: str):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        # 递归地 处理 data 将其扁平化

        return self

    def config(self) -> dict:
        # 这里需要做一个检查，看看程序必须使用的配置字段是否进行了初始化
        
        return self.configs