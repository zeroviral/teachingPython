from Airplane import Airplane
from B52 import B52

proto1 = Airplane(passengers=50)
print(proto1.getCapacity())
b52 = B52()

b52.increaseCapacity(45)

print(b52.getCapacity())

b52.setCapacity(300)

print(b52.getCapacity())

b52.setMaxSpeed(600)

print(b52.getMaxSpeed())

print("%i hours" % b52.calculateTravelTime(89999, 97000))