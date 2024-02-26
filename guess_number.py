def guess_number(name="Player"):
    import random

    game_count = 0
    win_count = 0
    while True:
        try:
            number = random.randint(1, 3)
            guess = int(input("请输入1、2或3：\n\n"))
            print(f"{name}, 你猜的数字是{guess}")
            if guess == number:
                print(f"感谢您，猜对了！")
                win_count += 1
            else:
                print(f"猜错了！再试试吧！")
                print(f"{name}, 正确的数字是{number}")
            game_count += 1
            print(
                f"你的游戏次数是{game_count}，胜利次数是{win_count}，获胜率是{(win_count / game_count) * 100:.2f}%。"
            )
            playagain = str(input("还要再玩一次？输入q退出，输入其他任意键继续\n\n"))
            if playagain.lower() == "q":
                print("谢谢参与！")
                print(
                    f"{name}看看你的游戏记录吧！\n游戏次数是{game_count}，胜利次数是{win_count}，获胜率是{(win_count / game_count) * 100:.2f}%。"
                )
                break
        except ValueError:
            print("输入错误，请输入1、2或3。")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="猜数字游戏，请输入1、2、3中的某一个数字"
    )

    parser.add_argument("-n", "--name", metavar="name", type=str, help="玩家姓名")
    args = parser.parse_args()
    name = args.name
    if not name:
        name = "玩家"
    print(f"欢迎{name}来到猜数字游戏！")
    guess_number(name)
