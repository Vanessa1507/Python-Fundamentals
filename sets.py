# Create an empty set we use set()
set()

{1}
type({1})  # <class 'set'>

names = {"Laura", "Maria", "Ivan", "Fernanda", "Laura"}
names  # {"Laura", "Maria", "Ivan", "Fernanda"}

len(names)  # 4

# Let's check for some hashes
hash("Laura")  # -1781415656554363987

hash([])  # TypeError: unhashable type: 'list'

{[]}  # TypeError: unhashable type: 'list'

# Get the unique items from a List
pet_names = ["Magola", "Arya", "Simón", "Ramón", "Magola", "Arya"]
set(pet_names)  # {'Arya', 'Magola', 'Simón', 'Ramón'}

names[0]  # Value of type "set[str]" is not indexableMypyindex


# ADDING, REMOVING, AND UPDATING
colors = {"red", "blue", "green", "pink"}
colors.add("black")
colors  # {'blue', 'pink', 'red', 'green', 'black'}
colors.discard("pink")
colors  # {'blue', 'red', 'green', 'black'}
# colors.remove("pink") # KeyError: 'pink'

numbers = {1, 2, 3}

colors.update(numbers)
colors  # {1, 2, 'blue', 3, 'red', 'green', 'black'}

colors.update("Laura")  # A string is a sequence under the hood
colors  # {1, 2, 'blue', 3, 'u', 'r', 'red', 'green', 'black', 'L', 'a'}


# COMBINING, COMPARING, AND CONTRASTING
# Set operations
"blue" in colors  # True
"orange" in colors  # False

rainbow_colors = {
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
}

favorite = {"black", "white", "gray", "blue"}
favorite_colors = favorite

rainbow_colors  # {'yellow', 'blue', 'red', 'violet', 'green', 'orange'}
favorite_colors  # {'gray', 'black', 'blue', 'white'}

# my_set.union(other_set) or my_set | other_set
rainbow_colors.union(favorite_colors)
# {'yellow', 'blue', 'white', 'red', 'violet', 'green', 'orange', 'black', 'gray'}
rainbow_colors | favorite_colors  # {'yellow', 'blue', 'white', 'red', 'violet', 'green', 'orange', 'black', 'gray'}

# my_set.intersection(other_set) or my_set & other_set
rainbow_colors.intersection(favorite_colors)  # {'blue'}
rainbow_colors & favorite_colors  # {'blue'}

# my_set.difference(other_set) or my_set ^ other_set
rainbow_colors.difference(favorite_colors)
# {'yellow', 'red', 'violet', 'green', 'orange'}

rainbow_colors ^ favorite_colors
# {'yellow', 'white', 'red', 'violet', 'green', 'black', 'orange', 'gray'}
