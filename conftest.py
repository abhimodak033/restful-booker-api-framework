import requests
import pytest
from payloads.user_payload import Userpayload
from config.config import base_url
from config.config import headers

@pytest.fixture(scope = "session")
def create_token_fixture():
    body = Userpayload.create_token_payload()
    response = requests.post(f"{base_url}/auth",json=body,headers=headers)
    generated_token = response.json()["token"]
    return generated_token

@pytest.fixture
def auth_header_fixture(create_token_fixture):
    token = create_token_fixture
    auth_header = {
    "Content-Type":"application/json",
    "Cookie" : f"token={token}"
    }
    return auth_header