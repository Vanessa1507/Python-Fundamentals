# Truthiness
True  # True
False  # False

type(True)  # <class 'bool'>

bool(True)  # It takes a specified argument and returns its boolean value.

bool(0)  # False-y
bool(1)  # Truthy
bool(-1)  # Truthy

bool([])  # False-y
bool({})  # False-y
bool(())  # False-y
bool(set())  # False-y

bool([1])  # Truthy
bool({1: 1})  # Truthy
bool((1,))  # Truthy
bool({1})  # Truthy

bool(None)  # False-y

# Don't name variables True, False, None. They are keywords


# COMPARISONS
3 < 5  # True
5 > 3  # True
1 <= 1  # True
1 < 3  # True
5 >= 5  # True
5 >= 3  # True

# Upper case letters are lower-valued in ASCII
"T" < "t"  # False

"bat" < "cat"  # True
"a" < "b"  # True

# EQUAITY  == !=
"Hello" == "Hello"  # True
[1, 2, 3] == [0, 2, 3]  # False
[1, 2, 3] == [1, 2, 3]  # True

a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True
a != b  # False


# Identity is keyword
x = None
x is None  # True

x is False  # False
x is True  # False

a is b  # False as they were created in different instances

c = a
a is c  # True

d = None
d is None  # True
d is not None  # False


# AND, OR, & NOT
i = True
j = True

i and j  # True, j is returned as i is not False
[1] and [2]  # [2], is returned as both are Truthy
[] and 3  # [] is returned
5 and {}  # {} is returned

i or j  # True, i is returned as i is True
[1] or [2]  # [1], is returned as the fisrt part is True
[] or 3  # 3 is returned as the first part is False
5 or {}  # 5 is returned

not False  # True
not True  # False
bool(1)  # True
not bool(1)  # False
bool(0)  # False
not bool(0)  # True


a = True
b = True
c = False
a and (b or c)  # True

a = True
b = True
not (a or b)  # False
