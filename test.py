import os
from dotenv import load_dotenv

load_dotenv()
data = {"hello":"world","test":"working"}

print(data.get('test'))