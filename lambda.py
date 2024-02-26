def funcBuilder(x):
    return lambda n: n + x


add_1 = funcBuilder(10)
add_2 = funcBuilder(50)

print(add_1(5))
print(add_2(5))

numbers = [3, 0.51, 3, 3213, 1321, 4]

square = list(map(lambda n: n**2, numbers))
print(square)

numbers2 = [3, 5415, 3, 55, 33, 11, 17, 12, 44, 63, 12, 56]

reverse_order = list(sorted(numbers2, reverse=True))
print(reverse_order)
odd = list(filter(lambda n: n % 2 != 0, numbers2))
print(odd)


from functools import reduce

numbers = [1, 3, 5, 6, 7]

total = reduce(lambda a, b: a + b, numbers, 10)
print(total)

names = ["Herway", "Sarah", "John", "Alex", "Victor", "Alice", "Bob"]

char_count = list(map(lambda n: len(n), names))
char_counts = reduce(lambda a, b: a + b, char_count, 0)
print(char_count)
print(char_counts)

total_char = reduce(lambda a, b: a + len(b), names, 0)
print(total_char)
