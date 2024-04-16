# -*- coding: utf-8 -*-

import json

import requests


class WeChatRobot:
    """
    企业微信群机器人工具类
    """

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_text(self, content):
        """
        向企业微信群机器人推送文本消息
        """
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        return self._send(data)

    def send_markdown(self, content, title=None):
        """
        向企业微信群机器人推送 Markdown 格式的消息
        """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        if title:
            data["markdown"]["title"] = title
        return self._send(data)

    def send_news(self, title, description, picurl):
        """
        向企业微信群机器人推送 News 格式的消息
        """
        data = {
            "msgtype": "news",
            "news": {
                "articles": [
                    {
                        "title": f"{title}",
                        "description": f"{description}",
                        "url": f"{picurl}",
                        "picurl": f"{picurl}"
                    }
                ]
            }
        }
        return self._send(data)

    def _send(self, data):
        """
        发送消息的内部方法
        """
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        response = requests.post(self.webhook_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return True
        else:
            return False


# 创建 WeChatRobot 实例
robot = WeChatRobot(webhook_url="http://****")

# 使用示例：
if __name__ == "__main__":
    # 发送文本消息
    robot.send_text("Hello, World!")

    # 发送 Markdown 格式的消息
    markdown_content = f"""
    > **QQ号**：459377246
    > **手机号**：13888888888
    > **昵称**：无敌小旋风
    > **时间**：2023-08-31 10:51:24
    > **消息**：各种加急处理
"""
    robot.send_markdown(markdown_content)
