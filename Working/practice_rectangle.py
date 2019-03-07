class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.length = 0


def main():

    rect1 = Rectangle()

    width = "Enter Width: " + int(input(""))
    length = "Enter Length: " + int(input(""))

    rect1.width = width
    rect1.length = length



