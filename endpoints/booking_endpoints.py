import requests
from config.config import base_url,headers
from api_client.api_client import ApiClient



class BookingEndpoints:
    @staticmethod
    def create_booking_endpoint(body):
        response = ApiClient.post(
            f"{base_url}/booking",
            json=body,
            headers=headers)
        return response
    
    @staticmethod
    def get_booking_endpoint(booking_id =None):
        if booking_id is None:
            response = ApiClient.get(
                f"{base_url}/booking",
                headers=headers
            )
        else:
            response = ApiClient.get(
                f"{base_url}/booking/{booking_id}",
                headers= headers
            )
        return response
    
    @staticmethod
    def update_booking_endpoint(body,booking_id,fixture):
        response = ApiClient.put(
            f"{base_url}/booking/{booking_id}",
            json =body,
            headers=fixture
        )
        return response
    
    @staticmethod
    def update_partial_booking_endpoint(body,booking_id,fixture):
        response = ApiClient.patch(
            f"{base_url}/booking/{booking_id}",
            json =body,
            headers=fixture
        )
        return response
    
    @staticmethod
    def delete_booking_endpoint(booking_id,fixture):
        response =ApiClient.delete(
            f"{base_url}/booking/{booking_id}",
            headers=fixture
        )
        return response