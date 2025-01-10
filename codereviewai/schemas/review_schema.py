from pydantic import BaseModel


class ReviewSchema(BaseModel):
    assignment_description: str
    github_repo_link: str
    candidate_level: str

    class Config:
        from_attributes = True


class ResponseReviewSchema(BaseModel):
    review_text: str

