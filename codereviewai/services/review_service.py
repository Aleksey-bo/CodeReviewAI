from typing import Protocol
from core.exceptions import server_error


class ReviewService(Protocol):
    def __init__(self, openai_interface, github_interface) -> None:
        self.openai_interface = openai_interface
        self.github_interface = github_interface

    async def review_handler(self, data, key) -> dict:
        try:
            github_repo = await self.github_interface(repo_link=data.github_repo_link)
            openai_repo = await self.openai_interface(
                data=data.model_dump(exclude=("github_repo_link")),
                git_repo=github_repo, key=key.openia_key
                )
            return openai_repo
        except Exception:
            raise server_error