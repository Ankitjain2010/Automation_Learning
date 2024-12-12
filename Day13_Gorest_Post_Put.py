import requests
import pytest

# Base URL for the API
BASE_URL = "https://gorest.co.in/public"


def test_create_and_update_booking():
    """Test case to create a booking and then update it."""

    # --- Step 1: Create a Booking ---
    create_endpoint = f"{BASE_URL}/v2/users"
    create_payload = {
        "id":7566332,
        "name":"Shrishti Bhattathiri",
        "email":"bhattathiri_shrishti@haag-daniel.example",
        "gender":"male",
        "status":"inactive"
    }

    create_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer bcd08f91e6d0930814c69491241716fe90d438e75c28b1f115490f8e85e2076b"
    }

    # Perform POST request
    create_response = requests.post(create_endpoint, headers=create_headers, json=create_payload)

    # Validate POST response
    assert create_response.status_code == 200, "Failed to create booking"
    booking_data = create_response.json()
    booking_id = booking_data.get("id")
    print(f"Created Booking ID: {id}")

    # --- Step 2: Update the Created Booking ---
    update_endpoint = f"{BASE_URL}/v2/users/{id}"
    update_payload = {
        "id":7566332,
        "name":"Ankit Jain",
        "email":"ankit@test.com",
        "gender":"male",
        "status":"inactive"
    }

    # Add Authorization Header for PUT request
    update_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer bcd08f91e6d0930814c69491241716fe90d438e75c28b1f115490f8e85e2076b"
    }

    # Perform PUT request
    update_response = requests.put(update_endpoint, headers=update_headers, json=update_payload)

    # Validate PUT response
    assert update_response.status_code == 200, "Failed to update booking"
    updated_data = update_response.json()
    print(f"Updated Booking Data: {updated_data}")
