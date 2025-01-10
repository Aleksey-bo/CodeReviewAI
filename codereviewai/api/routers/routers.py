from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import status, Depends

from api.dependencies import review_depend
from schemas.review_schema import ReviewSchema, ResponseReviewSchema
from schemas.openai_key_schema import OpenAISchema


router = APIRouter(prefix="/review")


@router.post("/", status_code=status.HTTP_200_OK)
async def review(data: ReviewSchema, openai_key: OpenAISchema, review_dep=Depends(review_depend)) -> ResponseReviewSchema:
    review_service: dict = await review_dep.review_handler(data=data, key=openai_key)
    return ResponseReviewSchema(review_text=review_service)