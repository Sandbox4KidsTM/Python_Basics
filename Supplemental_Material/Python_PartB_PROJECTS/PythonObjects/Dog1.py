# OOP Concepts

#Real World Objects: Attributes (Fields / Variables) & Capabilities (Methods / Functions)
# Dog Attributes: Height, Weights, Favorite Food
# Dog Capabilities (Methods): Run, Eat, Bark

class Dog: #template to create an Object 
    #whenever Dog is first created
    def __init__(self, name = "", height=0, weight=0): 
        #self allows an object to refer to itself: e.g. my height
        #init method helps initialize the object
        #self helps refer to itself (e.g. my height)
        self.name = name # my name is _______
        self.weight = weight # my weight is _______
        self.height = height # my height is _______
    
    def run(self):
        print("{} the dog runs.".format(self.name))
        
    def bark(self):
        print("Bow, Wow!!!")
        print("{} the dog barks.".format(self.name))
        
    def eat(self):
        print("{} the dog eats.".format(self.name))
        

#we'll create a dog called Spot, which is an instance of the Dog class
def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()
    koko = Dog()
    koko.name = "Kokomoko"
    koko.run()
    
#execution starts from below here
main()