import matplotlib.pyplot as plt
import numpy as np


class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def circ():

        fig, axes = plt.subplots()

        Drawing_colored_circle = plt.Circle(( 0.6 , 0.6 ), 0.2 )
    
        axes.set_aspect( 1 )
        axes.add_artist( Drawing_colored_circle )
        plt.title( 'Colored Circle' )
        plt.show()

    def __dell__(self):
        pass