def hello(name, lang):
    echo = {
        "english": "Hello",
        "french": "Bonjour",
        "spanish": "Hola",
        "german": "Hallo",
        "italian": "Ciao",
        "chinese": "你好",
    }
    return f"{echo[lang]} {name}"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Say hello in different languages")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet",
    )
    parser.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        help="The language you want to be greeted in",
        choices=["english", "french", "spanish", "german", "italian", "chinese"],
    )
    args = parser.parse_args()
    print(hello(args.name, args.lang))
