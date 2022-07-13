from Airplane import Airplane
from B52 import B52
import string

proto1 = Airplane(passengers=50)
print(proto1.getCapacity())
b52 = B52()
passenger = "John Smith"

proto1.addPassenger(passenger)
proto1.listPassengers()

