import os
from fastapi.testclient import TestClient
from codereviewai.main import app


client = TestClient(app)


def test_root():
    data = {
        "assignment_description": "Make technical review.",
        "github_repo_link": "https://github.com/Aleksey-bo/sportsite",
        "candidate_level": "Junior"
        }
    openai_key = str(os.getenv("OPENAI_KEY"))

    request_data = {"data": data, "openai_key": {"openai_key": openai_key}}
    response = client.post("/review", data=request_data)
    assert response.status_code == 200
    response_data = response.json()

    assert isinstance(response_data["git_tree"], str)
    assert isinstance(response_data["review_text"], str)