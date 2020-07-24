"""
A function can also be passed as an argument
"""

def plus_one(number):
      number=number+1
      return number


def add(function, number_to_add):
      res = function(number_to_add)
      print(res)

add(plus_one, int(input("Enter number for plus 1 :- ")))
