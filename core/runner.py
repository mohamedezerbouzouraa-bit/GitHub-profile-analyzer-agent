
class Runner:
    def __init__(self, agent):
        self.agent = agent
    async def run_async(self, user_id, session_id, message):
        result = await self.agent.run(user_id, session_id, message)
        yield result
