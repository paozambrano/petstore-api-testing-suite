import pytest
import json
import os
from apis.pet_api import PetApi

@pytest.fixture
def pet_api():
    return PetApi()

@pytest.fixture
def pet_data():
    data_path = os.path.join(os.path.dirname(__file__),'../data/pet_data.json')

    with open(data_path, "r") as file:
        data = json.load(file)
    return data

@pytest.fixture
def pet_setup_teardown(pet_api, pet_data):
    response = pet_api.create_pet(pet_data)
    pet_id = response.json()["id"]

    yield response, pet_id

    print(f"\n Cleaning: Deleting pet with ID {pet_id}")
    pet_api.delete_pet(pet_id)