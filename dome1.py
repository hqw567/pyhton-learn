mylist = list([1, "Herway", True])
print(mylist)

p = (1, 3, 3, 4, 5)
print(p)

newList = list(mylist)
newList.append(6)
print(newList)
print(mylist)

print("-----------------")
(one, *two, three, hey) = p
print(one)
print(two)
print(hey)

print(p.count(3))
