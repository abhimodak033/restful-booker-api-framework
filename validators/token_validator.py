


class Validator:
    @staticmethod
    def create_token_validator(response,response_body):
        assert response.status_code == 200
        assert "token" in response_body 
        print(response_body)