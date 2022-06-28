import os
from dotenv import load_dotenv

load_dotenv()


####### Settings #######

class Settings:
    
    def __init__(self):
        self.message_broker_host: str = os.getenv("MESSAGE_BROKER_HOST")
        self.commerce_queue: str = os.getenv("COMMERCES_QUEUE")
