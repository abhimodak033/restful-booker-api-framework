import pytest
from config.config import base_url
from api_client.api_client import ApiClient



class HealthCheckEndpoint:
    @staticmethod
    def health_check_endpoint():
        response = ApiClient.get(
            f"{base_url}/ping",
            headers=None
        )
        return response