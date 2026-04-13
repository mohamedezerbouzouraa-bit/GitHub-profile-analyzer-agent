import aiohttp
from config.settings import GITHUB_TOKEN

class GitHubTool:
    BASE = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

    async def get_user(self, username):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE}/users/{username}",
                headers=self.headers
            ) as r:
                return await r.json()

    async def get_repos(self, username):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.BASE}/users/{username}/repos",
                headers=self.headers
            ) as r:
                return await r.json()
