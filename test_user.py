# coding: utf-8
import json
import os
import time
import unittest
from functools import partial
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore

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
    def test_menu_functions(self):
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
        app.root.ids['temp_view'].choose_top('Животные')

        # Приложение написало слово по-русски
        ask_word = app.root.ids['temp_view'].header.text

        # Ответа не было видно, а были две кнопки учить и ответы
        test_word = 'Ответы'
        answer = app.root.ids['temp_view'].answers.text
        self.assertEqual(answer, test_word)
        test_word = 'Учить'
        answer = app.root.ids['temp_view'].learning.text
        self.assertEqual(answer, test_word)

        # Еще были пустые кнопки
        for version in app.root.ids['temp_view'].versions.children:
            answer = version.text
            self.assertEqual(answer, '')

        # Ванька знал это слово и нажимать на кнопку учить не хотел
        animals = {'животное': 'animal', 'слон': 'elephant', 'лошадь': 'horse', 'лев': 'lion', 'мышь': 'mouse',
                   'свинья': 'pig', 'птица': 'bird', 'вид': 'kind', 'овца': 'sheep', 'рыба': 'fish', 'змея': 'snake',
                   'Кот': 'cat', 'курица': 'chicken', 'корова': 'cow', 'собака': 'dog', 'ферма': 'farm'}
        answer_word = animals[ask_word]

        # Он нажал на ответы
        app.root.ids['temp_view'].show_answers()

        # Пустые кнопки изменились на английские слова и Ванька нашел там правильный ответ
        was = False
        find_btn = None
        for version in app.root.ids['temp_view'].versions.children:
            answer = version.text
            if answer_word == answer:
                was = True
                find_btn = version
        if not was:
            self.assertEqual(answer, 'Not find!')

        # Затем он нажал на него
        app.root.ids['temp_view'].choose_version(find_btn)

        # Все кнопки опять стали пустые
        for version in app.root.ids['temp_view'].versions.children:
            answer = version.text
            self.assertEqual(answer, '')

        # Сверху слово изменилось
        ask_word2 = app.root.ids['temp_view'].header.text
        self.assertNotEquals(ask_word, ask_word2)

        # Ванька сомневался что произошло и нажал назад
        app.root.ids['temp_view'].press_on('back')

        # Заголовок изменился
        test_word = 'Темы и прогресс'
        answer = app.root.ids['temp_view'].header.text
        self.assertEqual(answer, test_word)

        # Прогресс темы увеличился
        store = JsonStore('hello.json')
        topic_know_pr = store.get('user')['user_topics']['Животные']['know_pr']
        self.assertNotEquals(0.01, topic_know_pr)

        # Он опять вернулся в туже тему
        app.root.ids['temp_view'].choose_top('Животные')

        # Приложение опять написало слово по-русски
        ask_word = app.root.ids['temp_view'].header.text

        # Ванька решительно нажал на ответы
        app.root.ids['temp_view'].show_answers()

        # Ошибся с выбором
        for version in app.root.ids['temp_view'].versions.children:
            answer = version.text
            if answer_word != answer:
                find_btn = version

        # И нажал на него
        app.root.ids['temp_view'].choose_version(find_btn)

        # Сверху появился ответ
        answer_word = app.root.ids['temp_view'].header.text
        answer = animals[ask_word]
        self.assertEqual(answer_word, answer)

        # Он нажал на первую попавшуюся кнопку
        split_btn = app.root.ids['temp_view'].btn_place.children[-1]
        app.root.ids['temp_view'].choose_split(split_btn)

        # Заголовок не изменился
        answer_word = app.root.ids['temp_view'].header.text
        answer = animals[ask_word]
        self.assertEqual(answer_word, answer)

        # текст кнопки разбился на части
        for part in app.root.ids['temp_view'].part_place.children:
            print(part.text, ':', split_btn.text)
            self.assertIn(part.text, split_btn.text)

        # Он попробовал нажать на кнопку далее
        app.root.ids['temp_view'].press_on_next(app.root.ids['temp_view'].next_btn.text)

        # Ничего не изменилось, а кнопка была фиолетовой
        test_color = 'src/btn_main_other.png'
        answer = app.root.ids['temp_view'].next_btn.background_normal
        self.assertEqual(test_color, answer)

        # Снизу появились списки и Ванька выбрал по слову
        for word_list in app.root.ids['temp_view'].word_place.children:
            print(word_list.children[0].text)
            app.root.ids['temp_view'].choose_word(word_list.children[0])

        # Части слова выделились
        for part in app.root.ids['temp_view'].part_place.children:
            answer = 'src/lighted.png'
            self.assertIn(part.background_normal, answer)

        # Кнопка далее изменила цвет
        test_color = 'src/btn_main.png'
        answer = app.root.ids['temp_view'].next_btn.background_normal
        self.assertEqual(test_color, answer)

        scroll_list = app.root.ids['temp_view'].scroll_space.children[0]
        # Он попробовал нажать на кнопку далее еще раз
        app.root.ids['temp_view'].press_on_next(app.root.ids['temp_view'].next_btn.text)

        # Список слов пропал
        self.assertNotIn(scroll_list, app.root.ids['temp_view'].scroll_space.children)

        # Появились выбранные объекты
        for word_part in app.root.ids['temp_view'].scroll_space.children[1:]:
            self.assertIn(word_part.text, app.root.ids['temp_view'].kit)

        # Ванька следовал всем указаниям по запоминанию
        app.root.ids['temp_view'].save_learn_word()
        app.root.ids['temp_view'].return_on_topic()

        # И вышел посмотреть сохранило ли прогресс
        app.root.ids['temp_view'].press_on('back')
        topic_know_pr = store.get('user')['user_topics']['Животные']['know_pr']
        store = JsonStore('hello.json')
        self.assertGreater(store.get('user')['user_topics']['Животные']['hair_pr'],
                           store.get('user')['user_topics']['Животные']['know_pr'])

        # Он опять вернулся в туже тему
        app.root.ids['temp_view'].choose_top('Животные')

        # Ванька проработал еще десяток слов
        for n in range(10):
            # Он нажал на ответы
            app.root.ids['temp_view'].show_answers()

            # И сделал выбор
            app.root.ids['temp_view'].choose_version(app.root.ids['temp_view'].versions.children[0])
            if app.root.target_view[0] != 'topic':

                # выбрал разбиение
                split_btn = app.root.ids['temp_view'].btn_place.children[-1]
                app.root.ids['temp_view'].choose_split(split_btn)

                # Ванька подобрал опять по слову
                for word_list in app.root.ids['temp_view'].word_place.children:
                    app.root.ids['temp_view'].choose_word(word_list.children[0])

                app.root.ids['temp_view'].press_on_next(app.root.ids['temp_view'].next_btn.text)

                # Ванька следовал всем указаниям по запоминанию
                app.root.ids['temp_view'].save_learn_word()
                app.root.ids['temp_view'].return_on_topic()

        # Почувствовал усталость вышел
        app.root.ids['temp_view'].press_on('back')
        app.root.ids['temp_view'].press_on('back')

        run_time(60*30)

        print(111111, app.root.target_view)
        # Выбрал тему
        app.root.ids['temp_view'].press_on('all_topics')
        print(2222222, app.root.target_view)
        app.root.ids['temp_view'].choose_top('Животные')
        print(3333333, app.root.target_view)

def run_time(seconds):
    with open('hello.json', 'r') as file:
        text = file.read()
    print()
    new_text_list = []
    for part in text.split(' '):
        try:
            if ',' in part and '}' not in part and int(part[0:-1]) > 160000000:
                part = f"{int(part[0:-1]) - seconds},"
                print(part[0:-1])
        except:
            pass
        new_text_list.append(part)
    new_text = ' '.join(new_text_list)
    with open('hello.json', 'w') as file:
        file.write(new_text)


if __name__ == '__main__':
    unittest.MyApp()
