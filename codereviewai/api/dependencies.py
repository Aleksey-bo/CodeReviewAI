from services.review_service import ReviewService
from repositories.github_repo import github_get_repo
from repositories.openai_repo import openai_review_chat


def review_depend():
    return ReviewService(
        openai_interface=openai_review_chat,
        github_interface=github_get_repo
    )