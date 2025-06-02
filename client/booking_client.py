
from utils.custom_requester import CustomRequester

class BookingClient:
    def __init__(self, base_url):
        self.requester = CustomRequester(base_url)
        self.token = None

    def get_token(self, username, password):
        data = {"username": username, "password": password}
        response = self.requester.send("POST", "/auth", data=data, expected_status=200)
        self.token = response.json().get("token")
        return self.token

    def create_booking(self, booking_data, expected_status=200):
        return self.requester.send("POST", "/booking", data=booking_data, expected_status=expected_status)

    def get_booking(self, booking_id, expected_status=200):
        return self.requester.send("GET", f"/booking/{booking_id}", expected_status=expected_status)

    def update_booking_full(self, booking_id, data):
        headers = {"Cookie": f"token={self.token}"}
        return self.requester.send("PUT", f"/booking/{booking_id}", headers=headers, data=data, expected_status=200)

    def update_booking_partial(self, booking_id, data):
        headers = {"Cookie": f"token={self.token}"}
        return self.requester.send("PATCH", f"/booking/{booking_id}", headers=headers, data=data, expected_status=200)

    def delete_booking(self, booking_id):
        headers = {"Cookie": f"token={self.token}"}
        return self.requester.send("DELETE", f"/booking/{booking_id}", headers=headers, expected_status=201)

    def get_all_bookings(self):
        return self.requester.send("GET", "/booking", expected_status=200)