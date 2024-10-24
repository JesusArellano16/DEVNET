import os
from dotenv import load_dotenv

load_dotenv()
user=os.getenv("USER")
pswd=os.getenv("PSWD")

def amb_var():
    return user,pswd