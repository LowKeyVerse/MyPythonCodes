"""
Decorator example
"""


import string

def uppercase_decorator(function):
      def wrapper():
            func = function()
            message = func.upper()
            return message
      
      return wrapper


def split_decorator(function):
      def wrapper():
            message = function().split()
            return message
      
      return wrapper

"""
Without using @decorator the following function demonstrates how to use

"""
# def greet():
#       return 'Hello there'

# final  = split_decorator(greet)
# print(final())

"""
Python provides the following @ function to directly associate with the 'to be decorated function'.
"""

@split_decorator
@uppercase_decorator
def greet():
      return 'Hello there'

print(greet())
