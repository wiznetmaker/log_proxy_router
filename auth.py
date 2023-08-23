# auth.py
from models import Auth
from database import SessionLocal

def verify_auth(auth_token: str) -> bool:
    db = SessionLocal()
    auth_entry = db.query(Auth).filter(Auth.user_id == auth_token).first()
    if auth_entry and auth_entry.accepted:
        return True
    return False