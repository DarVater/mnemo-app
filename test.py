# coding: utf-8
import unittest
import os

from main import MyApp, ViewManager


class TestView(unittest.TestCase):

    def setUp(self):
        pass



if __name__ == '__main__':
    unittest.main()

import unittest

from functools import partial
from kivy.clock import Clock
import os
import sys
import time
import os.path as op

# when you have a test in <root>/tests/test.py
main_path = op.dirname(op.dirname(op.abspath(__file__)))
sys.path.append(main_path)

from main import MyApp


class Test(unittest.TestCase):
    def pause(*args):
        time.sleep(0.000001)

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

    # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something

        # Comment out if you are editing the test, it'll leave the
        # Window opened.
        app.stop()

    def test_example(self):
        app = MyApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()
        print(app.root.ids['temp_view'].btn.text)

if __name__ == '__main__':
    unittest.main()
