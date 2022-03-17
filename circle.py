class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
        
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError('Radius should be positive')
            
    @property
    def diameter(self):
        return 2 * self.radius
    
    @property
    def circumference(self):
        return 2 * 3.14 * self.radius
            
        
    def display(self):
        print(f"radius: {self.radius}, diameter: {self.diameter}, circumference: {self.circumference} and area: {self.area()}")
            
circle = Circle(4)
circle.display()
print(circle.radius)