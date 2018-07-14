# this explores the OOP concept of inheritance
# https://www.youtube.com/watch?v=d8kCdLCi6Lk

class Animal:
    
    def __init__(self, birthType="Unknown", appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType #live or egg
        self.appearance = appearance #fur, feathers, etc.
        self.blooded = blooded #warm or cold blooded
    
    @property
    def birthType(self):
        return self.__birthType
    
    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType
        
    
    @property
    def appearance(self):
        return self.__appearance
    
    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance
        
    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded
    
    def __str__(self): #magic method starts and ends with "__"
        return "A {} is {} it is {} it is {}".format(type(
                self).__name__, self.birthType, self.appearance, self.blooded)
        
class Mammal(Animal): #Mammal class inherits from Animal class
    def __init__(self, birthType="born alive",
                 appearance="hair or fur",
                 blooded="warm blooded",
                 nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung #new property that is in Mammal, but not in Animal class
        
    @property
    def nurseYoung(self):
        return self.__nurseYoung
    
    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung
            
    def __str__(self):
        return super().__str__() + "and it is {} they nurse their young".format(self.nurseYoung)
        
def main():
    animal1 = Animal("born alive")
    print(animal1.birthType)
    print(animal1)
    print()
    
    mammal1 = Mammal()
    print(mammal1.birthType)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print(mammal1)

main()