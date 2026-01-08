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