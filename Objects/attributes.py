#%%
class Point:
    pass

p1=Point()
p2=Point()
p1.x=5
p2.x=3
p1.y=4
p2.y=6
print(p1.x,p1.y)
print(p2.x,p2.y)


# %%
import math
class Point:
    def move(self,x,y):
        self.x=x
        self.y=y
    def reset(self):
        self.x=0
        self.y=0
    def calculate_distance(self,other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)

point1 = Point()

point2 = Point()

point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(point1))
assert point2.calculate_distance(point1) == point1.calculate_distance(
    point2
)
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

# %%
