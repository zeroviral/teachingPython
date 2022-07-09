class Airplane:

    maxSpeed = None
    passengerCount = None

    def __init__(self, passengers=100):
        self.passengerCount = passengers

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

