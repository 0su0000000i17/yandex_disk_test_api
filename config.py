import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv("TOKEN")
    
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"