def add_numbers(x, y):
    return x + y


add_numbers(1, 2)


a = 1
b = 2

add_numbers(a, b)

# expected an indented block after function definition on line
# def foo():
# x=5

x = 1
y = 2


def add_numbers2(x, y):
    print(f"Inside the function, x: {x}, y: {y}")
    return x + y


print(f"Outside the function, x: {x}, y: {y}")  # "Outside the function, x: 1, y: 2"
add_numbers(4, 5)  # "Inside the function, x: 4, y: 5"


def numbers():
    x = 0
    y = -1

    print(f"Inside the function, x: {x}, y: {y}")


numbers()  # "Inside the function, x: 0, y: -1"
print(f"Outside the function, x: {x}, y: {y}")  # "Outside the function, x: 1, y: 2"


# POSITIONAL ARGUMENTS VS KEYWORD ARGUMENTS
def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    if operation == "subtract":
        return x - y


calculate_numbers(4, 5)  # Positional arguments
calculate_numbers(4, 5, operation="subtract")
calculate_numbers(y=3, x=2)  # Keyword arguments
# calculate_numbers()  # Add 2 missing arguments; 'calculate_numbers' expects at least 2 positional arguments
