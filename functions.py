def foo():
    print("Hello")


def meaning_of_life():
    return 42


called_foo = foo()
x = meaning_of_life()


# FUNCTION ARGUMENTS
def add_numbers(x, y):
    return x + y


add_numbers(3, 5)

a = 1
b = 5

add_numbers(a, b)
# TypeError: add_numbers() missing 1 required positional argument: 'y'
# add_numbers(a)


def say_greeting(
    name,
    greeting="Hello",
):
    print(f"{greeting}, {name}")


say_greeting("Vanessa")
say_greeting("Vanessa", "Bonjour")


def create_query(language="Javascript", num_stars=50, sort="desc"):
    return f"language: {language}, {num_stars} {sort}"


create_query()  # language: Javascript, 50 desc"
create_query(language="Python")  # language: Python, 50 desc"
create_query(language="Python", sort=100, num_stars=1)  # language: Python, 1 100"


# WARNING: Don't do this
def dont_do_this(a, b=[]):
    b.append(a)
    print(f"B is: {b}")


def do_this(a, b=None):
    if b is None:
        b = []

    b.append(a)
    print(f"B is: {b}")


dont_do_this(5)  # B is: [5]
dont_do_this(13)  # B is: [5, 13]


def twitter_info():
    account = "something"
    print(f"Account inside the function is {account}")


# account # NameError: name 'account' is not defined

name = "Vanessa"


def try_change_name():
    name = "Max"
    print(f"Name inside function: {name}")


# Print what is inside the scope
try_change_name()
# Print what is outside the scope
print(f"Name outside function: {name}")
