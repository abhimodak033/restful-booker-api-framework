import pytest
from payloads.user_payload import Userpayload
from endpoints.booking_endpoints import BookingEndpoints
from validators.booking_validator import Validator
from validators.schema_validator import Schemavalidator

booking_id = None

class TestUserBooking:
    @pytest.mark.regression
    def test_create_booking(self):
        global booking_id
        body = Userpayload.create_booking_payload()
        response = BookingEndpoints.create_booking_endpoint(body)
        Schemavalidator.booking_schema_validator(response.json())
        booking_id = Validator.create_booking_validator(response,body)

        
        
    @pytest.mark.smoke   
    def test_get_booking_ids(self):
        response = BookingEndpoints.get_booking_endpoint()
        Validator.get_booking_validator(response)
        

    @pytest.mark.regression    
    def test_get_booking_by_id(self):
        response = BookingEndpoints.get_booking_endpoint(booking_id)  
        Schemavalidator.schema_validator(response.json())      
        Validator.get_booking_validator(response)
        res_body = response.json()
        print(res_body)
 
        
    @pytest.mark.regression
    def test_update_booking(self,auth_header_fixture):
        body = Userpayload.update_booking_payload()
        response = BookingEndpoints.update_booking_endpoint(body,booking_id,auth_header_fixture)
        Schemavalidator.schema_validator(response.json())
        Validator.update_booking_validator(response,body)
  
        
    @pytest.mark.regression   
    def test_partial_update_booking(self,auth_header_fixture):
        body = Userpayload.partial_update_booking_payload()
        response = BookingEndpoints.update_partial_booking_endpoint(body,booking_id,auth_header_fixture)
        Schemavalidator.schema_validator(response.json())
        Validator.partial_update_booking_validator(response,body)

        
    @pytest.mark.regression    
    def test_delete_booking(self,auth_header_fixture):
        response = BookingEndpoints.delete_booking_endpoint(booking_id,auth_header_fixture)
        Validator.delete_booking_validator(response)
        
    