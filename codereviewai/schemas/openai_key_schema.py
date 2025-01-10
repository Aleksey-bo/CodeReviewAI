from pydantic import BaseModel


class OpenAISchema(BaseModel):
    openia_key: str