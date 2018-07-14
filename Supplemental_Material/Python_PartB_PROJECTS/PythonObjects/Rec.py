class Rec:
    def __init__(self,height=0, width=0): #initializes global variables
        self.height = height
        self.width = width
        
    def getArea(self):
        area = self.height * self.width
        return area        


def main():
    leng = int(input("enter the height: "))
    widt = int(input("enter the width: "))
    aRec = Rec(leng,widt) #create a Rectangle with 11 height and 12 width
    print(aRec.getArea())
    
main()