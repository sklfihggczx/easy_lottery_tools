import abc
import importlib.util

import csv_reader


class LotteryBase(metaclass=abc.ABCMeta):
    def __init__(self):
        self.inter = 0.01
        self.show_prompt("读取成绩...")
        self.result = csv_reader.get_result_map("result.csv")
        self.show_prompt("就绪！")
        self.final = {}

    @abc.abstractmethod
    def show_prompt(self, string, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, user):
        pass

    @abc.abstractmethod
    def roll(self, name, k):
        pass

    @abc.abstractmethod
    def publish(self):
        pass


find_pyqt = importlib.util.find_spec("PyQt6.QtWidgets") is not None
