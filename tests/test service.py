import os
import asyncio
from codereviewai.services.review_service import ReviewService
from codereviewai.repositories.github_repo import github_get_repo
from codereviewai.repositories.openai_repo import openai_review_chat


def review_service_test():
    review_service = ReviewService(
        openai_interface=openai_review_chat,
        github_interface=github_get_repo
    )

    data = {
        "assignment_description": "Make technical review.",
        "github_repo_link": "https://github.com/Aleksey-bo/sportsite",
        "candidate_level": "Junior"
        }
    openai_key = str(os.getenv("OPENAI_KEY"))

    review_handler_test = asyncio.run(review_service.review_handler(data=data, key=openai_key))

    assert isinstance(review_handler_test, dict)
    assert isinstance(review_handler_test["git_tree"], dict)
    assert isinstance(review_handler_test["review_text"], str)