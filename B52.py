from Airplane import Airplane

class B52(Airplane):

    def increaseCapacity(self, additional):
        self.passengerCount += additional

    def remove_passenger(self, passenger):
        for seat, name in self.passengers.items():
            if name == passenger:
                del self.passengers[seat]
                return







