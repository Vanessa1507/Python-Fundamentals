colors = ["Red", "Blue", "Black", "Green"]

for color in colors:
    print(color)

# Red
# Blue
# Black
# Green

range(5)  # range(0, 5)
list(range(0, 5))  # [0, 1, 2, 3, 4]


for num in range(5):
    print(num)

# 0
# 1
# 2
# 3
# 4


for num in range(1, 5):
    print(num)

# 1
# 2
# 3
# 4

for num in range(0, 10, 3):
    print(num)

# 0
# 3
# 6
# 9


for i, color in enumerate(colors):
    print(f"index: {i} color: {color}")

# index: 0 color: Red
# index: 1 color: Blue
# index: 2 color: Black
# index: 3 color: Green


# LOOPING OVER DICTIONARIES
hex_colors = {"red": "#FF", "green": "#008"}

for color in hex_colors:
    print(color)  # The keys


for key, value in hex_colors.items():
    print(key, value)  # The keys

# red #FF
# green #008


# ValueError: too many values to unpack (expected 2)
# for key, value in hex_colors:
#     print(key, value)


# CONTROL FLOW
if 3 < 5:
    print("Hello")
# Hello

if 3 > 5:
    print("Hello")

a = []
if a:
    print("Hello")
# Nothing

b = [1]
if b:
    print("Hello")
# Hello


a = True
if a:
    print("Hello")
else:
    print("Goodbye")
# Hello

a = False
if a:
    print("Hello")
else:
    print("Goodbye")
# Goodbye

a = False
b = True
if a:
    print("1")
elif b:
    print("2")
else:
    print("3")
# 2


# WHILE & CONTROL STATEMENTS
counter = 0
max = 4

while counter < max:
    print("The count is", counter)
    counter = counter + 1

# The count is 0
# The count is 1
# The count is 2
# The count is 3


# USING break
names = ["Laura", "Ivan", "Maria", "Fernanda"]

for name in names:
    print(f"Hello, {name}")
    if name == "Maria":
        break
# Hello, Laura
# Hello, Ivan
# Hello, Maria


# continue
for name in names:
    if name != "Ivan":
        continue
    print("Hello", {name})
# Hello {'Ivan'}


count = 0
while True:
    count += 1
    if count == 5:
        print("count was reached")
        break
# count was reached


def find_target_name(names, target_name="Fer"):
    for name in names:
        print(name)
        if name == target_name:
            return "Found the special case"


find_target_name(names)
# Laura
# Ivan
# Maria
# Fernanda

find_target_name(names, "Maria")
# Laura
# Ivan
# Maria
# 'Found the special case'
