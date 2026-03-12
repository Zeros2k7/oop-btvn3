import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, width=0, height=0, corner=Point()):
        self.width = width
        self.height = height
        self.corner = corner 
class Circle:
    def __init__(self, center, radius):
        self.center = center  
        self.radius = radius
def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
def point_in_circle(circle, point):
    d = distance_between_points(circle.center, point)
    return d <= circle.radius
def rect_in_circle(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x, rect.corner.y + rect.height)
    p3 = Point(rect.corner.x + rect.width, rect.corner.y)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    return (point_in_circle(circle, p1) and 
            point_in_circle(circle, p2) and 
            point_in_circle(circle, p3) and 
            point_in_circle(circle, p4))
def rect_circle_overlap(circle, rect):
    p1 = rect.corner
    p2 = Point(rect.corner.x, rect.corner.y + rect.height)
    p3 = Point(rect.corner.x + rect.width, rect.corner.y)
    p4 = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    
    if (point_in_circle(circle, p1) or point_in_circle(circle, p2) or 
        point_in_circle(circle, p3) or point_in_circle(circle, p4)):
        return True
    return False
center_point = Point(150, 100)
my_circle = Circle(center_point, 75)
test_point = Point(160, 110)
print(f"Điểm (160, 110) nằm trong hình tròn: {point_in_circle(my_circle, test_point)}")
my_rect = Rectangle(width=50, height=50, corner=Point(140, 90))
print(f"HCN nằm hoàn toàn trong hình tròn: {rect_in_circle(my_circle, my_rect)}")