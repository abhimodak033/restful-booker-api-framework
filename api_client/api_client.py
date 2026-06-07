import requests
import pytest
from utils.logger import get_logger

logger = get_logger()
class ApiClient:
    @staticmethod
    def post(url,json,headers):
        try:
            logger.info(f"POST request url: {url}")
            
            response = requests.post(
                url,
                json=json,
                headers=headers,
                timeout=15
            )
            
            logger.info(f"Response Status Code: {response.status_code}\n")
            return response
        
        except requests.exceptions.Timeout:
            logger.error("Request Timeout")
            raise

        except requests.exceptions.ConnectionError:
            logger.error("Connection Error")
            raise

        except requests.exceptions.RequestException as e:
            logger.error(f"Request Failed: {e}")
            raise
    
    
    @staticmethod
    def get(url,headers):
        try:
            logger.info(f"GET request url: {url}")
            
            response = requests.get(
                url,
                headers=headers,
                timeout=15
            )
            logger.info(f"Response Status Code: {response.status_code}\n")
            return response
        
        except requests.exceptions.Timeout:
            logger.error("Request Timeout")
            raise
        
        except requests.exceptions.ConnectionError:
            logger.error("Connection Error")
            raise

        except requests.exceptions.RequestException as e:
            logger.error(f"Request Failed: {e}")
            raise
    
    
    @staticmethod
    def put(url,json,headers):
        try:
            logger.info(f"PUT request url: {url}")
            
            response = requests.put(
                url,
                json = json,
                headers= headers,
                timeout=15
            )
            logger.info(f"Response Status Code: {response.status_code}\n")
            return response
        
        except requests.exceptions.Timeout:
            logger.error("Timeout error")
            raise
        
        except requests.exceptions.ConnectionError:
            logger.error("Connection Error")
            raise

        except requests.exceptions.RequestException as e:
            logger.error(f"Request Failed: {e}")
            raise
    
    
    
    @staticmethod
    def patch(url,json,headers):
        try:
            logger.info(f"PATCH request url: {url}")
            
            response = requests.patch(
                url,
                json = json,
                headers= headers,
                timeout=15
            )
            logger.info(f"Response Status Code: {response.status_code}\n")
            return response
        
        except requests.exceptions.Timeout:
            logger.error("Timeout error")
            raise
        
        except requests.exceptions.ConnectionError:
            logger.error("Connection Error")
            raise

        except requests.exceptions.RequestException as e:
            logger.error(f"Request Failed: {e}")
            raise
    
    
    
    @staticmethod
    def delete(url,headers):
        try:
            logger.info(f"DELETE request url: {url}")
            
            response = requests.delete(
                url,
                headers= headers,
                timeout=15
            )
            logger.info(f"Response Status Code: {response.status_code}\n")
            return response
        
        except requests.exceptions.Timeout:
            logger.error("Timeout error")
            raise
        
        except requests.exceptions.ConnectionError:
            logger.error("Connection Error")
            raise

        except requests.exceptions.RequestException as e:
            logger.error(f"Request Failed: {e}")
            raise
    