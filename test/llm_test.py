from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
    model="openrouter/meta-llama/llama-3.3-70b-instruct",
    temperature=0.3,
    max_tokens=1000
)

response = llm.call(
    "Say hello"
)

print(response)