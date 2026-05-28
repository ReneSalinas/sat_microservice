from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    RFC = os.getenv("RFC")

    CERT_PASSWORD = os.getenv("CERT_PASSWORD")

    CERT_PATH = os.getenv("CERT_PATH")
    KEY_PATH = os.getenv("KEY_PATH")


settings = Settings()