import requests
import json

# 서버 주소 설정
BASE_URL = "http://localhost:8000"

# 인증 토큰 설정 (임시 값)
auth_token = "your_auth_token"

# Add 서버 요청 테스트
add_data = {"server_name": "TestServer", "port": 8080}
response = requests.post(f"{BASE_URL}/add/", json=add_data, headers={"Authorization": auth_token})
print(response.json())

# Remove 서버 요청 테스트
remove_data = {"server_name": "TestServer", "port": 8080}
response = requests.delete(f"{BASE_URL}/remove/", json=remove_data, headers={"Authorization": auth_token})
print(response.json())

# Register User 요청 테스트
register_data = {"user_id": "new_user", "password": "new_password"}
response = requests.post(f"{BASE_URL}/registeruser/", json=register_data, headers={"Authorization": auth_token})
print(response.json())

# Admin 인터페이스 요청 테스트
admin_response = requests.get(f"{BASE_URL}/admin/", headers={"Authorization": auth_token})
print(admin_response.json())

# 로그 내보내기 요청 테스트
export_params = {"format": "csv", "duration": "last_week"}
export_response = requests.post(f"{BASE_URL}/export/", json=export_params, headers={"Authorization": auth_token})
with open("exported_logs.csv", "wb") as file:
    file.write(export_response.content)
print("Logs exported.")