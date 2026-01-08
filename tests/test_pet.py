def test_create_and_get_pet(pet_api, pet_data):
    post_response = pet_api.create_pet(pet_data)
    assert post_response.status_code == 200, f"Error: Expected 200 but received {post_response.status_code}"

    pet_id = post_response.json()["id"]
    print(f"\n-Pet created with ID: {pet_api}")

    get_response = pet_api.get_pet_by_id(pet_id)
    assert get_response.status_code == 200

    response_body = get_response.json()
    assert response_body["name"] == pet_data["name"]
    assert response_body["status"] == pet_data["status"]

    print(f"Validation Successful validation: The name{response_body['name']} matches")