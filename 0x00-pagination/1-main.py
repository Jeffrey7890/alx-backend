#!/usr/bin/env python3

Server = __import__('1-simple_pagination').Server


server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with nagitive values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("ASsertionError raised with 0")

try:
    should_err = server.get_page(2, "Bob")
except AssertionError:
    print("ASsertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
