# coding: utf-8
import unittest
import os

from main import Main, ViewManager


class TestView(unittest.TestCase):

    def setUp(self):
        pass

    def test_chose_main_view(self):
        try:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hello.json')
            os.remove(path)
        except:
            print("Don`t have 'hello.json' file to delete")
        answer_no_user = 'sing_up'
        app = ViewManager()

        test_view = app.target_view

        self.assertEqual(test_view, answer_no_user)

        answer_had_user = 'home'

        app.store.put('user', name='Ванька', sex='male', age=17)
        app.chose_main_view()
        test_view = app.target_view

        self.assertEqual(test_view, answer_had_user)



if __name__ == '__main__':
    unittest.main()
