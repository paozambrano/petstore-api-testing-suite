import requests

class PetApi:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2/pet"
        self.headers = {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

    def create_pet(self, payload):
        response = requests.post(self.base_url, json=payload, headers=self.headers)
        return response
    
    def get_pet_by_id(self, pet_id):
        response = requests.get(f"{self.base_url}/{pet_id}", headers=self.headers)
        return response
    
    def delete_pet(self, pet_id):
        response = requests.delete(f"{self.base_url}/{pet_id}", headers=self.headers)
        return response