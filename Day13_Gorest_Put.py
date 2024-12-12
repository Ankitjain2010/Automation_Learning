# Put Method

import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://gorest.co.in/public"

def test_create_booking():
    """Test case to perform a GET request to /booking."""
    id = 7567022
    endpoint = f"{BASE_URL}/v2/users/{id}"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer bcd08f91e6d0930814c69491241716fe90d438e75c28b1f115490f8e85e2076b"
    }

    # Sample data to be sent in the POST request
    payload = {
        "id":7567022,
        "name":"Amit Bhattathiri",
        "email":"Amit@haag-daniel.example",
        "gender":"male",
        "status":"inactive"
    }

    # Perform Put request
    response = requests.put(endpoint, headers=headers, json=payload)

    # Log status code
    print(f"Status Code: {response.status_code}")

    # Log response content (body)
    print(f"Response Body: {response.text}")

    # Log response headers
    print(f"Response Headers: {response.headers}")

    # Optionally, you can also log JSON content if the response is in JSON format
    try:
        json_response = response.json()
        print(f"Response JSON: {json_response}")
    except ValueError:
        print("Response is not in JSON format.")
# -----------------------------------------------------------------------------------------
