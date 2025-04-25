class Booking:
    def __init__(self, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.bookingdates = {
            "checkin": checkin,
            "checkout": checkout
        }
        self.additionalneeds = additionalneeds

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates,
            "additionalneeds": self.additionalneeds
        }