# TYPES
x = 42
y = 3 / 4
z = int("7")
a = float(5)
name = "Vanessa"


# NUMBERS
rent = 480
per_day = rent / 30
print(per_day)


#  STRINGS
print("Hello world")
print("My name is", name)

# There are three different ways to format strings in Python3. You may run into %-formatting and str.format() in older code. These are still common in Python but no longer recommended, due to readability concerns.
print("Hello, my name is %s" % name)

f"Hello, my name is {name}. I pay ${per_day} in rent, per day"
