from dotenv import load_dotenv
import os

load_dotenv()

print("SERPER:", os.getenv("SERPER_API_KEY"))
print("OPENROUTER:", os.getenv("OPENROUTER_API_KEY"))