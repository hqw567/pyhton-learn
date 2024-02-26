def hello():
    print("Hello, World!")


hello()


def sum(a, b=5):
    if type(a) != int or type(b) != int:
        return ValueError("Invalid input")
    return a + b


print(sum("3"))


def mult_items(*args):
    print(args)
    print(type(args))


def mult_items_2(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_items(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

mult_items_2(a=1, b=2, c=3)
