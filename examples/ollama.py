import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

import asyncio
from browser_use import Agent
from langchain_ollama import ChatOllama


async def run_search() -> str:
    agent = Agent(
        task="Search for a 'browser use' post on the r/LocalLLaMA subreddit and open it.",
        llm=ChatOllama(
            model="llama3.2-vision:11b",
            num_ctx=32000,
        ),
    )

    result = await agent.run()
    return str(result)


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())
