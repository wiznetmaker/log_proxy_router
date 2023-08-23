# main.py
from fastapi import FastAPI
from models import Server
from auth import verify_auth
from exporter import export_logs

app = FastAPI()

@app.post("/add/")
async def add_server(server: Server, auth: str):
    if verify_auth(auth):
        # 저장 로직 및 성공 여부 처리
        return {"message": "Server added successfully."}
    else:
        return {"message": "Authentication failed."}

# remove, registeruser 엔드포인트도 유사하게 정의

@app.get("/admin/")
async def admin_interface(auth: str):
    if verify_auth(auth):
        # 관리자 인터페이스 로직 처리 및 템플릿 반환
        return {"template": "admin_interface.html"}
    else:
        return {"message": "Authentication failed."}

@app.post("/export/")
async def export_logs_endpoint(format: str, duration: str, auth: str):
    if verify_auth(auth):
        file_path = export_logs(format, duration)
        return FileResponse(file_path)
    else:
        return {"message": "Authentication failed."}