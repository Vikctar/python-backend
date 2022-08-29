import unittest

from tests.configure import BaseTest


class ApiTestCase(BaseTest):
    """This class represents the api test case"""
    def test_demo_route(self):
        response = self.client().get('/api/v1/demo')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
