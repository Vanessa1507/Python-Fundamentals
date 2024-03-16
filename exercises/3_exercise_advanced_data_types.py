# ==================================================
#                      List
# ==================================================
my_list = ["h", "e", "l", "l", "o,"]
my_list  # ["h", "e", "l", "l", "o,"]

my_list.append("!")
my_list  # ["h", "e", "l", "l", "o,", "!"]

len(my_list)  # 6
my_list[0]  # "h"

# Slicing
my_list[0:3]  # ["h", "e", "l"]
my_list[:3]  # ["h", "e", "l"]

# Get the last item
my_list[-1]  # ["!"]

my_list.remove("l")
my_list  # ["h", "e", "l", "o,", "!"]


my_list.insert(2, "l")
my_list  # ["h", "e", "l", "l", "o,", "!"]


# Delete items from a list
del my_list[0]
my_list  # ["e", "l", "l", "o,", "!"]

last_item = my_list.pop()
last_item  # "!"
my_list  # ["e", "l", "l", "o,"]

"!" in my_list  # False

my_list.sort(reverse=True)  # ["o", "l", "l", "e"]
sorted(my_list, reverse=True)


# ==================================================
#                      Set
# ==================================================
my_set = set()
type(my_set)  # <class 'set'>

my_set = {1, 2, 3}
my_set  # {1, 2, 3}

my_set.add(4)
my_set  # {1, 2, 3, 4}

my_set.remove(2)
my_set  # {1, 3, 4}

# Membership
2 in my_set  # False

my_set.add(3)
my_set  # {1, 3, 4}


my_other = {1, 2, 3}
my_other_set = my_other

my_set.union(my_other_set)
my_set  # {1, 2, 3, 4}

my_set.difference(my_other_set)
my_set  # {4}

my_set.intersection(my_other_set)
my_set  # {1, 3}


# ==================================================
#                      Tuple
# ==================================================
type((3))  # <class 'int'>
type((3,))  # <class 'tuple'>

my_tuple = (1,)
my_tuple  # (1, )

# my_tuple[1] = 2  # TypeError: 'tuple' object does not support item assignment

person = ("Jim", 29, "Austin, TX")
name, age, hometown = person

name  # "Jim"
age  # 29
hometown  # "Austin, TX"


# ==================================================
#                      Dict
# ==================================================
my_dict = {"key": "value"}
my_dict[0]  # KeyError: 0

my_dict["hello"] = "world"
my_dict["foo"] = "bar"

my_dict["hello"]  # 'world'
my_dict.get("hello")  # 'world'

# my_dict["baz"]  # KeyError: 'baz'
my_dict.get("baz")  # NoneType
my_dict.get("baz", "default")  # 'default'
my_dict.get("foo", "default")  # 'bar'


my_dict.keys()  # dict_keys(['key', 'hello', 'foo'])
my_dict.values()  # dict_values(['value', 'world', 'bar'])
my_dict.items()  # dict_items([('key', 'value'), ('hello', 'world'), ('foo', 'bar')])


# ==================================================
#                      Mutability
# ==================================================
my_list = [1, 2, 3]
my_list[0] = "a"
my_list  # ["a", 2, 3]

my_dict = {"hello": "world"}
my_dict["foo"] = "bar"
my_dict  # {"hello": "world", "foo": "bar"}

my_set = {1, 2, 3}
# my_set[0] = "a" # "Can not do this"
my_set.add("a")
my_set  # {1,2,3, "a"}


my_tuple = (
    1,
    2,
    3,
)
my_tuple[0]  # 1
# my_tuple[0] = "a"  # TypeError: 'tuple' object does not support item assignment
