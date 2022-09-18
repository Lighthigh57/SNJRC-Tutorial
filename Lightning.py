import random
import Command


# PlayerName = Light
class Lightning:
    def __init__(self):
        self.priority = []
        """priority = 優先度"""

        self.run = None
        """instance of Command class"""

        self.last = 0
        """last direction"""

        self.side = 0
        """My Client's side"""

        self.Check_Zone = 0
        """Interval of Map_Check"""

        self.Safety_Heart = 0
        """ModeChange border"""

        self.item = 0

    def main(self):
        turn = 0
        last = 0
        while True:
            self.priority = [0 for _ in range(9)]
            last = self.checker(last, run.get_ready())
            turn += 1

    # def map_Check(map):
    #     """マップを調べて取り残さない"""
    #     CUTX = 5
    #     CUTY = 5
    #
    #     result = [[0 for i in range(int(len(map[0]) / CUTX))] for j in range(int(len(map) / CUTY))]
    #
    #     for y in range(len(result)):
    #         temp = map[y * CUTY:y * CUTY + CUTY]
    #         for x in range(len(result[0])):
    #             check = []
    #             for i in temp:
    #                 check += i[x * CUTX:x * CUTX + CUTX]
    #             for j in check:
    #                 if j == 9:
    #                     result[y][x] += 1
    #
    #     ave = 0
    #     for law in result:
    #         for b in law:
    #             ave += b
    #     ave /= 9
    #     nice = []
    #     for y_in, y in enumerate(result):
    #         for x_in, x in enumerate(y):
    #             if x > ave:
    #                 nice += [y_in * 3 + x_in]
    #     print(nice)

    def solve_diagonal(self, target, com):
        """斜めに物が見えた時の処理"""
        if target < 3:  # Where this is for X
            y = 1
        else:
            y = 7
        if target == 0 or target == 6:  # Where this is for X
            x = 3
        else:
            x = 5
        if com == "avoid":  # if this is enemy
            self.priority[x] = -1
            self.priority[y] = -1
        else:  # if this is item
            self.priority[x] += 1
            self.priority[y] += 1

    def checker(self, current, ready_value) -> int:
        """敵いたら潰します(笑)"""
        global run

        for i in range(0, 9):  # Safe Command
            if ready_value[i] == 3:  # Can I get now?
                if i % 2 == 1:
                    self.priority[i] += 1
                else:
                    self.solve_diagonal(i, "get")
        # Danger Command
        for i in range(0, 9):
            if ready_value[i] == 1:  # Can I put there now?
                if i % 2 == 0:
                    self.solve_diagonal(i, "avoid")
                else:
                    run.move("put", i)
                    break
            if ready_value[i] == 2:  # There is a block?
                self.priority[i] = -2

        max_priority = self.priority[1]  # maximum value
        now_max = [1]  # direction index who it has maximum

        # find maximum value in priority list(look like search sort)
        for i in range(3, 8, 2):
            if max_priority < self.priority[i]:
                max_priority = self.priority[i]
                now_max = [i]
            elif max_priority == self.priority[i]:
                now_max += [i]

        if len(now_max) != 1:  # remove last place
            if (current == 1) and (7 in now_max):
                now_max.remove(7)
            elif (current == 3) and (5 in now_max):
                now_max.remove(5)
            elif (current == 5) and (3 in now_max):
                now_max.remove(3)
            elif (current == 7) and (1 in now_max):
                now_max.remove(1)
        if max_priority < 0:  # I should go to Danger Zone!!!
            run.move("look", 1)
            return 0
        else:
            goto = now_max[random.randint(0, len(now_max) - 1)]
            run.move("walk", goto)
        return goto


if __name__ == "__main__":
    run = Command.Command()  # Set Command instance
    Lightning().main()
