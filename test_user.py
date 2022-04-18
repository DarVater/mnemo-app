# coding: utf-8
import unittest

from main import Main, ViewManager


class TestView(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_get_target_view(self):
        app = ViewManager()

        print(111111111111, app.target_view)



if __name__ == '__main__':
    unittest.main()
