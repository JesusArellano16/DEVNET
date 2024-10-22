import os
from dotenv import load_dotenv

load_dotenv()
user=os.getenv("USERS")
pswd=os.getenv("PSWDS")

def amb_var():
    return user,pswd