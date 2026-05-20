import os
from pathlib import Path
from dotenv import load_dotenv

root_dir = Path(__file__).parent.parent

load_dotenv(root_dir / '.env', override=True)


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{root_dir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv('CSRF_SECRET_KEY', 'default_csrf_secret_key')


config = Config()
