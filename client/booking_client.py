import requests

class BookingClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def get_token(self, username, password):
        response = requests.post(f"{self.base_url}/auth", json={
            "username": username,
            "password": password
        })
        response.raise_for_status()
        self.token = response.json()["token"]
        return self.token

    def create_booking(self, booking_data):
        return requests.post(f"{self.base_url}/booking", json=booking_data)

    def get_booking(self, booking_id):
        return requests.get(f"{self.base_url}/booking/{booking_id}")

    def update_booking_full(self, booking_id, data):
        headers = {"Cookie": f"token={self.token}"}
        return requests.put(f"{self.base_url}/booking/{booking_id}", headers=headers, json=data)

    def update_booking_partial(self, booking_id, data):
        headers = {"Cookie": f"token={self.token}"}
        return requests.patch(f"{self.base_url}/booking/{booking_id}", headers=headers, json=data)

    def delete_booking(self, booking_id):
        headers = {"Cookie": f"token={self.token}"}
        return requests.delete(f"{self.base_url}/booking/{booking_id}", headers=headers)

    def get_all_bookings(self):
        return requests.get(f"{self.base_url}/booking")