band = {
  "vocals" : "Plant",
  "guitar" : "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))


print(band.get("vocals"))
print(band['guitar'])

print(band.keys())
print(band.values())

print(band.items())

print("guitar" in band)
print("guitar1" in band)

band['vocals'] = "Plant2"
band.update({"vocals3":"Plant3"})
print(band)

print(band.pop("vocals3"))
print(band)

print(band.popitem())
print(band.popitem())
print(band)

band.update({"vocals":"Plant"})
band.clear()
print(band)

band['3213'] = 3
del band['3213']
print(band)

del band2
band.update({"vocals":"Plant"})
band2 = band.copy()
print(band2)

band.clear()
print(band2)
print(band)

print("--------------")

member1 = {
  "name" : "John",
  "instrument" : "guitar"
}

member2 = {
  "name" : "Paul",
  "instrument" : "bass"
}

band4 = {
  "member1" : member1,
  "member2" : member2
}

print(band4)
print(band4['member1']['name'])

print('========')

nums = { 1, 2, 3, 4}

nums2  =  set([1, 2, 3, 4])
print(nums)
print(nums2)
print(len(nums))
print(type(nums2))
print(type(nums))

nums = {1,True,5,False,2}
print(nums)

print(True in nums)
nums.add(6)
print(nums)
nums.remove(6)
print(nums)

morenums = {4,5,6,7}
print(nums.update(morenums))
print(nums.union(morenums))

one = {1,2,3,4}
two = {3,4,5,6}

one.difference_update(two)
print(one)
one = {1,2,3,4}
two = {3,4,5,6}
one.symmetric_difference_update(two)
print(one)
