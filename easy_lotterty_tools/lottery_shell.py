import random
import time

import writer

from kernel import LotteryBase


class Shell(LotteryBase):
    def __init__(self):
        super().__init__()
        self.show_result()
        self.run()

    def run(self):
        flag = True
        while flag:
            print(">>> ", end="")
            cmds = input().split()
            if len(cmds) == 1 and cmds[0] == 'quit':
                flag = False
            elif len(cmds) == 1 and cmds[0] == 'info':
                self.show_result()
            elif len(cmds) == 2 and cmds[0] == 'del':
                user = cmds[1]
                self.delete(user)
            elif len(cmds) == 3 and cmds[0] == 'roll':
                name = cmds[1]
                num = int(cmds[2])
                self.roll(name, num)
            elif len(cmds) == 1 and cmds[0] == 'pub':
                self.publish()
            else:
                print("命令错误")

    def show_result(self):
        for r in self.result:
            print("%-20s%-4.1f" % (r, self.result[r]))

    def delete(self, user):
        if user in self.result:
            self.result.pop(user)
        else:
            print("用户不存在")

    def roll(self, name, k):
        lucky_dogs = []
        for i in range(k):
            print(f"第{i + 1}位获得{name}的同学是:")
            users = []
            probs = []
            for user in self.result:
                users.append(user)
                probs.append(self.result[user])
            try:
                while True:
                    cur = random.choices(users, probs, k=1)[0]
                    writer.refresh()
                    writer.output("    " + cur)
                    time.sleep(self.inter)
            except KeyboardInterrupt as e:
                writer.refresh()
                writer.output("    " + cur + "\n")
                lucky_dogs.append(cur)
                self.delete(cur)
        print("恭喜以下同学:")
        print("    ", end="")
        for dog in lucky_dogs:
            print(dog, end="  ")
        self.final[name] = lucky_dogs
        print()

    def publish(self):
        for name in self.final:
            print(f"{name}:\n    ", end="")
            for user in self.final[name]:
                print(user, end="  ")
            print("")

    def show_prompt(self, string, **kwargs):
        print(string, **kwargs)

