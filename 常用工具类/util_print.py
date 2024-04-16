# -*- coding: utf-8 -*-


from datetime import datetime


class Print:
    """
    Print函数工具类
    """

    @staticmethod
    def red(text):
        print(f"\033[31m" + f"[{Print.now_time()}] " + text + "\033[0m")

    @staticmethod
    def green(text):
        print("\033[32m" + f"[{Print.now_time()}] " + text + "\033[0m")

    @staticmethod
    def yellow(text):
        print(f"\033[33m" + f"[{Print.now_time()}] " + text + "\033[0m")

    @staticmethod
    def blue(text):
        print(f"\033[34m" + f"[{Print.now_time()}] " + text + "\033[0m")

    @staticmethod
    def magenta(text):
        print(f"\033[35m" + f"[{Print.now_time()}] " + text + "\033[0m")

    @staticmethod
    def cyan(text):
        print(f"\033[36m" + f"[{Print.now_time()}] " + text + "\033[0m")

    @staticmethod
    def now_time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def print(*args, **kwargs):
        print(f"[{Print.now_time()}]", *args, **kwargs)
