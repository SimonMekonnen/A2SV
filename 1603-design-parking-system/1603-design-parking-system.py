class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.m = medium 
        self.s = small 
    def addCar(self, car: int) -> bool:
    
        if car == 3:
            
            if self.s <= 0:
                return False
            self.s -= 1
        elif car == 2:
            if self.m <= 0:
                return False
            self.m -= 1
        else:
            if self.big <= 0:
                return False
            self.big -= 1
            
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)