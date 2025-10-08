import httpx

from config import settings

# Проходим аутентификацию
login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post(f"{settings.http_client.url}api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Инициализируем клиент с base_url
client = httpx.Client(
    base_url=settings.http_client.url,
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

# Выполняем запрос с авторизацией
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print('Get user me data:', get_user_me_response_data)
