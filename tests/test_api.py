import unittest

from tests.configure import BaseTest


class ApiTestCase(BaseTest):
    """This class represents the api test case"""

    new_trip = {
        "vehicle_id": 1,
        "driver_id": 1,
        "customer_id": 1,
        "address_type": "PICKUP_POINT",
        "done_by_user_id": 1,
        "address": "Mombasa",
        "cargo_tonnage": 1000.00
    }

    def test_demo_route(self):
        response = self.client().get('/api/v1/demo')
        self.assertEqual(response.status_code, 200)

    def test_record_trip(self):
        response = self.client().post('/api/v1/record-trip?api_token=some-token', json=self.new_trip)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
