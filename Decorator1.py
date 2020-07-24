"""
Definig a function inside another function.
"""

def add_one(number):
      def Plus_one(number):
            return number+1
      
      return Plus_one(number)

add_one(4)
# print(adding)