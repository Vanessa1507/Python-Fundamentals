# Create a tuple with () or tuple()
a = ()
type(a)  # <class 'tuple'>

# b = (1)
# type(b)  # <class 'int'>

c = (1,)
type(c)  # <class 'tuple'>

x = 1, 2, 3, 5
type(x)  # <class 'tuple'>

student = ("Marcy", 8, "History", 3.5)

# Access item by index
student[0]  # Marcy
student[1]  # 8

# student[0] = "Laura"  # TypeError: 'tuple' object does not support item assignment


# UNPACKING TUPLES
student  # ("Marcy", 8, "History", 3.5)
name, age, subject, grade = student
name  # Marcy
age  # 8
subject  # History
grade  # 3.5

# foo, bar, baz = student  # Too many values to unpack (3 expected, 4 provided)Mypymisc
# Omit saving the grade item as a variable
name, age, subject, _ = student


# Use unpacking in the return of a function
def http_status_code():
    return 200, "OK"


http_status_code()  # 200, "OK"
