import matplotlib.pyplot as plt

#class classname(parent class):
class Circle(object):

    #constructor 
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    #self -> self referencing to current obj
    
    def get_area(self):
        return 3.14*self.radius*self.radius
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
    

obj = Circle(2, "red")
dir(Circle)
print(obj.radius, obj.color)
print(obj.get_area())

if(4 > 3):
    t = 4
print(t)
