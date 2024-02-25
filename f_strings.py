person = "Herway"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

mesage = "\n%s has %s coins left." % (person,coins)
print(mesage)


message = "\n{} has {} coins left.".format(person,coins)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = {
  "person": "Herway",
  "coins":3
}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person.lower()} has {coins * 2} coins left."
print(message)

message = f"\n{player['person']} has {coins * 5} coins left."
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for n in range(1,11):
  print(f"\n num echo is {2 * n:.2f}")


for n in range(1,11):
  print(f"\n num echo is {n / 4.52:.2%}")
