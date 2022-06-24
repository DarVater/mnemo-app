# coding: utf-8
import json
import os
import time
import unittest
from functools import partial
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button

from main import MyApp, words_by_lvl
from word_by_topics import words_by_lvl_A2, words_by_lvl_A1


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
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'hello_{words_by_lvl["en_lvl"]}.json')
            os.remove(path)
        except:
            print(f"Don`t have hello_{words_by_lvl['en_lvl']}.json file to delete")
        app = MyApp()
        p = partial(self.run_test, app)
        Clock.schedule_once(p, 0.000001)
        app.run()

        # дополнительных надписей не было
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

        # И прошёл обучение
        btn = Button()
        btn.nuances = 4
        app.root.ids['temp_view'].press_on_got_it(btn)

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
        test_word = 'Слова рівня'
        answer = app.root.ids['temp_view'].header.text
        self.assertIn(test_word, answer)

        # Ваника поменял обратно
        app.root.ids['temp_view'].press_on('choose_language')
        app.root.ids['temp_view'].press_on('ru')
        app.root.ids['temp_view'].press_on('back')
        test_word = 'Слова уровня'
        answer = app.root.ids['temp_view'].header.text
        self.assertIn(test_word, answer)

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
        app.root.ids['temp_view'].choose_top('Animals')

        # Приложение написало слово по-русски
        ask_word = app.root.ids['temp_view'].header.text

        # Ответа не было видно, а были две кнопки учить и ответы
        test_word = 'Знаю'
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
                   'Кот': 'cat', 'курица': 'chicken', 'корова': 'cow', 'собака': 'dog', 'ферма': 'farm',
                   'медведь': 'bear', 'домашнее животное': 'pet',
                   'население': 'population', 'муха': 'fly', 'индивидуум': 'individual',
                   'обезьяна': 'monkey', 'насекомое': 'insect',
                   'паук': 'spider', 'лягушка': 'frog', 'ребенок (разговорный)': 'kid',
                   }

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
        store = JsonStore(f'hello_{words_by_lvl["en_lvl"]}.json')
        topic_know_pr = store.get('user')['user_topics']['Animals']['know_pr']
        self.assertNotEquals(0.01, topic_know_pr)

        # Он опять вернулся в туже тему
        app.root.ids['temp_view'].choose_top('Animals')

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
        self.assertIn(answer, answer_word)

        # Он нажал на первую попавшуюся кнопку
        split_btn = app.root.ids['temp_view'].btn_place.children[-1]
        app.root.ids['temp_view'].choose_split(split_btn)

        # Заголовок не изменился
        answer_word = app.root.ids['temp_view'].header.text
        answer = animals[ask_word]
        self.assertIn(answer, answer_word)

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
        topic_know_pr = store.get('user')['user_topics']['Animals']['know_pr']
        store = JsonStore(f'hello_{words_by_lvl["en_lvl"]}.json')
        self.assertGreater(store.get('user')['user_topics']['Animals']['hair_pr'],
                           store.get('user')['user_topics']['Animals']['know_pr'])

        #################################################################
        try_catch_float_bug = 1
        if try_catch_float_bug:
            time.sleep(5)
            need_topics = ['topic_town', 'home', 'food', 'nature', 'human', 'relations', 'vehicle', 'Animals', 'Sport',
                           'Colors', 'Work', 'Professions', 'learning', 'Entertainment', 'clock', 'Calendar',
                           'Clothing', 'Hobby', 'Other', 'Pointers', 'Exclamation', 'unions', 'numbers', 'preposition',
                           'Adverb', 'Availability', 'Operations', 'Communication', 'Stages', 'Movements', 'Thinking',
                           'Other_verbs', 'Emotions', 'Abstract', 'Approximately', 'Condition', 'Qualities', 'Pronouns']

            for top in need_topics:
                app.root.ids['temp_view'].choose_top(top)
                # Ванька проработал все слова
                for n in range(70):
                    print('range(', n, ')')
                    # Он нажал на ответы
                    app.root.ids['temp_view'].show_answers()

                    # И сделал выбор
                    app.root.ids['temp_view'].choose_version(app.root.ids['temp_view'].versions.children[0])
                    if app.root.target_view[0] != 'topic':

                        # выбрал разбиение
                        try:
                            split_btn = app.root.ids['temp_view'].btn_place.children[-1]
                            app.root.ids['temp_view'].choose_split(split_btn)
                        except:
                            if n < 8:
                                split_btn = app.root.ids['temp_view'].btn_place.children[0]
                                app.root.ids['temp_view'].choose_split(split_btn)

                        # Ванька подобрал опять по слову
                        for word_list in app.root.ids['temp_view'].word_place.children:
                            app.root.ids['temp_view'].choose_word(word_list.children[0])

                        app.root.ids['temp_view'].press_on_next(app.root.ids['temp_view'].next_btn.text)

                        # Ванька следовал всем указаниям по запоминанию
                        app.root.ids['temp_view'].save_learn_word()
                        app.root.ids['temp_view'].return_on_topic()
                        if app.root.target_view == 'all_topics':
                            break


        ###################################################################
        else:
            # Он опять вернулся в туже тему
            app.root.ids['temp_view'].choose_top('Animals')

            # Ванька проработал еще десяток слов
            for n in range(6):
                print('range(', n, ')')
                # Он нажал на ответы
                app.root.ids['temp_view'].show_answers()

                # И сделал выбор
                app.root.ids['temp_view'].choose_version(app.root.ids['temp_view'].versions.children[0])
                if app.root.target_view[0] != 'topic':

                    # выбрал разбиение
                    try:
                        split_btn = app.root.ids['temp_view'].btn_place.children[-1]
                        app.root.ids['temp_view'].choose_split(split_btn)
                    except:
                        if n < 8:
                            split_btn = app.root.ids['temp_view'].btn_place.children[0]
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
            run_time(60 * 30)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопки учить уже не было
            must_be = 'Объекты'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Ответ с одной подсказкой
            if 1:
                # Программа спрашивала слово
                ask_word = app.root.ids['temp_view'].header.text

                # Он нажал на ответы
                app.root.ids['temp_view'].show_answers()

                # Этого слова он не помнил и нажал на кнопку помощи
                app.root.ids['temp_view'].show_helper(app.root.ids['temp_view'].learning)

                # Она поменялась на
                must_be = 'Забыл'
                answer_word = app.root.ids['temp_view'].learning.text
                self.assertEqual(answer_word, must_be)

                # Ванька вспомнил слово
                answer_word = animals[ask_word]
                for version in app.root.ids['temp_view'].versions.children:
                    answer = version.text
                    if answer_word == answer:
                        find_btn = version
                help1 = find_btn.text
                print('help1: ', help1)
                app.root.ids['temp_view'].choose_version(find_btn)

            # Ответ с двумя подсказками
            if 2:
                # Программа спрашивала слово
                ask_word = app.root.ids['temp_view'].header.text

                # Он нажал на ответы
                app.root.ids['temp_view'].show_answers()

                # Этого слова он не помнил и нажал на кнопку помощи
                app.root.ids['temp_view'].show_helper(app.root.ids['temp_view'].learning)

                # Объекты не помогли он нажал на не помню
                app.root.ids['temp_view'].show_helper(app.root.ids['temp_view'].learning)

                # Она поменялась на
                must_be = 'Плохо'
                answer_word = app.root.ids['temp_view'].learning.text
                self.assertEqual(answer_word, must_be)

                # Ванька вспомнил слово
                answer_word = animals[ask_word]
                for version in app.root.ids['temp_view'].versions.children:
                    answer = version.text
                    if answer_word == answer:
                        find_btn = version
                help2 = find_btn.text
                print('help2: ', help2)
                app.root.ids['temp_view'].choose_version(find_btn)

            # Ванька ответил на остальные вопросы повторения
            for n in range(len(app.root.ids['temp_view'].repeating_list)):
                # Программа спрашивала слово
                ask_word = app.root.ids['temp_view'].header.text

                # Он нажал на ответы
                app.root.ids['temp_view'].show_answers()

                # Ванька знал слово
                answer_word = animals[ask_word]
                for version in app.root.ids['temp_view'].versions.children:
                    answer = version.text
                    if answer_word == answer:
                        find_btn = version
                app.root.ids['temp_view'].choose_version(find_btn)

            # Выкинуло в выбор темы
            must_be = 'Темы и прогресс'
            answer_word = app.root.ids['temp_view'].header.text
            self.assertEqual(answer_word, must_be)

            # Его позвали и он вышел
            app.root.ids['temp_view'].press_on('back')
            app.root.ids['temp_view'].press_on('back')

            # Прошло еще 5 минут
            run_time(60 * 5)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопка учить еще была
            must_be = 'Учить'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Его позвали и он вышел
            app.root.ids['temp_view'].press_on('back')
            app.root.ids['temp_view'].press_on('back')

            # Прошло еще 25 минут
            run_time(60 * 25)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопки учить уже не было
            must_be = 'Объекты'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Его позвали и он вышел
            app.root.ids['temp_view'].press_on('back')
            app.root.ids['temp_view'].press_on('back')

            # Прошло еще 31 минут
            run_time(60 * 60 * 2)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопки учить уже не было
            must_be = 'Объекты'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Ситуация повторилась
            if 1:
                # Ответ с одной подсказкой
                if 1:
                    # Программа спрашивала слово
                    ask_word = app.root.ids['temp_view'].header.text

                    # Он нажал на ответы
                    app.root.ids['temp_view'].show_answers()

                    # Этого слова он не помнил и нажал на кнопку помощи
                    app.root.ids['temp_view'].show_helper(app.root.ids['temp_view'].learning)

                    # Она поменялась на
                    must_be = 'Забыл'
                    answer_word = app.root.ids['temp_view'].learning.text
                    self.assertEqual(answer_word, must_be)

                    # Ванька вспомнил слово
                    answer_word = animals[ask_word]
                    for version in app.root.ids['temp_view'].versions.children:
                        answer = version.text
                        if answer_word == answer:
                            find_btn = version
                    help1 = find_btn.text
                    print('help1: ', help1)
                    app.root.ids['temp_view'].choose_version(find_btn)

                # Ответ с двумя подсказками
                if 2:
                    # Программа спрашивала слово
                    ask_word = app.root.ids['temp_view'].header.text

                    # Он нажал на ответы
                    app.root.ids['temp_view'].show_answers()

                    # Этого слова он не помнил и нажал на кнопку помощи
                    app.root.ids['temp_view'].show_helper(app.root.ids['temp_view'].learning)

                    # Объекты не помогли он нажал на не помню
                    app.root.ids['temp_view'].show_helper(app.root.ids['temp_view'].learning)

                    # Она поменялась на
                    must_be = 'Плохо'
                    answer_word = app.root.ids['temp_view'].learning.text
                    self.assertEqual(answer_word, must_be)

                    # Ванька вспомнил слово
                    answer_word = animals[ask_word]
                    for version in app.root.ids['temp_view'].versions.children:
                        answer = version.text
                        if answer_word == answer:
                            find_btn = version
                    help2 = find_btn.text
                    print('help2: ', help2)
                    app.root.ids['temp_view'].choose_version(find_btn)

                # Ванька ответил на остальные вопросы повторения
                for n in range(len(app.root.ids['temp_view'].repeating_list)):
                    # Программа спрашивала слово
                    ask_word = app.root.ids['temp_view'].header.text

                    # Он нажал на ответы
                    app.root.ids['temp_view'].show_answers()

                    # Ванька знал слово
                    answer_word = animals[ask_word]
                    for version in app.root.ids['temp_view'].versions.children:
                        answer = version.text
                        if answer_word == answer:
                            find_btn = version
                    app.root.ids['temp_view'].choose_version(find_btn)

                # Выкинуло в выбор темы
                must_be = 'Темы и прогресс'
                answer_word = app.root.ids['temp_view'].header.text
                self.assertEqual(answer_word, must_be)

            # Его позвали и он вышел
            app.root.ids['temp_view'].press_on('back')
            app.root.ids['temp_view'].press_on('back')

            # Прошло еще 5 минут
            run_time(60 * 5)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопка учить еще была
            must_be = 'Учить'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Слов для повторения не было
            self.assertEqual(0, len(app.root.ids['temp_view'].repeating_list))

            # Его позвали и он вышел
            app.root.ids['temp_view'].press_on('back')
            app.root.ids['temp_view'].press_on('back')

            # Прошло еще 25 минут
            run_time(60 * 25)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопки учить уже не было
            must_be = 'Объекты'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Добавилось слово для повторения
            self.assertEqual(1, len(app.root.ids['temp_view'].repeating_list))

            # Его позвали и он вышел
            app.root.ids['temp_view'].press_on('back')
            app.root.ids['temp_view'].press_on('back')

            # Прошло еще 91 минут
            run_time(60 * 92)

            # Выбрал тему
            app.root.ids['temp_view'].press_on('all_topics')
            app.root.ids['temp_view'].choose_top('Animals')

            # Кнопки учить уже не было
            must_be = 'Объекты'
            answer_word = app.root.ids['temp_view'].learning.text
            self.assertEqual(answer_word, must_be)

            # Добавилось слово для повторения
            self.assertEqual(3, len(app.root.ids['temp_view'].repeating_list))

            # Ванька ответил на эти вопросы
            for n in range(len(app.root.ids['temp_view'].repeating_list)):
                # Программа спрашивала слово
                ask_word = app.root.ids['temp_view'].header.text

                # Он нажал на ответы
                app.root.ids['temp_view'].show_answers()

                # Ванька знал слово
                answer_word = animals[ask_word]
                for version in app.root.ids['temp_view'].versions.children:
                    answer = version.text
                    if answer_word == answer:
                        find_btn = version
                app.root.ids['temp_view'].choose_version(find_btn)

            # Выкинуло в выбор темы
            must_be = 'Темы и прогресс'
            answer_word = app.root.ids['temp_view'].header.text
            self.assertEqual(answer_word, must_be)

            print(app.root.target_view)


class TestDictionary(unittest.TestCase):
    lvl_words = {}

    def test_avery_word_hes_transcription(self):
        word_trans_dict = load_dict('word_trans_dict')
        from word_by_topics import words_by_lvl_A1
        for top_name in words_by_lvl_A1['ru']:
            for word in words_by_lvl_A1['ru'][top_name]:
                self.assertIn(word, word_trans_dict)

    def test_ru_china_transcription(self):
        ru_china_trans = load_dict('ru_china_trans')
        word_trans_dict = load_dict('word_trans_dict')
        from word_by_topics import words_by_lvl_A1
        for top_name in words_by_lvl_A1['ru']:
            for word in words_by_lvl_A1['ru'][top_name]:
                trans = word_trans_dict[word]
                now = ''
                for t in trans:
                    if t not in ru_china_trans['complex'] and t.lower() not in ru_china_trans['simple'] and t not in \
                            ru_china_trans['simple']:
                        print(t not in ru_china_trans['complex'], t.lower() not in ru_china_trans['simple'],
                              t not in ru_china_trans['simple'])
                        print(trans)
                        print(now, f"'{t}'")
                        self.assertIn(t, ru_china_trans['simple'])
                    else:
                        now += t

    def test_ua_china_transcription(self):
        ua_china_trans = load_dict('ua_china_trans')
        word_trans_dict = load_dict('word_trans_dict')
        from word_by_topics import words_by_lvl_A1
        for top_name in words_by_lvl_A1['ru']:
            for word in words_by_lvl_A1['ru'][top_name]:
                trans = word_trans_dict[word]
                now = ''
                for t in trans:
                    if t not in ua_china_trans['complex'] and t.lower() not in ua_china_trans['simple'] and t not in \
                            ua_china_trans['simple']:
                        print(t not in ua_china_trans['complex'], t.lower() not in ua_china_trans['simple'],
                              t not in ua_china_trans['simple'])
                        print(trans)
                        print(now, f"'{t}'")
                        self.assertIn(t, ua_china_trans['simple'])
                    else:
                        now += t

    def test_vowels_n_consonant(self):
        ua_china_trans = load_dict('ua_china_trans')
        ru_china_trans = load_dict('ru_china_trans')
        all_letters = ''
        for china in ua_china_trans['complex']: all_letters += ua_china_trans['complex'][china]
        for china in ua_china_trans['simple']: all_letters += ua_china_trans['simple'][china]
        for china in ru_china_trans['complex']: all_letters += ru_china_trans['complex'][china]
        for china in ru_china_trans['simple']: all_letters += ru_china_trans['simple'][china]
        vowels_consonant = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'і', 'е', 'б', 'в', 'г', 'д', 'ж', 'з',
                            'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч',
                            'ш', 'щ', 'ъ', 'ь', ' ']
        for one_letter in all_letters:
            self.assertIn(one_letter, vowels_consonant)

    def get_all_lwl_words(self):
        lvl_dir = '/home/bilcko/AndroidProgects/EnglishTeacher/research/words_by_level/All words by lvl and types/'
        lvl_files = ['A1', 'A2']  #
        for file_name in lvl_files:
            with open(f'{lvl_dir}{file_name}.txt') as file:
                all_rows = file.read().split('\n')
            self.lvl_words[file_name] = {}
            for row in all_rows:
                if ' ' in row:
                    self.lvl_words[file_name][row.partition(' ')[0]] = ''

    def test_all_need_word_exist(self):
        if self.lvl_words == {}:
            self.get_all_lwl_words()
        not_fined_words = []
        black_list = ['ice cream', 'CD', 'bar', 'DVD', 'yourself', 'next to', 'no one', 'TV', 'cannot', 'online',
                      'internet', 'photo', 'laughter', 'according', 'ah', 'electrical', 'happily', 'loudly', 'math',
                      'may', 'normally', 'wooden', 'wow', 'worse', 'advertising']
        for lvl in self.lvl_words:
            for word in self.lvl_words[lvl]:
                self.lvl_words[lvl][word] = False
        dont_need_words = {}
        for lang in ['ru', 'ua']:
            for words_by_lvl in [words_by_lvl_A1, words_by_lvl_A2]:  #
                for top_name in words_by_lvl[lang]:
                    for top_word in words_by_lvl[lang][top_name]:
                        # list of avery word in avery top in avery lvl
                        was = False
                        for lvl in self.lvl_words:
                            if top_word in self.lvl_words[lvl]:
                                self.lvl_words[lvl][top_word] = True
                                was = True
                        if not was and top_word not in black_list:
                            dont_need_words[top_word] = ''
        for lvl in self.lvl_words:
            for word in self.lvl_words[lvl]:
                if self.lvl_words[lvl][word] == False:
                    if word not in black_list:
                        not_fined_words.append(word)
        if 0 != len(dont_need_words):
            print('\n', len(dont_need_words), 'dont_need_words', dont_need_words)
        self.assertEqual(len(dont_need_words), 0)
        if 0 != len(not_fined_words):
            print('\n', len(not_fined_words), 'not_fined_words', not_fined_words)
        self.assertEqual(len(not_fined_words), 0)

    def test_equivalents_topics_in_languages(self):
        for top_name in words_by_lvl['ru']:
            count_words_in_topic = {}
            for lang in words_by_lvl:
                if lang != 'en_lvl':
                    count_words_in_topic[len(words_by_lvl[lang][top_name])] = ''
            if len(count_words_in_topic) != 1:
                # Look avery top word
                for lang2 in words_by_lvl:
                    if lang2 != 'en_lvl':
                        for word2 in words_by_lvl[lang2][top_name]:
                            # In avery equivalent languages
                            fined = False

                            for lang3 in words_by_lvl:
                                if lang3 != 'en_lvl':
                                    if word2 not in words_by_lvl[lang3][top_name]:
                                        fined = lang3
                            if fined:
                                print()
                                print('++++++++++++++++++++++++++++++++++')
                                print('+ Not fined !')
                                print('+ Word: ', word2)
                                print('+ Lang: ', fined)
                                print('+ Top name: ', top_name)
                                print('++++++++++++++++++++++++++++++++++')
            self.assertEqual(len(count_words_in_topic), 1)

    def test_translate_not_repeat(self):
        translated_and_words = {}
        translated = {}
        was_repeat = []
        translate_was_repeat = []
        all_words_by_lvl = {'A1': words_by_lvl_A1, 'A2': words_by_lvl_A2}
        for lvl in all_words_by_lvl:
            each_words_by_lvl = all_words_by_lvl[lvl]
            for lang in each_words_by_lvl:
                if lang != 'en_lvl':
                    for top_name in each_words_by_lvl[lang]:
                        for word in each_words_by_lvl[lang][top_name]:
                            word_nad_translate = f'{lang}, {word} = {each_words_by_lvl[lang][top_name][word]}'
                            if word_nad_translate not in translated_and_words:
                                translated_and_words[word_nad_translate] = ''
                            else:
                                was_repeat.append(word_nad_translate)
                                print()
                                print(f'{lvl}-{lang} "{word_nad_translate}" was repeat!')
                            trans = f'{lang} {each_words_by_lvl[lang][top_name][word]}'
                            if trans not in translated:
                                translated[trans] = f'{lang} {word}'
                            else:
                                translate_was_repeat.append(trans)
                                print()
                                print(f'{lvl}-{lang} "{translated[trans]}" и "{lang} {word}" = "{trans}" was repeat!')
        self.assertEqual(len(was_repeat), 0)
        print(len(translate_was_repeat))
        self.assertEqual(len(translate_was_repeat), 0)


def run_time(seconds):
    with open(f'hello_{words_by_lvl["en_lvl"]}.json', 'r') as file:
        text = file.read()
    new_text_list = []
    for part in text.split(' '):
        try:
            if ',' in part and '}' not in part and int(part[0:-1]) > 160000000:
                part = f"{int(part[0:-1]) - seconds},"
        except:
            pass
        new_text_list.append(part)
    new_text = ' '.join(new_text_list)
    with open(f'hello_{words_by_lvl["en_lvl"]}.json', 'w') as file:
        file.write(new_text)


def load_dict(name: str):
    '''
    load dict from data file
    :param name:
    :return:
    '''
    with open(f'{name}.data', 'r') as file:
        ret = json.loads(file.read())
        return ret


if __name__ == '__main__':
    unittest.MyApp()
