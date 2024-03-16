# Dictionaries
{}
type({})  # <class 'dict'>
dict()
type(dict())  # <class 'dict'>


{1: "one"}
nums = {"one": 1, "two": 2, "three": 3}
type(nums)  # <class 'dict'>
nums  # {"one": 1, "two": 2, "three": 3}

# {[]: 1}  # TypeError: unhashable type: 'list'
# Only immutable types can be used as dictionary keys!

nums["one"]  # 1

nums[0]  # KeyError: 0, because the 0 key doesn't exist

nums.get("one")  # 1
nums.get("four")  # NoneType
nums.get("four", "default value")  # default value
nums.get("one", "default value")  # 1


# ADDING, REMOVING, AND ACCESSING KEYS OR VALUES
# Add
nums["four"] = 4

# Update. It overwrite the current value of the key with a new one
nums["two"] = "twooooo"

# Combine
colors = {"r": "red", "b": "blue", "g": "green"}
numbers = {1: "one", 2: "two", 3: "three"}
colors.update(numbers)
colors  # {'r': 'red', 'b': 'blue', 'g': 'green', 1: 'one', 2: 'two', 3: 'three'}


vegetables = {"green": ["Spinach"]}
type(vegetables["green"])  # <class 'list'>
vegetables["green"].append("Apple")
vegetables["green"]  # ['Spinach', 'Apple']


nums = {"one": 1, "two": 2, "three": 3}
nums.keys()  # dict_keys(['one', 'two', 'three'])
nums.values()  # dict_values([1, 2, 3])
nums.items()  # dict_items([('one', 1), ('two', 2), ('three', 3)])
