def test_create_booking(client, booking_data):
    response = client.create_booking(booking_data)
    assert response.status_code == 200
    assert "bookingid" in response.json()

def test_get_booking(client, created_booking):
    booking_id, booking_data = created_booking
    response = client.get_booking(booking_id)
    assert response.status_code == 200
    assert response.json()["firstname"] == booking_data["firstname"]

def test_update_booking_full(client, created_booking, booking_data):
    booking_id, _ = created_booking
    booking_data["firstname"] = "Updated"
    response = client.update_booking_full(booking_id, booking_data)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Updated"

def test_update_booking_partial(client, created_booking):
    booking_id, _ = created_booking
    partial = {"firstname": "Patched"}
    response = client.update_booking_partial(booking_id, partial)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Patched"

def test_delete_booking(client, created_booking):
    booking_id, _ = created_booking
    response = client.delete_booking(booking_id)
    assert response.status_code == 201

    # Проверка удаления
    get_response = client.get_booking(booking_id)
    assert get_response.status_code == 404

def test_get_all_bookings(client):
    response = client.get_all_bookings()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_booking_with_invalid_data(client):
    bad_data = {
        "firstname": 123,
        "lastname": None,
        "totalprice": "cheap",
        "depositpaid": "yes",
        "bookingdates": {
            "checkin": "bad",
            "checkout": "date"
        },
        "additionalneeds": "none"
    }
    response = client.create_booking(bad_data)
    assert response.status_code in [400, 500]

def test_get_nonexistent_booking(client):
    response = client.get_booking(9999999)
    assert response.status_code == 404