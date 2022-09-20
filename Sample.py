from Command import Command


def main():
    runner = Command()
    side = runner.side
    wall_max = 0
    runner.get_ready()
    if side == 0:
        value = runner.move("search", 3)

        for i, info in enumerate(value):
            if info != 2:
                wall_max = i

        print(wall_max)

        walked = -1
        while wall_max > walked:
            print(walked)
            value = runner.get_ready()
            if value[3] != 2:
                runner.move("walk", 3)
                walked += 1
            elif value[1] != 2:
                runner.move("walk", 1)
            elif value[7] != 2:
                runner.move("walk", 7)
            else:
                runner.move("walk", 5)

    else:
        value = runner.move("search", 5)

        for i, info in enumerate(value):
            if i != 2:
                pass


if __name__ == "__main__":
    main()
