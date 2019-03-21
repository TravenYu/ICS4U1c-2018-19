import math

class Point():

    def __init__(self, px, py):
        """
        Create an instance of a Point
        :param px: x coordinate value
        :param py: y coordinate value
        """
        self.x = px
        self.y = py

    def get_distance(self, other_point):
        """
        Compute the distance between the current object and another Point
        :param other_point: Point object to find the distance to
        :return: float
        """
        distance = math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        return distance

def main():
    """
    Program demonstrating the creation of Point instances and calling class methods
    """
    p1 = Point(5, 10)
    p2 = Point(3, 4)

    dist = p1.get_distance(p2)
    print("The distance between the points is: " + str(dist))

main()
