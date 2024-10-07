### Write OOP classes to handle the following scenarios:

# - A user can create and view 2D coordinates
# we wants the points to be printed in a way as <2,1> etc
# - A user can find out the distance between 2 coordinates
# - A user can find find the distance of a coordinate from origin
# - A user can check if a point lies on a given line
# - A user can find the distance between a given 2D point and a given line


class TwoDCoordinates:
    # init constuctor
    def __init__(self,x,y) :
        # the data realted to 2d points can be x coodrinate valuue and the y coordinate value
        self.x_cord=x
        self.y_cord=y 
    def __str__(self) :
        return '<{},{}>'.format(self.x_cord,self.y_cord)
    
    # meathod to find the eculadian distance between two points
    # for ecu distance we need two points one point here is selff(x,y) other is the other (z,x) type
    def Eculadian_Distance(self,other):
        return ((self.x_cord -  other.x_cord,) ** 2 + (self.y_cord - other.y_cord) **2)** 0.5
    
    #To find the distance of the of coordinates from origin
    def OriginDistance(self):
        return self.Eculadian_Distance(Point(0,0))
    
    # to check if a point lies on a given line
class line():
    # constructor
    def __init__(self,A,B,C) -> None:
        self.A=A
        self.B=B
        self.C=C
    def __str__(self) -> str:
        return '{}x + {}y + {}z = 0'.format(self.A,self.B,self.C)

    def point_on_line(line,point):
        if line.A*point.x_cord+line.B*point.y_cord+C==0:
            return "lies on the line"
        else:
            return "doesnot lies on the line"
        #please solve this shit on your own
         
    def shortest_distance(line,point):
        abs(line.A)
        

# object for the class

point1=TwoDCoordinates(3,4)
point2=TwoDCoordinates(-2,9)
# passing the other value into the eculadian distance
point1.Eculadian_Distance((3,-5))
point1.OriginDistance()
print(point1)
print(point2)