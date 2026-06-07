import json
from jsonschema import ValidationError, validate
from utils.logger import get_logger

logger = get_logger()
class Schemavalidator:
    @staticmethod
    def booking_schema_validator(response_body):
        with open("./utils/json_create_booking_schema.json",mode="r") as json_file:
           response_schema = json.load(json_file)
           
        try:
            validate(instance=response_body,schema=response_schema)
            logger.info("JSON schema validation passed")
        except ValidationError as e: 
            logger.error(f"JSON schema validation failed :{e}")
            assert False
            
            
    def schema_validator(response_body):
        with open("./utils/json_booking_schema.json",mode="r") as json_file:
           response_schema = json.load(json_file)
           
        try:
            validate(instance=response_body,schema=response_schema)
            logger.info("JSON schema validation passed")
        except ValidationError as e: 
            logger.error(f"JSON schema validation failed :{e}")
            assert False