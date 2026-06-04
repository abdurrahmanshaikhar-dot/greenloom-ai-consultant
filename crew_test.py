from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

llm = LLM(
    model="openrouter/meta-llama/llama-3.3-70b-instruct:free"
)

agent = Agent(
    role="Tester",
    goal="Answer questions",
    backstory="You answer questions.",
    llm=llm
)

task = Task(
    description="Explain Netflix in 3 sentences.",
    expected_output="3 sentences",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential
)

result = crew.kickoff()

print(result)