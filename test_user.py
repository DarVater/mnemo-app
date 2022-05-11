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
        app.root.ids['temp_view'].exit.on_press()


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

    def setUp(self):
        pass

    # Ванька включил приложение как только появилось свободное время
    def test_menu_language(self):
        app = MyApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()

        # в главном меню его заинтересовал пункт как это работает и он нажал а него
        app.root.ids['temp_view'].press_on('how_it_works')

        # На этой странице Ванька увидел заголовок
        test_word = 'Это программа для подбора образов кодирующих иностранное слово'
        answer = app.root.ids['temp_view'].header.text
        self.assertEqual(answer, test_word)

        # Он прочитал и захотел пройти все как следует. И проверить работает ли система. Нажал кнопку назад
        app.root.ids['temp_view'].press_on('back')

        # Оказался в главном меню
        answer_no_user = 'home'
        test_view = app.root.target_view
        self.assertEqual(test_view, answer_no_user)

        # Поинтересовался Ванька какие языки еще есть
        app.root.ids['temp_view'].press_on('choose_language')

        # Там Ванька увидел заголовок
        test_word = 'С каким языком ассоциировать?'
        answer = app.root.ids['temp_view'].header.text
        self.assertEqual(answer, test_word)

        # Случайно нажал на Украинский
        app.root.ids['temp_view'].press_on('ua')

        # И вышел
        app.root.ids['temp_view'].press_on('back')

        # Он заметил, что в главном окне изменилась надпись на Украинский язык
        test_word = 'Слова рівня А1'
        answer = app.root.ids['temp_view'].header.text
        self.assertEqual(answer, test_word)

        # Ваника поменял обратно
        app.root.ids['temp_view'].press_on('choose_language')
        app.root.ids['temp_view'].press_on('ru')
        app.root.ids['temp_view'].press_on('back')
        test_word = 'Слова уровня А1'
        answer = app.root.ids['temp_view'].header.text
        self.assertEqual(answer, test_word)

        # Потом он нажал на темы
        app.root.ids['temp_view'].press_on('all_topics')

        # Заголовок изменился
        test_word = 'Темы и прогресс'
        answer = app.root.ids['temp_view'].header.text
        self.assertEqual(answer, test_word)

        # За ней следовала надпись "Доступная новая тема!"
        test_word = 'Доступная новая тема!'
        answer = app.root.ids['temp_view'].alert_text.text
        self.assertEqual(answer, test_word)

        # Ему понравилась тема животные
        print(app.root.ids['temp_view'])
        app.root.ids['temp_view'].choose_top('Животные')


if __name__ == '__main__':
    unittest.MyApp()
