from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    user_db: str = os.environ.get("USER")
    password_db: str  = os.environ.get("PASSWORD")
    host_db: str = os.environ.get("HOST")
    port_db: int = os.environ.get("PORT")
    name_db: str = os.environ.get("DB_NAME")