from dotenv import load_dotenv
from duckduckgo_search import DDGS

from crewai import Agent, Task, Crew, Process, LLM

import os

load_dotenv()

# ==================================================
# WEB SEARCH
# ==================================================

def search_company(company):
    try:
        with DDGS() as ddgs:
            results = list(
                ddgs.text(
                    f"{company} latest business news strategy competitors",
                    max_results=8
                )
            )

        search_text = ""

        for result in results:
            search_text += f"""
Title: {result.get('title')}
URL: {result.get('href')}
Snippet: {result.get('body')}

----------------------------------------
"""

        return search_text

    except Exception as e:
        return f"Search Error: {str(e)}"


# ==================================================
# MAIN CREWAI FUNCTION
# ==================================================

def generate_report(company, problem):

    search_results = search_company(company)

    llm = LLM(
        model="openrouter/meta-llama/llama-3.3-70b-instruct",
        temperature=0.3,
        max_tokens=1500
    )

    # ==================================================
    # AGENTS
    # ==================================================

    research_agent = Agent(
        role="Business Research Analyst",
        goal="Conduct company and market research.",
        backstory="""
        You analyze companies, industries,
        competition, risks and opportunities.
        Use web research heavily.
        """,
        llm=llm,
        verbose=True
    )

    strategy_agent = Agent(
        role="Business Strategy Consultant",
        goal="Analyze business problems and create recommendations.",
        backstory="""
        You are a management consultant.
        You identify growth opportunities,
        risks and strategic actions.
        """,
        llm=llm,
        verbose=True
    )

    report_agent = Agent(
        role="Executive Report Writer",
        goal="Create professional business reports.",
        backstory="""
        You write reports suitable for executives,
        founders and investors.
        """,
        llm=llm,
        verbose=True
    )

    # ==================================================
    # TASKS
    # ==================================================

    research_task = Task(
        description=f"""
Company: {company}

Business Problem:
{problem}

Web Research:
{search_results}

Create:

1. Company Overview
2. Business Model
3. Top Competitors
4. Recent News

Maximum 500 words.
""",
        expected_output="Research summary.",
        agent=research_agent
    )

    strategy_task = Task(
        description=f"""
Business Problem:
{problem}

Using research findings identify:

1. Root Causes
2. Risks
3. Opportunities

Maximum 600 words.
""",
        expected_output="Strategic analysis.",
        context=[research_task],
        agent=strategy_agent
    )

    report_task = Task(
        description=f"""
Create a consulting report.

Company:
{company}

Problem:
{problem}

Include:

1. Executive Summary
2. Problem Analysis
3. Recommended Actions
4. Expected Business Impact
5. Conclusion

Maximum 1200 words.
""",
        expected_output="Final report.",
        context=[research_task, strategy_task],
        agent=report_agent
    )

    crew = Crew(
        agents=[
            research_agent,
            strategy_agent,
            report_agent
        ],
        tasks=[
            research_task,
            strategy_task,
            report_task
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    os.makedirs("reports", exist_ok=True)

    file_name = f"reports/{company.replace(' ', '_')}_report.md"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(str(result))

    return str(result)


# ==================================================
# TERMINAL TEST
# ==================================================

if __name__ == "__main__":

    company = input("Company Name: ")
    problem = input("Business Problem: ")

    report = generate_report(company, problem)

    print("\n" + "=" * 80)
    print(report)