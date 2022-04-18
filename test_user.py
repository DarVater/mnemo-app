# coding: utf-8
import time
import unittest
from functools import partial
from kivy.clock import Clock

from main import MyApp


class TestView(unittest.TestCase):
    def pause(*args):
        time.sleep(0.000001)

    # main test function
    def run_test(self, app, *args):
        Clock.schedule_interval(self.pause, 0.000001)

        # Do something

        # Comment out if you are editing the test, it'll leave the
        # Window opened.
        app.stop()

    # Пользаватель Ванька увлышал про новое приложение для простого изучения английских слов
    def setUp(self):
        pass

    # Он рещил попробовать и открыть его в первый раз. Приложение поприветствовало и спросило имя

    def test_example(self):
        app = MyApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()

        # дополнительных надписей небыло
        start_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(start_help_text, '')

        # Ванька ввел имя и фамилию
        test_word = 'ИванФамилия'
        start_header = app.root.ids['temp_view'].header.text
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()
        test_answer = app.root.ids['temp_view'].name

        next_header = app.root.ids['temp_view'].header.text

        # Заголовок не поменялся
        self.assertEqual(start_header, next_header)

        # Добавилась надпипь
        need_help_text = 'Имя до 10 символов'
        change_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(change_help_text, need_help_text)

        # Ванька подумал что следующий вопрос как всегла год рождения
        test_word = '1999'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Добавилась другая надпипь
        need_help_text = 'Имя только из букв'
        change_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(change_help_text, need_help_text)

        # Ванька понял свою ошибку и ввел только имя с мальнькой буквы
        test_word = 'ванька'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        need_text = 'Ванька, какого ты года рождения?'
        change_help_text = app.root.ids['temp_view'].header.text
        self.assertEqual(change_help_text, need_text)


if __name__ == '__main__':
    unittest.MyApp()
