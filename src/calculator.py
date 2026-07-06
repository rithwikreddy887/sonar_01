import os

username = os.getenv("username") # Compliant
password = os.getenv("password") # Compliant
usernamePassword = 'user=%s&password=%s' % (username, password) # Compliant


def divide(a, b):
    return a / b


def calculate():

    unused = 100

    num1 = 10
    num2 = 0

    print(divide(num1, num2))


def duplicate_one():

    total = 0

    for i in range(10):
        total += i

    print(total)


def duplicate_two():

    total = 0

    for i in range(10):
        total += i

    print(total)