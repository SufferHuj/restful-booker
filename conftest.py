import pytest
from client.booking_client import BookingClient
from utils.data_generator import generate_booking_data
import logging

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def client():
    bc = BookingClient(BASE_URL)
    bc.get_token("admin", "password123")
    return bc

@pytest.fixture
def booking_data():
    return generate_booking_data()

@pytest.fixture
def created_booking(client, booking_data):
    response = client.create_booking(booking_data)
    booking_id = response.json()["bookingid"]
    return booking_id, booking_data