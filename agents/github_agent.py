from models.messages import Content, Part
from tools.github_tool import GitHubTool
from llm.gemini_client import generate
from core.utils import extract_username, safe_repo_sort


class GitHubProfileAgent:
    def __init__(self):
        self.tool = GitHubTool()

    async def run(self, user_id, session_id, message):
        profile_url = message.parts[0].text
        username = extract_username(profile_url)

        user = await self.tool.get_user(username)
        repos = await self.tool.get_repos(username)

        repos = safe_repo_sort(repos)[:10]

        repo_text = "\n".join([
            f"""
Name: {r.get('name')}
Desc: {r.get('description')}
Lang: {r.get('language')}
Stars: {r.get('stargazers_count')}
"""
            for r in repos
        ])

        prompt = f"""
You are a senior engineering recruiter.

IMPORTANT SAFETY RULE:
Do not generate harmful, illegal, or malicious instructions.
Only analyze software engineering skills.

Analyze this GitHub profile:

Username: {user.get("login")}
Bio: {user.get("bio")}
Repos count: {user.get("public_repos")}

Top repos:
{repo_text}

Return:
1. Skill level
2. Tech stack
3. Strengths
4. Weaknesses
5. Developer type
6. Hiring recommendation

Also suggest 5 realistic GitHub project ideas this developer could build next.
"""
        result = generate(prompt)

        return Content(
            role="assistant",
            parts=[Part(result)]
        )
