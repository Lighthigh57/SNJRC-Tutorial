import CHaser


class Command:
    def __init__(self):
        self.run = CHaser.Client()
        self.ready_OK = False
        self.side = self.run.side

    def move(self, com, dir):
        """
        各種行動を起こします。 Get_ready忘れないで！
        :param com: アクションの名前
        :type com: str
        :param dir: 方向を指定。get_readyをした時のインデックスの位置で指定してね。
        :type dir: int
        """

        result = [0 for _ in range(9)]

        if not self.ready_OK:  # if didn't get_ready()
            self.get_ready()
            print("Warning!:You didn't get_ready().")

        if com == "put":
            if dir == 1:
                result = self.run.put_up()
            if dir == 7:
                result = self.run.put_down()
            if dir == 3:
                result = self.run.put_left()
            if dir == 5:
                result = self.run.put_right()

        if com == "walk":
            if dir == 1:
                result = self.run.walk_up()
            if dir == 7:
                result = self.run.walk_down()
            if dir == 3:
                result = self.run.walk_left()
            if dir == 5:
                result = self.run.walk_right()

        if com == "look":
            if dir == 1:
                result = self.run.look_up()
            if dir == 7:
                result = self.run.look_down()
            if dir == 3:
                result = self.run.look_left()
            if dir == 5:
                result = self.run.look_right()

        if com == "search":
            if dir == 1:
                result = self.run.search_up()
            if dir == 7:
                result = self.run.search_down()
            if dir == 3:
                result = self.run.search_left()
            if dir == 5:
                result = self.run.search_right()

        print(com + " " + str(dir))
        self.ready_OK = False

        return result

    def get_ready(self):
        """Lunch get_ready and return map."""
        self.ready_OK = True
        result = self.run.get_ready()
        return result
