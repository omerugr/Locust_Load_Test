from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def post_user_create(self):
        payload = {
            "id": 123312321,
            "username": "testcan123",
            "firstName": "test",
            "lastName": "can",
            "email": "can.test@test.com",
            "password": "123",
            "phone": "121312123123",
            "userStatus": 1
            }
        self.client.post("/v2/user", json=payload)

    @task
    def get_user_info(self):
        self.client.get("/v2/user/testcan123")

    @task
    def get_login(self):
        payload = {
            "username": "testcan123",
            "password": "123"
            }
        self.client.get("/v2/user/login", params=payload)

    @task
    def get_logout(self):
        self.client.get("/v2/user/logout")

    @task
    def put_user_update(self):
        payload = {
            "id": 3213213211,
            "username": "testcan123",
            "firstName": "test",
            "lastName": "can",
            "email": "test@can.com",
            "password": "123",
            "phone": "321213231123213",
            "userStatus": 0
            }
        self.client.put("/v2/user/testcan123", json=payload)

    # @task
    # def delete_user(self):
    #     payload = {
    #         "id": 123312321,
    #         "username": "testcan1234",
    #         "firstName": "test",
    #         "lastName": "can",
    #         "email": "can.test@test.com",
    #         "password": "123",
    #         "phone": "121312123123",
    #         "userStatus": 1
    #         }
    #     self.client.post("/v2/user", json=payload)
    #     self.client.delete("/v2/user/testcan1234")

    @task
    def post_create_with_array(self):
        payload = [
            {
                "id": 1,
                "username": "sasadas",
                "firstName": "ads",
                "lastName": "ad",
                "email": "asdsad@test.com",
                "password": "123",
                "phone": "132123321321",
                "userStatus": 0
            }]
        self.client.post("/v2/user/createWithArray", json=payload)