from collections import defaultdict

class Airplane:

    maxSpeed = None
    passengerCount = None
    passengers = defaultdict()
    seatsAvailable = None

    def __init__(self, passengers=100, seatsAvailable=100):
        self.passengerCount = passengers
        self.seatsAvailable = seatsAvailable

    def getCapacity(self):
        return self.passengerCount

    def setCapacity(self, newCount):
        self.passengerCount = newCount

    def getMaxSpeed(self):
        return self.maxSpeed

    def setMaxSpeed(self, topSpeed):
        self.maxSpeed = topSpeed

    def calculateTravelTime(self, odoStart, odoEnd):
        if odoEnd <= odoStart or odoStart < 0:
            print("Incorrect odometer range.")
            return None
        totalDistance = odoEnd - odoStart
        travelTime = totalDistance // self.maxSpeed
        return travelTime

    def addPassenger(self, name):
        if self.seatsAvailable == 0:
            print("No more seats available")
            return

        self.passengers[name] = self.seatsAvailable
        self.seatsAvailable -= 1

    def listPassengers(self):
        print(self.passengers)

    def getPassengerSeatNumber(self, name):
        returnString = ("Passenger '%s' has seat number: %i" % (name, self.passengers[name]))

        return returnString