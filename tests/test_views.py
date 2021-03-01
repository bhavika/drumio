import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_process_song_view(self):
        from drumio.views.default import process_song_view

        request = testing.DummyRequest()
        info = process_song_view(request)
        self.assertEqual(info["ui"], "process")
