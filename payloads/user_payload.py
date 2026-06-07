from faker import Faker

faker = Faker()
class Userpayload:
    @staticmethod  
    def create_token_payload():
        payload ={
            "username" : "admin",
            "password" : "password123"
        }
        return payload
    
    @staticmethod
    def create_booking_payload():
        payload = {
            "firstname" : faker.first_name(),
            "lastname" : faker.last_name(),
            "totalprice" : faker.random_number(digits=3),
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : str(faker.date()),
                "checkout" : str(faker.future_date())
            },
            "additionalneeds" : "Breakfast"
        }
        
        return payload

    @staticmethod
    def update_booking_payload():
        payload={
            "firstname" : faker.first_name(),
            "lastname" : faker.last_name(),
            "totalprice" : faker.random_number(digits=3),
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : str(faker.date()),
                "checkout" : str(faker.future_date())
            },
            "additionalneeds" : "Breakfast"
        }
        
        return payload
    
    @staticmethod
    def partial_update_booking_payload():
        paylaod = {
            "firstname" : faker.first_name(),
            "lastname" : faker.last_name()
        }
        
        return paylaod