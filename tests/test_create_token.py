from endpoints.auth_endpoint import AuthEndpoint
from payloads.user_payload import Userpayload
from validators.token_validator import Validator

token = None

class TestTokenValidation:
    def test_create_token(self):
        body = Userpayload.create_token_payload()
        response = AuthEndpoint.create_token_endpoint(body)
        response_body = response.json()
        Validator.create_token_validator(response,response_body)

    
    
