# -*- coding: utf-8 -*-
import random
import time


class TimeUtil:
    """
    Time工具类
    """

    @staticmethod
    def random_wait(start=5, end=10):
        """
        随机等待时间
        :param start:
        :param end:
        :return:
        """
        wait_time = random.randint(start, end)
        time.sleep(wait_time)
