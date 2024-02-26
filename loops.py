# value = 0
# while value <= 10:
#   value += 1
#   if value == 5:
#     continue
#   print(value)
# else:
#   print("Loop ended " + str(value))


names = ["John", "Paul", "George", "Ringo"]
for name in names:
    if name == "George":
        continue
    print(name)


for i in "Mississippi":
    print(i)

for name in names:
    if name == "Paul":
        break
    print(name)


for i in range(10, 20, 5):
    print(i)
else:
    print("Loop ended " + str(i))

names = ["John", "Paul", "George", "Ringo"]
actions = ["singing", "playing guitar", "playing bass", "playing drums"]

for name in names:
    for action in actions:
        print(name + " is " + action)
    print("\n")

# for name, action in zip(names, actions):
#   print(name + " is " + action)
#   print("\n")
