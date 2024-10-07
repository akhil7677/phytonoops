class Fraction():
    # use of parameter function
    def __init__(self,x,y):
        self.numerator=x
        self.denominator=y
        
    def __str__(self) :
        return "{}/{}".format(self.numerator,self.denominator)
    
    def __add__(self,other):
        
    
fr1=Fraction(3,4)
print(fr1)