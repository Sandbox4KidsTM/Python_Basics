class Workerbee:
    #pass
    raise_amt = 1.04    

    #self means passing the instance as the parameter
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@sandbox.com'
    
    def fullname(self): #self means passing the instance as the parameter
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.rasie_amt)
    
    @classmethod
    #cls refers to class variable name, just as self refers to instance variable
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
#w1 = Workerbee()
#w2 = Workerbee()

#w1.first = 'Corey'
#w1.last = 'Schaffer'
#w1.pay = 75000
#w1.email = w1.first + '.' + w1.last + '@sandbox.com'

#print(w1)
#print(w2)

#print(w1.first)

w1 = Workerbee('Corey', 'Schaffer', 75000)
print(Workerbee.fullname(w1)) 
#note: instance w1 is being passed as paramter to the method, same as 'self'

print(w1.fullname())