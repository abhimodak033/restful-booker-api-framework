import requests
from config.config import base_url,headers
from api_client.api_client import ApiClient




class AuthEndpoint:
    @staticmethod
    def create_token_endpoint(body):
        response = ApiClient.post(
            f"{base_url}/auth",
            json=body,
            headers=headers
        )
        return response