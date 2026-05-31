"""
这个类型是用来提供程序配置信息的
"""
from loguru import logger
from json import load


def flatten_to_dict(src: dict, des: dict, fore_name: str = "") -> dict:
    """
    扁平化src，方便后面索引配置使用 而且也方便配置覆盖
    :param src: json源
    :param des: copy到的目标
    :param fore_name: 配置源的顶层名 会被这样使用 fore_name:key
    :return: 合并的配置结果
    """
    keys_temp = src.keys()

    for key in keys_temp:
        if type(src[key]) == dict:
            flatten_to_dict(src[key], des, f"{fore_name}:{key}")
        else:
            des[f"{fore_name}:{key}"] = src[key]
    return des


class AppConfig:
    """
    提供应用程序的配置，像是 api_key 数据库链接字符串 什么的
    """
    def __init__(self, if_raise: bool = False) -> None:
        self.__if_raise = if_raise
        self.__configs = dict()
        pass

    def add_json_config(self, file: str):

        try:
            with open(file, "r") as f:
                config_in_json = load(f)
                f.close()

            # 处理读文件时可能的错误
        except FileNotFoundError as e:
            if self.__if_raise:
                raise e
            else:
                logger.warning(f"文件没有找到: {e}")
                return self
        except TypeError as te:
            if self.__if_raise:
                raise te
            else:
                logger.error(f"转换json格式时出现错误: {te}")
                return self

        # 扁平化这个配置
        flatten_to_dict(config_in_json, self.__configs)
        return self

    def get_value(self, *args):
        try:
            # ":{arg1}:{arg2}"
            key = f":{':'.join(args)}"
            value = self.__configs[key]
            return value
        except KeyError as ke:
            if self.__if_raise:
                raise ke
            else:
                return None

    def get_configs(self):
        return self.__configs