
dividend = int(input("Dividend: "))

divisor = int(input("Divisor: "))

result = 0

try:
      result = dividend/divisor

except ZeroDivisionError as error:
      print(error)

else:
      print(result)

finally:
      print("I run irrespective of anything")




 