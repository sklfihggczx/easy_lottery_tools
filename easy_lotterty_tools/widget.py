import sys
from enum import Enum

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from layout_parser import QtComponent
from lottery_graphic import Graphic


class RollStatus(Enum):
    STOP = 0
    START = 1
    PAUSE = 2


class MainWidget(QMainWindow):
    cur_idx = 0
    cur_status = RollStatus.STOP

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lottery Machine")
        self.resize(1000, 600)

        self.component = QtComponent(self, "./assets/layout")

        self.component.components['be-chosen'].setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.component.components['to-choose'].setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )

        try:
            self.shell = Graphic(self)
        except FileNotFoundError:
            QMessageBox.information(self, "文件无法打开", "找不到 result.csv 文件，请先下载排名！")
            sys.exit(1)

        self.timer = QTimer(self)
        self.timer.setInterval(int(self.shell.inter * 1000))

        self.fill_to_choose()
        self.signals_slots()

        self.show()

    def fill_to_choose(self):
        for k, v in self.shell.result.items():
            self.component.components["to-choose"].append(f"{k}\t[{v}]")

    def signals_slots(self):
        self.component.components["object"].textChanged.connect(self.ready_to_roll)
        self.component.components["roll-button"].clicked.connect(
            lambda: self.switch_roll(
                self.component.components["object"].text(),
                self.component.components["count"].value()
            )
        )
        self.timer.timeout.connect(self.next_roll)

    def ready_to_roll(self, s: str):
        self.component.components["roll-button"].setEnabled(not s == "")
        self.shell.show_prompt("就绪！")

    def switch_roll(self, name: str, k: int):
        match self.cur_status:
            case RollStatus.STOP:
                self.timer.start()
                self.lock_input()

                self.component.components["roll-button"].setText("停止！")
                self.component.components["be-chosen"].append(name + "：")
                self.shell.show_prompt(f"正在抽取：{name} 第 {1} / {k} 个")

                self.cur_idx = 1

                self.cur_status = RollStatus.START

            case RollStatus.START:
                self.timer.stop()

                winner = self.component.components["main-label"].text()
                self.shell.show_prompt(f"正在抽取：{name} 第 {self.cur_idx} / {k} 个，抽中了 {winner}")
                self.shell.delete(winner)

                self.component.components["be-chosen"].append("    " + winner)

                self.cur_idx += 1

                if self.cur_idx <= k:
                    self.component.components["roll-button"].setText("继续！")
                    self.cur_status = RollStatus.PAUSE
                else:
                    self.component.components["roll-button"].setText("开始！")
                    self.cur_status = RollStatus.STOP
                    self.reset_input()
                    self.unlock_input()

            case RollStatus.PAUSE:
                self.timer.start()

                self.component.components["roll-button"].setText("停止！")
                self.shell.show_prompt(f"正在抽取：{name} 第 {self.cur_idx} / {k} 个")

                self.cur_status = RollStatus.START

    def next_roll(self):
        try:
            self.component.components["main-label"].setText(self.shell.roll("", 0))
        except IndexError:
            QMessageBox.information(self, "人数已达上限", "所有的人都领到奖品啦~")
            self.timer.stop()
            self.cur_status = RollStatus.STOP
            self.reset_input()
            self.unlock_input()

    def lock_input(self):
        self.component.components["object"].setEnabled(False)
        self.component.components["count"].setEnabled(False)

    def unlock_input(self):
        self.component.components["object"].setEnabled(True)
        self.component.components["count"].setEnabled(True)

    def reset_input(self):
        self.component.components["count"].setValue(1)
        self.component.components["object"].setText("")
        self.component.components["roll-button"].setText("开始！")
