# coding: utf-8
import unittest

from main import ViewManager


class TestView(unittest.TestCase):

    # Пользаватель Ванька увлышал про новое приложение для простого изучения английских слов
    def setUp(self):
        pass

    # Он рещил попробовать и открыть его в первый раз. Приложение встречало его окном регистрации
    def test_get_target_view(self):
        answer = 'sing_up'
        app = ViewManager()

        test_view = app.target_view

        self.assertEqual(test_view, answer)


if __name__ == '__main__':
    unittest.main()
