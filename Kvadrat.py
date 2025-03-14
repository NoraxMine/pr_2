import matplotlib.pyplot as plt
import numpy as np


class Uravnenie:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def discriminant(self):
        disc = (self.b ** 2) - (4 * self.a * self.c)
        return disc
    
    def cor(self):
        if int(self.discriminant()) > 0:
            coren_1 = (( -(self.b)) - (self.discriminant() ** (1/2))) / (2 * self.a) 
            coren_2 = (( -(self.b )) + (self.discriminant() ** (1/2))) / (2 * self.a)
            print (f"1:{coren_1},2: {coren_2}")
        elif int(self.discriminant()) == 0:
            coren_1 = (( -(self.b))/ (2 * self.a))
            print (f"1:{coren_1}")
        
        elif int(self.discriminant()) < 0:
            print (f"1:corna_net")

    def __del__(self):                     
        print('!')

    def func(self, x):
        y = (self.a * (x ** 2)) + (self.b * x) + self.c
        return y

    def paint(self):
        xmin = -20.0
        xmax = 20.0
        count = 2000000

        xlist = np.linspace(xmin, xmax, count)
        ylist = [self.func(x) for x in xlist]
        plt.plot(xlist, ylist, color = 'red')
        plt.grid()
        plt.show() 

class Proizvod(Uravnenie):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def func(self, x):
        y = (self.a * x * 2) + (self.b) 
        return y

    def paint(self):
        xmin = -20.0
        xmax = 20.0
        count = 2000000

        xlist = np.linspace(xmin, xmax, count)
        ylist = [self.func(x) for x in xlist]
        plt.plot(xlist, ylist, color = 'purple')
        plt.grid()
        plt.show() 

    def __del__(self):                     
        print('!')

class Integral(Uravnenie):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)

    def func(self, x):
        y = ((self.a * (x ** 3))/3) + ((self.b *(x ** 2))/2) + (self.c * x) + self.d
        return y

    def paint(self):
        xmin = -20.0
        xmax = 20.0
        count = 2000000

        xlist = np.linspace(xmin, xmax, count)
        ylist = [self.func(x) for x in xlist]
        plt.plot(xlist, ylist, color = 'yellow')
        plt.grid()
        plt.show()

    def __del__(self):                     
        print('!')

def lf():
    u = Uravnenie(1,-2,1,0)
    u.cor()
    u.paint()
    r = Proizvod(1,-2,1,0)
    r.paint()
    i = Integral(1,-2,1,0)
    i.paint()
lf()
