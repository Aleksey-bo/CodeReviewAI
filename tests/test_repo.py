import os
import asyncio
from codereviewai.repositories.github_repo import github_get_repo
from codereviewai.repositories.openai_repo import openai_review_chat


def test_github_api():
    repo_link = "https://github.com/Aleksey-bo/sportsite"

    git_content, git_tree = asyncio.run(github_get_repo(repo_link=repo_link))

    assert isinstance(git_tree, str)
    assert isinstance(git_content, str)


def test_openai_repo():
    data = {
        "assignment_description": "Make technical review.",
        "github_repo_link": "https://github.com/Aleksey-bo/sportsite",
        "candidate_level": "Junior"
        }
    openai_key = str(os.getenv("OPENAI_KEY"))

    review_text = asyncio.run(openai_review_chat(data=data, key=openai_key))

    assert isinstance(review_text, str)