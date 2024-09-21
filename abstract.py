#abstractmethod oop
from abc import ABC, abstractmethod
class ABC:
    @abstractmethod
    def switchOn(self):
        pass
    @abstractmethod
    def switchOff(self):
        pass
    @abstractmethod
    def ring(self):
        pass

class iphone(ABC):
    def switchOn(self):
        return "Enter setting \n Enter switch on"
    def switchOff(self):
        return "Hold power button"
    def ring(self):
        return "awilo"
    
class Andriod(ABC):
    def switchOn(self):
        return "Enter setting \n Enter switch on"
    def switchOff(self):
        return "Hold oning button"
    def ring(self):
        return "psquare"
    
device =[Andriod(), iphone()]
for devices in device:
     print(devices.switchOn())
j = iphone()
print(j.switchOn())
    
