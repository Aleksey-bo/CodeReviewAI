from openai import AsyncOpenAI
from core.exceptions import server_error


async def openai_review_chat(data: dict, git_repo: list, key: str) -> str:
    try:
        client = AsyncOpenAI(api_key=key)
        completion = await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "developer",
                        "content": f"You are an experienced developer. Conduct a technical review of the repository, point out the flaws, and rate it from 0 to 5."
                    },
                    {
                        "role": "user",
                        "content": f"""
                                    Assignment description: {data["assignment_description"]}
                                    Candidate level: {data["candidate_level"]}
                                    GitHub: {git_repo}
                                    """
                    }
                ],
                max_completion_tokens=3000
            )
        print(completion.choices[0].message.content)
        return completion.choices[0].message.content
    except Exception as e:
        print(e)
        raise server_error
    