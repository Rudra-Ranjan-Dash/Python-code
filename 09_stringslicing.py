# cocatenating two strings
# name = "pikun"
# greeting = "Good morning, "
# print(type(name))
# print(greeting + name)
name = "pikun"
print(name[2])
# name[3] = "d" --> doesnot work
print(name[0:3])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
print(name[-4:-1]) # is same as name[1:4]

# slicing with skip value
name = "pikunisgood"
d = name[0::2]
print(d)

#print the string multiple times
story = "today is a sunny day "
print(story*3)