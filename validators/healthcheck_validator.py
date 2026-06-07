



class Validator:
    @staticmethod
    def health_check_validator(response):
        assert response.status_code == 201