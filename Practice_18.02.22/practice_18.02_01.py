["John", "Mike", "Bob", "Taras", "Bob"]
# 2 arr
[1, 23, 13,]

# 1) Find Mikes index
# 2) Slice arr from 0 to 3 and save it into new variable
# 3) Count , how much Bobs into arr
# 4) Remove Taras from arr
# 5) Sort arr

# 6) Join two arrays into one
# 7) Joined arr must be a string

names= ["John", "Mike", "Bob", "Taras", "Bob"]


names.remove("Taras")
print(names)

sorted_arr=sorted(names)
print(sorted_arr)

arr=[1, 23, 13,]

names.extend(arr)
print(names)

names= ["John", "Mike", "Bob", "Taras", "Bob"]
print(names.index("Mike"))


print(names[0:3])

print(names.count("Bob"))

names= ["John", "Mike", "Bob", "Taras", "Bob"]
arr=[1, 23, 13,]
names.extend(arr)
print(names)

print(" ".join(names))


