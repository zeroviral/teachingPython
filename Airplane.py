class Airplane:

    passengerCount = None

    def __init__(self, passengers=100):
        self.passengerCount = passengers

    def getCapacity(self):
        return self.passengerCount