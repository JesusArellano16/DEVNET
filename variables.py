import os
from dotenv import load_dotenv

load_dotenv()
user=os.getenv("USR")
pswd=os.getenv("PSWD")

def amb_var():
    return user,pswd