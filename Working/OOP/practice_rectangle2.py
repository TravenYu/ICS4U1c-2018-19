class Rectangle():

    def __init__(self, dwidth, dlength):
        self.width = dwidth
        self.length = dlength

    def get_area(self):

        return self.width * self.length

def main():
        my_rect1 = Rectangle(2.5)

        print("The area is " + str(my_rect1.get_area()))

main()
