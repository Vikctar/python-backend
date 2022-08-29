import unittest

from flask import current_app

from tests.configure import BaseTest


class AppTestCase(BaseTest):

    def test_app_exists(self):
        self.assertFalse(self.app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
