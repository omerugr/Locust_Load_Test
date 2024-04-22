from locust import HttpUser, task, between

class PetstoreUser(HttpUser):
    wait_time = between(5, 15)

    @task(1)
    def post_pet_create(self):
        payload = {
            "id": 198494949,
            "category": {
                "id": 618118186,
                "name": "dogs"
            },
            "name": "Charlie",
            "photoUrls": [
                "https://picsum.photos/200/300"],
            "tags": [
                {
                    "id": 16188,
                    "name": "tag1"
                }
            ],
            "status": "available"
        }
        self.client.post("/v2/pet", json=payload)

    @task(2)
    def post_pet_upload_image(self):
        data = {
            "additionalMetadata": "Sevimli bir köpek resmi"
        }
        files = {
            'file': ('74acffada595e829189eda96abae8bc4.jpg',
                     open('', 'rb'),
                     'image/jpeg')
        }
        self.client.post("/v2/pet/198494949/uploadImage", data=data, files=files)

    @task(3)
    def put_pet_update(self):
        payload = {
            "id": 198494949,
            "category": {
                "id": 618118186,
                "name": "dogs"
            },
            "name": "Charlie",
            "photoUrls": [
                "https://picsum.photos/200/300"],
            "tags": [
                {
                    "id": 16188,
                    "name": "tag1"
                }
            ],
            "status": "available"
        }
        self.client.put("/v2/pet", json=payload)

    @task(4)
    def get_pet_info(self):
        self.client.get("/v2/pet/198494949")

    @task(5)
    def get_pet_by_status(self):
        self.client.get("/v2/pet/findByStatus", params={"status": "available"})

    @task(6)
    def post_pet_update_form(self):
        data = {
            "name": "Max",
            "status": "sold"
        }
        self.client.post("/v2/pet/198494949", json=data)

    @task(7)
    def delete_pet(self):
        self.client.delete("/v2/pet/198494949")
