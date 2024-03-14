# Create a list with [] or list()
type([])  # <class 'list'>

names = [
    "Laura",
    "Maria",
    "Ivan",
    "Fernanda",
]
type(names)  # <class 'list'>
print(names)  # ['Laura', 'Maria', 'Ivan', 'Fernanda']

# Check the number of items in the list
len(names)  # 4

names[0]  # "Laura"
names[1]  # "Maria"
names[2]  # "Ivan"
names[3]  # "Fernanda"
# names[4]  # IndexError: list index out of range

names[0] = "Arya"

# numbers=[ 1, 2, 3 4] # SyntaxError: invalid syntax (lists.py, line 26)compile


# CHANGING THE ORDER OF A LIST
lottery_numbers = [1, 4, 1234123, 78, 11]
sorted(lottery_numbers)  # [1, 4, 11, 78, 1234123]
print(lottery_numbers)  # [1, 4, 1234123, 78, 11]
sorted(lottery_numbers, reverse=True)  # [1234123, 78, 11, 4, 1]

# Second way of sorting list in Python -- in place
lottery_numbers.sort()
print(lottery_numbers)  # [1, 4, 11, 78, 1234123]
lottery_numbers.reverse()
print(lottery_numbers)  # [1234123, 78, 11, 4, 1]

type(lottery_numbers)  # <class 'list'>
dir(
    lottery_numbers
)  # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
help(
    lottery_numbers.reverse
)  # reverse() method of builtins.list instance Reverse *IN PLACE*.

len(lottery_numbers)  # 5


# ADDING ITEMS TO A LIST
pet_names = ["Magola", "Arya", "Simón", "Ramón"]
pet_names.append("Apolo")
print(pet_names)  # ["Magola", "Arya", "Simón", "Ramón", "Apolo"]
len(pet_names)  # 5

# Insert into my List
pet_names.insert(0, "Mateo")
print(pet_names)  # ["Mateo", "Magola", "Arya", "Simón", "Ramón", "Apolo"]
len(pet_names)  # 6

# Combine lists
colors = ["Orange", "White"]
pet_names.extend(
    colors
)  # [ "Mateo", 'Magola', 'Arya', 'Simón', 'Ramón', 'Apolo', 'Orange', 'White']


# LIST LOOKUPS
food = ["Pizza", "Rice", "Beans", "Pizza"]
print("Rice" in food)  # True
print("Pizza" in food)  # True

# By index()
food.index("Rice")  # 1
food.index("Pizza")  # 0

food.count("Rice")  # 1
food.count("Pizza")  # 0

food[0] = "Apple"
print(food)  # ['Apple', 'Rice', 'Beans', 'Pizza']

pos = food.index("Beans")
food[pos] = "Grapes"
print(food)  # ['Apple', 'Rice', 'Grapes', 'Pizza']


# REMOVING ITEMS FROM A LIST
animals = ["Dog", "Cat", "Rabbit", "Cow", "Dog"]
animals.remove("Dog")
print(animals)  # ['Cat', 'Rabbit', 'Cow', 'Dog']
# animals.remove("Pig")  # ValueError: list.remove(x): x not in list

animals.pop()  # 'Dog'
print(animals)  # ['Cat', 'Rabbit', 'Cow']

animals.pop(1)  # 'Rabbit'
print(animals)  # ['Cat', 'Cow']
len(animals)  # 2

# animals.pop(3)  # IndexError: pop index out of range
