



class Validator:
    @staticmethod
    def create_booking_validator(response,body):
        assert response.status_code == 200
        res_body = response.json()
        assert res_body["booking"]["firstname"] == body["firstname"]
        assert res_body["booking"]["lastname"] == body["lastname"]
        assert res_body["booking"]["totalprice"] == body["totalprice"]
        assert res_body["booking"]["depositpaid"] is True
        assert "bookingid" in res_body
        return res_body["bookingid"]
    
    
    @staticmethod
    def get_booking_validator(response):
        assert response.status_code == 200
        
    
    @staticmethod    
    def update_booking_validator(response,body):
        assert response.status_code == 200
        res_body = response.json()
        assert res_body["firstname"] == body["firstname"]
        assert res_body["lastname"] == body["lastname"]
        assert res_body["totalprice"] == body["totalprice"]
        assert res_body["depositpaid"] is True
        
    
    @staticmethod
    def partial_update_booking_validator(response,body):
        assert response.status_code == 200
        res_body = response.json()
        assert res_body["firstname"] == body["firstname"]
        assert res_body["lastname"] == body["lastname"]
        
    
    @staticmethod   
    def delete_booking_validator(response):
        assert response.status_code == 201