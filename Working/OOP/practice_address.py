
class Address():

    def __init__(self):
        self.address_line1 = ""
        self.address_line2 = ""
        self.postal_code = ""
        self.city = ""
        self.province = ""
        self.country = ""

def print_address(addr):
    print(addr.address_line1)
    if addr.address_line2 != "":
        print(addr.address_line2)
    print(addr.city + ", " + addr.postal_code + ", " + addr.province)
    print(addr.country)

def main():

    home_address = Address()
    home_address.address_line1 = "123 Main St."
    home_address.address_line2 = "Unit #2"
    home_address.postal_code = "L3R 8M1"
    home_address.city = "Markham"
    home_address.province = "Ontario"
    home_address.country = "Canada"

    work_address = Address()
    work_address.address_line1 = "8101 Leslie St."
    work_address.postal_code = "L4A 9E3"
    work_address.city = "Thornhill"
    work_address.province = "Ontario"
    work_address.country = "Canada"

    # print out the addresses
    print(" **** HOME ADDRESS ****")
    print_address(home_address)

    print("")

    print(" **** WORK ADDRESS ****")
    print_address(work_address)

main()