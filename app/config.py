import os

from dotenv import load_dotenv
load_dotenv()  

class Config:
    SECRET_KEY = "dfb1dee3d529bd885c1c6a6d3d4532c7e122e240e76f068d55bd98a9df6bc1db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "574dc4399b80456489175c3cd56a1264d30a89697585cc3d7b4a42e9b10c30b4"

    # إعدادات البريد الإلكتروني
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
