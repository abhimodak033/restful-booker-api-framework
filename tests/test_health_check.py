import pytest
from endpoints.health_check_endpoint import HealthCheckEndpoint
from validators.healthcheck_validator import Validator


class TestHealthCheck:
    def test_health_check(self):
        response = HealthCheckEndpoint.health_check_endpoint()
        Validator.health_check_validator(response)
        