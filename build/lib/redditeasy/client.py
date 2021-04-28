from enum import Enum
from dotenv import load_dotenv
import os

direct = os.path.dirname(__file__)
load_dotenv(os.path.join(direct, ".env"))


class Client(Enum):
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    USER_AGENT = os.getenv("USER_AGENT")
