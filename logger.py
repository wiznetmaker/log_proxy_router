# logger.py
from models import Log
from database import SessionLocal
from datetime import datetime

def log_message(message: str):
    db = SessionLocal()
    log_entry = Log(timestamp=datetime.now(), message=message)
    db.add(log_entry)
    db.commit()
    db.close()