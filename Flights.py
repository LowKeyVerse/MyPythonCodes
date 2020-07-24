class Flight():
      counter = 1
      def __init__(self, org, dest):
            self.id = Flight.counter
            self.origin = org
            self.destination = dest
            self.passenger_list=[]
            Flight.counter+=1

      def add_passenger(self, P):
            self.passenger_list.append(P)
            P.flight_ID = self.id

class Passenger():
      def __init__(self, name):
            self.name = name

      def print_info(self):
            print(f"Name : {self.name}")
            try:
                  print(f"Flight_ID is : {self.flight_ID}")
            except AttributeError:
                  print(f"{self.name} has not been added to any flight yet")

def main():
      f1 = Flight("Naini", "Dehradun")
      f2 = Flight("Gzbd", "Naini")
      f3 = Flight("Dehradun", "Naini")
      Lokesh = Passenger("Lokesh")
      Manish = Passenger("Manish")
      # f1.add_passenger(Lokesh)
      f3.add_passenger(Manish)
      Manish.print_info()
      Lokesh.print_info()

if __name__ == "__main__":
      main()
