from loguru import logger
from openai import OpenAI, OpenAIError

def assistant_message(content: str) -> dict:
    return {"role": "assistant", "content": content}

def user_message(content: str) -> dict:
    return {"role": "user", "content": content}

class ChatClient:
    def __init__(self, base_url: str, model_name: str, api_key: str, history_messages: list = None):
        """
        聊天用的类
        :param base_url: ai模型的api链接
        :param model_name: 要使用的模型名
        :param api_key: api key
        :param history_messages: 历史对话记录
        """
        self.__model_name = model_name
        self.__api_key = api_key
        self.__base_url = base_url
        self.__openai_client = OpenAI(api_key=self.__api_key, base_url=self.__base_url)

        # __messages.append() 不能处理消息太多的情况 这里就可以通过属性做一些手段

        self.__messages: list
        if history_messages is None:
            self.__messages = []
        else:
            self.__messages = history_messages
        return

    def set_prompt(self, prompt_content: str) -> str:
        # 传递提示词
        prompt_message = {"role": "system", "content": prompt_content}
        assistant_response = self.send_message(prompt_message)
        self.__messages.append(assistant_response)
        return assistant_response["content"]

    def user_query(self, query: str) -> dict:
        # 用户发送消息 并且添加到历史消息里面
        user_query = user_message(query)
        self.__messages.append(user_query)

        # ai响应结果 返回出去，并且添加到历史消息里面
        ai_response = self.send_message(user_query)
        self.__messages.append(ai_response)
        return ai_response

    def send_message(self, message: dict) -> dict:
        # 发送消息给ai
        self.__messages.append(message)
        try:
            response = self.__openai_client.chat.completions.create(
                model=self.__model_name,
                messages=self.__messages,
            )
            content = response.choices[0].message.content
            if content is None:
                content = ""
            return assistant_message(content)
        except OpenAIError as e:
            logger.error(e)
            return assistant_message("")
