from faker import Faker

fake = Faker()

def generate_booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=50, max=500),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": "2025-05-01",
            "checkout": "2025-05-05"
        },
        "additionalneeds": fake.word()
    }