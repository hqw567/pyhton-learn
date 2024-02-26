from guess_number import guess_number
from rps8 import play_game


def arcade(name="玩家"):
    choice_game = ""
    while True:
        choice_game = input(
            f"{name}, 请选择你需要玩的游戏：\n1. 猜数字\n2. 石头剪刀布\nq. 退出\n"
        )

        if choice_game not in ["1", "2", "q"]:
            print("输入错误，请重新输入！")
            continue
        if choice_game == "1":
            guess_number(name)
        elif choice_game == "2":
            play_game(name)
        elif choice_game.lower() == "q":
            print("谢谢参与！")
            break


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="游戏中心")

    parser.add_argument("-n", "--name", metavar="name", type=str, help="玩家姓名")
    args = parser.parse_args()
    name = args.name
    if not name:
        name = "玩家"
    print(f"欢迎{name}来到游戏中心！")
    arcade(name)
