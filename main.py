from Airplane import Airplane
from B52 import B52

proto1 = Airplane(passengers=50)
print(proto1.getCapacity())
b52 = B52()

b52.increaseCapacity(45)

print(b52.getCapacity())
