class Ur:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
     

    def kvur(self):
        disc = (self.b ** 2) - (4 * self.a * self.c)
        return disc
        
    def cor(self):
        cor1 = (( -(self.b)) - (self.kvur() ** (1/2))) / (2 * self.a) 
        cor2 = (( -(self.b )) + (self.kvur() ** (1/2))) / (2 * self.a) 
        print (f"1:{cor1},2: {cor2}")

    def __del__(self):                     
        print('!')

def lf():
    u = Ur(1,2,3)
    u.cor()
lf()
    







#(a * (x ** 2) + (b * x) + c)