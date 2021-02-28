import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views.default import process_song_view

        request = testing.DummyRequest()
        info = process_song_view(request)
        self.assertEqual(info["project"], "drumio")


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from drumio import main

        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get("/", status=200)
        self.assertTrue(b"Pyramid" in res.body)
