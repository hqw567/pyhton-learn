# r = Read
# w = Write
# a = Append
# r+ = Read and Write
# x = Create


f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names1.txt")
    print(f.read())
except:
    print("File not found")
finally:
    f.close()

f = open("names.txt", "a")
f.write("\nSara")
f.close()

f = open("names.txt", "r")
print(f.read())
f.close()

f = open("context.txt", "w")
f.write("Hello!")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()

f = open("n.txt", "w")
f.write("Hn!")
f.close()

import os

if not os.path.exists("dev.txt"):
    f = open("dev.txt", "x")
    f.close()
else:
    print("File already exists")

if os.path.exists("dev.txt"):
    os.remove("dev.txt")

with open("hello.txt") as f:
    print(f.read())
