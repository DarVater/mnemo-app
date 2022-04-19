# coding: utf-8
import os
import time
import unittest
from functools import partial
from kivy.clock import Clock

from main import MyApp


class TestSingUpView(unittest.TestCase):
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

    def test_sing_up(self):
        try:
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hello.json')
            os.remove(path)
        except:
            print("Don`t have 'hello.json' file to delete")
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

        # Программа предложила ввести свой год рождения
        need_text = 'Ванька, какого \nты года рождения?'
        change_help_text = app.root.ids['temp_view'].header.text
        self.assertEqual(change_help_text, need_text)

        # Ванька ввел день рождения и месяц
        test_word = '1307'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Программа предположила что он  из прошлого
        need_text = 'Ты из прошлого?'
        change_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(change_help_text, need_text)

        # Ванька ввел полную дату рождения
        test_word = '13071999'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Программа предположила что он  из прошлого
        need_text = 'Ты из будущего?'
        change_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(change_help_text, need_text)

        # Ванька ввел только год рождения
        test_word = '1999'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Программа спросила эмейл
        need_text = 'Твоя электронная почта?'
        change_help_text = app.root.ids['temp_view'].header.text
        self.assertEqual(change_help_text, need_text)

        # Ванька ввел случайный текст
        test_word = 'фыва фывав'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Программа написала что на электронный адрес не похоже
        need_text = 'На настоящую почту не похоже!'
        change_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(change_help_text, need_text)

        # Он попрообовол симулировать почту
        test_word = 'фыва@фывав'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Программа опять написала что на электронный адрес не похоже
        need_text = 'На настоящую почту не похоже!'
        change_help_text = app.root.ids['temp_view'].help_text.text
        self.assertEqual(change_help_text, need_text)

        # На этот раз ввел реалистичную почту
        test_word = 'фыва@фывав.авы'
        app.root.ids['temp_view'].input.text = test_word
        app.root.ids['temp_view'].next()

        # Ванька наконецто увидел надпись выбора пола
        need_text = 'Последний вопрос. \nКакого ты пола?'
        change_help_text = app.root.ids['temp_view'].header.text
        self.assertEqual(change_help_text, need_text)

        # Он назал на кнопку 'Мужской'
        app.root.ids['temp_view'].view_interface.ids['gander_male'].on_press()

        # Ванька увидел экран домашней страницы
        answer_no_user = 'home'
        test_view = app.root.target_view
        self.assertEqual(test_view, answer_no_user)

        # Его отвлекли и он выключил приложение



class TestHomeView(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.MyApp()
