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

names[0]  # TypeError: 'set' object is not subscriptable
