import unittest
from webtest import TestApp


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from drumio import main

        app = main({})
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get("/", status=200)
        self.assertTrue(b"Upload" in res.body)
