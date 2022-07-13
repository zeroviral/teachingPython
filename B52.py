from Airplane import Airplane

class B52(Airplane):

    def increaseCapacity(self, additional):
        self.passengerCount += additional

    def cancelReservation(self, name):
        if name in self.passengers:
            self.passengers[name] = None



