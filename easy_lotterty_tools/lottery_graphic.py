import random

from kernel import LotteryBase


class Graphic(LotteryBase):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

    def show_prompt(self, string, **kwargs):
        self.parent.statusBar().showMessage(string)

    def delete(self, user) -> bool:
        if user in self.result:
            self.result.pop(user)
            return True
        else:
            self.show_prompt(f"用户 {user} 不存在")
            return False

    def roll(self, _, __):
        users = []
        probs = []
        for user in self.result:
            users.append(user)
            probs.append(self.result[user])
        cur = random.choices(users, probs, k=1)[0]
        return cur

    def publish(self):
        pass
