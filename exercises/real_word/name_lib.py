def upper_case_name(name):
    return name.upper()


# Main method: https://www.learnpython.dev/02-introduction-to-python/175-running-code/30-the-main-method/
# __name__ is a special variable that’s set by Python that tells it where it was called from. We can tell it’s a special variable because it starts and ends with __. That’s a hint that you don’t want to change the value of this variable, or it could adversely affect the execution of your Python program.
# In Python, __ is also called double underscore, or dunder.
print("dunder name", __name__)
if __name__ == "__main__":
    name = "Vanessa"
    name_upper = upper_case_name(name)

    print(f"Upper case name is {name_upper}")
