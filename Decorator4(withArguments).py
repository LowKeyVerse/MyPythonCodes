
def deco_with_arg(function):
      def wrapper(arg1, arg2):
            print("My arguments are {0}, {1}".format(arg1, arg2))
            function(arg1, arg2)

      return wrapper

@deco_with_arg
def cities(city_1, city_2):
      print("The two cities are {0}, {1}".format(city_1,city_2))


cities("Pithoragarh", "Munsyari")