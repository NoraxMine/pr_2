import matplotlib.pyplot as plt
import numpy as np


class Uravnenie:
    def __init__(self, a, b, c, d):
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

class Proizvod(Uravnenie):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)

    def func(self, x):
        y = (self.a * x * 2) + (self.b) 
        return y

    def __del__(self):                     
        print('!')

class Integral(Uravnenie):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)

    def func(self, x):
        y = ((self.a * (x ** 3))/3) + ((self.b *(x ** 2))/2) + (self.c * x) + self.d
        return y

    def __del__(self):                     
        print('!')

def lf():
    def plot_all(a, b, c, d):
        x = np.linspace(-20, 20, 10_000)

        u = Uravnenie(a, b, c, d)
        p = Proizvod(a, b, c, d)
        i = Integral(a, b, c, d)

        u = u.func(x)  
        p = p.func(x)  
        i = i.func(x)  

        plt.figure(figsize=(10, 6))  
        plt.plot(x, u, color='red', label="Квадратичная функция")
        plt.plot(x, p, color='purple', label="Производная")
        plt.plot(x, i, color='yellow', label="Интеграл")
        plt.grid()
        plt.show()

    plot_all(1, -2, 1, 3)

lf()
