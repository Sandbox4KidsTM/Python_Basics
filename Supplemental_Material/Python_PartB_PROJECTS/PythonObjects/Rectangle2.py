# Getter & Setter Methods to protect data from being assigned bad field values and to improve output

# @property decorator: http://stackabuse.com/python-properties/

class Rectangle:
    
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
    
    @property #allows us to refer to individual fields
    # @property is called a decorater
    # A decorator is simply a function 
    # that takes another function as an argument and adding to its behavior by wrapping it
    
    def height(self):
        print("Retreiving the Height")
        
        return self.__height #private field
    
    @height.setter
    def height(self, value):
        
        if value.isfloat():
            self.__height = value
        else:
            print("Please enter only numbers for height")
            
    @property #allows us to refer to individual fields
    def width(self):
        print("Retreiving the Height")
        
        return self.__width #private field
    
    @width.setter
    def width(self, value):
        
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only numbers for width")
    
    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    aRectangle = Rectangle() #make an instance of the blueprint
    
    h = input("Enter the height")
    w = input("Enter the width")
    
    aRectangle.height = h #as we have @property set up, 
                        #we don't have to refer to this as height()
    aRectangle.width = w #as we have @property set up,
                        #we don't have to refer to this as height()
    
    print("Height :", aRectangle.height)
    print("Width :", aRectangle.width)
    
    print("The Area is :", aRectangle.getArea())
    
main()