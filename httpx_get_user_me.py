import httpx

from config import settings

login_payload = {
    "email": "ii@ii.ii",
    "password": "ivanov"
}

login_response = httpx.post(f"{settings.http_client.url}api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

headers = {
    "Authorization": f"{login_response_data['token']['tokenType']} {login_response_data['token']['accessToken']}"
}

user_response = httpx.get(f"{settings.http_client.url}api/v1/users/me", headers=headers)
user_response_data = user_response.json()

print("User response:", user_response_data)
print("Status Code:", user_response.status_code)

