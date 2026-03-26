import asyncio
import nest_asyncio
nest_asyncio.apply()

from agents.github_agent import GitHubProfileAgent
from core.runner import Runner
from models.messages import Content, Part


async def main():

    agent = GitHubProfileAgent()
    runner = Runner(agent)

    url = input("Enter GitHub profile URL: ")

    message = Content(
        role="user",
        parts=[Part(url)]
    )

    async for event in runner.run_async(
        user_id="user_1",
        session_id="session_1",
        message=message
    ):
        print("\n🧠 FINAL OUTPUT:\n")
        print(event.parts[0].text)


asyncio.run(main())
