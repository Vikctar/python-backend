import unittest


from app import create_app, db


class BaseTest(unittest.TestCase):
    """Base test class that provides test setup methods"""

    def setUp(self) -> None:
        """Define test variables and initialize app"""
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

