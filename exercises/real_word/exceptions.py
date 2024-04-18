# This will throw an error
try:
    int("a")
# We can use as to save the error in a variable and if we use it, it can give us more information
except ValueError as e:
    print("Oops, you can't do that!", e)
print("This is the end of my program")
