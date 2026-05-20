import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyDsmI1qeJ23F4XLk-TH9znlCRfBQfJ7oGw  "))

for m in genai.list_models():
    print(m.name)