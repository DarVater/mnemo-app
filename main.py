import random
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.core.window import Window
from datetime import datetime

from kivy.uix.gridlayout import GridLayout

from language import Language
from word_by_topics import words_by_lvl, source_by_top
from assosiator import Associator

#Window.size = 540, 960


class SelectionPart(BoxLayout):
    def write_word(self, btn):
        text = btn.parent.children[1].text
        if len(text) > 1:
            btn.parent.children[1].background_normal =  'src/lighted.png'
            root = btn.parent.parent.parent.parent.parent.parent
            index_part = btn.parent.parent.children[10].index
            root.kit[index_part] = text
            print(root.kit)
            print(index_part)
            for n in range(10):
                btn.parent.parent.children[n].background_normal = 'src/transparent.png'
                btn.parent.parent.children[n].background_down = 'src/transparent.png'
            root.check_kit()
            index_part = len(root.part_place.children) - 1 - index_part
            root.part_place.children[index_part].background_normal = 'src/lighted.png'

class WordPart(Button):
    pass


class ViewSelection(GridLayout):
    all_compares = None
    words_by_group = {}
    root = None
    kit = None
    lang = Language()
    next_allowed = False

    def press_on_next(self):
        if self.next_allowed:
            print('next')
        else:
            print('Need Choose for all')

    def press_on_back(self):
        print('back')
        self.root.target_view.pop(-1)
        self.root.target_view[0] = 'splitting'
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def choose_word(self, btn):
        print(btn.text)
        for n in range(10):
            btn.parent.children[n].background_normal = 'src/transparent.png'
            btn.parent.children[n].background_down = 'src/transparent.png'
        print(btn.parent.children[10].children[1])
        btn.parent.children[10].children[1].background_normal = 'src/input.png'
        btn.background_normal = 'src/lighted.png'
        btn.background_down = 'src/lighted.png'
        index_part = len(self.part_place.children) - 1 - self.words_by_group[btn.text]
        self.part_place.children[index_part].background_normal = 'src/lighted.png'
        self.kit[self.words_by_group[btn.text]] = btn.text
        print(self.kit)
        self.check_kit()
        a = 0
        if a:
            self.root.target_view.append(self.broken_word[btn.index])
            self.root.target_view[0] = 'selection'
            self.root.remove_w('temp_view')
            self.root.draw_view()

    def check_kit(self):
        self.next_allowed = True
        if '' in self.kit:
            self.next_allowed = False
        if self.next_allowed:
            self.next_btn.background_normal = 'src/btn_main.png'
            self.next_btn.background_down = 'src/btn_main_pressed.png'

    def selection(self):
        self.header.text = self.root.target_view[2]
        self.next_btn.text = self.lang.title('TITLE_TOPIC_BTN_NEXT')
        ass = Associator()
        self.all_compares = ass.get_words_of_broken_version(self.root.target_view[4])
        self.kit = [''] * len(self.root.target_view[4])
        self.word_place.width = f"{len(self.root.target_view[4]) * 300}sp"
        for part in self.root.target_view[4]:
            word_part = WordPart()
            word_part.text = part
            self.part_place.add_widget(word_part)
            selection_part = SelectionPart()
            word_index = self.root.target_view[4].index(part)
            for n in range(10):
                part_word = self.all_compares[word_index][n]
                self.words_by_group[part_word[2]] = word_index
                selection_part.children[n].text = part_word[2]
                selection_part.children[n].bind(on_release=self.choose_word)
            selection_part.children[10].index = word_index
            self.word_place.add_widget(selection_part)

    def give_root(self, root):
        self.root = root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VersionBtn(Button):
    pass


class SplitBtn(VersionBtn):
    pass


class ViewSplitWord(FloatLayout):
    root = []
    lang = Language()
    broken_word = {}

    def split_word(self):
        self.header.text = self.root.target_view[2]
        ass = Associator()
        self.broken_word = ass.get_broken_word(self.root.target_view[2].lower())
        for n in self.broken_word:
            btn = SplitBtn()
            btn.text = ', '.join(self.broken_word[n])
            btn.index = n
            btn.bind(on_release=self.choose_split)
            self.btn_place.add_widget(btn)

    def press_on(self, text):
        if text == 'back':
            self.root.target_view = 'home'
            self.root.remove_w('temp_view')
            self.root.draw_view()

    def choose_split(self, btn):
        print(self.broken_word[btn.index])
        self.root.target_view.append(self.broken_word[btn.index])
        self.root.target_view[0] = 'selection'
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def give_root(self, root):
        self.root = root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ViewLoadScreen(FloatLayout):
    pass


class ViewTopic(BoxLayout):
    root = []
    lang = Language()
    learning_list = []
    answer_versions = []
    right_answers = {}
    timer_start = 0
    target_word = ''
    check_answers = False

    def choose_version(self, btn):
        if self.check_answers:
            print(self.right_answers[self.target_word], self.right_answers[self.target_word] == btn.text, btn.text)
            if self.right_answers[self.target_word] == btn.text:
                self.learning_list.pop(self.learning_list.index(self.target_word))
                print('next word')
                user_store = self.root.store.get('user')
                user_store['user_topics'][self.root.target_view[1]]['etch_top_word'][
                    self.right_answers[self.target_word]]['cont_repeat'] = 5
                user_store['user_topics'][self.root.target_view[1]]['etch_top_word'][
                    self.right_answers[self.target_word]]['last_word_connect'] = round(time.time())
                user_store['user_topics'][self.root.target_view[1]]['etch_top_word'][
                    self.right_answers[self.target_word]]['ans_speed'] = round(time.time()) - self.timer_start
                user_store = self.calculate_topic_progress(user_store)
                self.root.store.put('user',
                                    name=user_store['name'],
                                    sex=user_store['sex'],
                                    age=user_store['age'],
                                    lang=user_store['lang'],
                                    user_topics=user_store['user_topics'],
                                    amail=user_store['amail']
                                    )
                print(user_store['user_topics'][self.root.target_view[1]])

                self.learning_mod()
                self.clear_answers()
            else:
                self.learn_word()

    def calculate_topic_progress(self, user_store):
        know = 0
        repeat = 0
        hair = 0
        word_count = len(user_store['user_topics'][self.root.target_view[1]]['etch_top_word'])
        for word in user_store['user_topics'][self.root.target_view[1]]['etch_top_word']:
            last_word_connect = user_store['user_topics'][self.root.target_view[1]]['etch_top_word'][word][
                'last_word_connect']
            cont_repeat = user_store['user_topics'][self.root.target_view[1]]['etch_top_word'][word]['cont_repeat']
            if last_word_connect != 0:
                hair += 1
                if cont_repeat > 0:
                    repeat += 1
                if cont_repeat == 5:
                    know += 1
        user_store['user_topics'][self.root.target_view[1]]['know_pr'] = self.calculate_bar(word_count / 2, know)
        user_store['user_topics'][self.root.target_view[1]]['repeat_pr'] = self.calculate_bar(word_count / 2, repeat)
        user_store['user_topics'][self.root.target_view[1]]['hair_pr'] = self.calculate_bar(word_count / 2, hair)
        return user_store

    def calculate_bar(self, half, f_sum):
        if f_sum <= half:
            return round(0.5 / half * f_sum, 2)
        else:
            return 1 + round(1 / half * (f_sum - half), 2)

    def learn_word(self):
        print('learn word', self.target_word)
        self.root.target_view = ['splitting', self.root.target_view[1], self.right_answers[self.target_word],
                                 self.target_word]
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def press_on(self, text):
        if text == 'back':
            self.root.target_view = 'all_topics'
            self.root.remove_w('temp_view')
            self.root.draw_view()

    def give_root(self, root):
        self.root = root

    def learning_mod(self):
        self.learning.text = self.lang.title('TITLE_TOPIC_BTN_LEARN')
        self.answers.text = self.lang.title('TITLE_TOPIC_BTN_ANSWERS')
        self.target_word = self.learning_list[random.randint(0, len(self.learning_list)) - 1]
        self.header.text = self.target_word

    def clear_answers(self):
        self.check_answers = False
        for ver in self.versions.children:
            ver.text = ''

    def show_answers(self):
        self.timer_start = round(time.time())
        self.check_answers = True
        not_ketch = True
        while not_ketch:
            for ver in self.versions.children:
                ver.bind(on_press=self.choose_version)
                ver.text = self.answer_versions[random.randint(0, len(self.answer_versions)) - 1]
                if self.right_answers[self.target_word] == ver.text:
                    not_ketch = False

    def check_top_action(self, top, top_name):
        self.learning_list = []
        self.answer_versions = []
        self.right_answers = {}
        time_repeat_by_number_repeat = {0: 3600 / 0.3,
                                        1: 3600 * 2,
                                        2: 3600 * 18,
                                        3: 3600 * 24 * 7,
                                        4: 3600 * 24 * 60,
                                        5: 3600 * 24 * 365,
                                        }
        repeat = False
        if top['hair_pr'] < 1:
            if round(time.time()) - top['last_top_connect'] > 3600 and top['last_top_connect'] != 0:
                repeat = True
            else:
                for word in top['etch_top_word']:
                    ask_word = words_by_lvl['ru'][top_name][word]
                    self.answer_versions.append(word)
                    last_word_connect = round(time.time()) - top['etch_top_word'][word]['last_word_connect']
                    time_past_from_repeat = time_repeat_by_number_repeat[top['etch_top_word'][word]['cont_repeat']]
                    if last_word_connect > time_past_from_repeat:
                        self.right_answers[ask_word] = word
                        self.learning_list.append(ask_word)
                self.learning_mod()
        else:
            repeat = True
        if repeat:
            print('need repeat')


class ViewChooseTopics(FloatLayout):
    root = []
    lang = Language()

    def press_on(self, text):
        if text == 'back':
            self.root.target_view = 'home'
            self.root.remove_w('temp_view')
            self.root.draw_view()

    def choose_top(self, top):
        self.root.target_view = ['topic', top]
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def give_root(self, root):
        self.root = root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ViewButton(Button):
    text = 'asdasd'

    def on_touch_down(self, touch):
        if 'temp_view' in App.get_running_app().root.ids:
            App.get_running_app().root.remove_w('temp_view')
        else:
            App.get_running_app().root.add_w('temp_view')


class MainBtn(Button):
    background_normal = 'src/btn_main.png'
    background_down = 'src/btn_main_pressed.png'


temp_data = ''


class TopicInfoLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global temp_data
        self.temp_image_source = temp_data


class TopicLayout(BoxLayout):

    def press_on_topic(self, topic_name):
        App.get_running_app().root.ids['temp_view'].choose_top(topic_name.text)


class ViewSingUp(FloatLayout):
    root = []
    name = ''
    amail = ''
    age = 0
    lang = Language()

    def give_root(self, root):
        self.root = root

    def next(self):
        temp_view = self.root.ids['temp_view']
        if temp_view.header.text == self.lang.title('TITLE_HI_WHAT_ARE_YOUR_NAME'):
            name = temp_view.input.text
            if len(name) > 1:
                next_allowed = True
                if len(name) > 10:
                    temp_view.help_text.text = self.lang.title('TITLE_NAME_NOT_LONGER')
                    next_allowed = False
                not_allowed_character = '\'1234567890!@#$%^&*()_+=-";:.,/\\*`~'
                for character in name:
                    if character in not_allowed_character:
                        next_allowed = False
                        temp_view.help_text.text = self.lang.title('TITLE_NAME_ONLY_CHARACTERS')
                if next_allowed:
                    temp_view.input.text = ''
                    temp_view.input.input_filter = 'int'
                    self.name = name.lower()[0].upper() + name.lower()[1::]
                    temp_view.header.text = f"{self.name}, {self.lang.title('TITLE_HOW_LOD_ARE_YOU')}"
        elif temp_view.header.text == f"{self.name}, {self.lang.title('TITLE_HOW_LOD_ARE_YOU')}":
            answer = temp_view.input.text
            year = datetime.now().year
            if int(answer) < year - 100:
                temp_view.help_text.text = self.lang.title('TITLE_YOU_ARE_FROM_THE_PAST')
            elif int(answer) > year - 6:
                temp_view.help_text.text = self.lang.title('TITLE_YOU_ARE_FROM_THE_FUTURE')
            else:
                temp_view.help_text.text = ''
                temp_view.input.text = ''
                temp_view.header.text = self.lang.title('TITLE_YOUR_MAIL')
                temp_view.input.input_filter = None
                self.age = year - int(answer)
        elif temp_view.header.text == self.lang.title('TITLE_YOUR_MAIL'):
            answer = temp_view.input.text
            next_allowed = False
            if ' ' in answer:
                temp_view.help_text.text = self.lang.title('TITLE_DONT_LOOK_LIKE_REAL_MAIL')
            elif '@' in answer:
                splited_answer = answer.split('@')
                if len(splited_answer) == 2 and '.' in splited_answer[1]:
                    next_allowed = True
                else:
                    temp_view.help_text.text = self.lang.title('TITLE_DONT_LOOK_LIKE_REAL_MAIL')
            else:
                temp_view.help_text.text = self.lang.title('TITLE_DONT_LOOK_LIKE_REAL_MAIL')
            if next_allowed:
                temp_view.header.text = self.lang.title('TITLE_WHAT_GENDER_ARE_YOU')
                temp_view.help_text.text = ''
                temp_view.input.text = ''
                self.amail = answer
                self.remove_input()
                self.add_and_change_gender_btns()

    def add_and_change_gender_btns(self):
        self.gander_male = MainBtn()
        self.gander_male.text = self.lang.title('TITLE_MALE')
        self.view_interface.ids['gander_male'] = self.gander_male
        self.view_interface.ids['gander_male'].on_press = self.choose_male
        self.view_interface.add_widget(self.gander_male)

        self.gander_female = MainBtn()
        self.gander_female.text = self.lang.title('TITLE_FEMALE')
        self.gander_female.spacing = 30
        self.view_interface.ids['gander_female'] = self.gander_female
        self.view_interface.ids['gander_female'].on_press = self.choose_female
        self.view_interface.add_widget(self.gander_female)

    def choose_male(self):
        self.user_register('M')

    def choose_female(self):
        self.user_register('F')

    def create_start_user_topics(self):
        lan = 'ru'
        topics = words_by_lvl[lan].keys()
        user_topics = {}
        for top in topics:
            etch_top_word = {}
            for top_word in words_by_lvl[lan][top]:
                etch_top_word[top_word] = {'cont_repeat': 0, 'last_word_connect': 0, 'ans_speed': 64}
            user_topics[top] = {'know_pr': 0.01,
                                'repeat_pr': 0.01,
                                'hair_pr': 0.01,
                                'last_top_connect': 0,
                                'etch_top_word': etch_top_word,
                                }
        return user_topics

    def user_register(self, gender):
        user_topics = self.create_start_user_topics()
        self.root.store.put('user',
                            name=self.name,
                            sex=gender,
                            age=self.age,
                            lang='ru',
                            user_topics=user_topics,
                            amail=self.amail)
        self.root.remove_w('temp_view')
        self.root.chose_main_view()
        self.root.draw_view()

    def remove_input(self):
        textinput = self.ids.input
        textinput.parent.remove_widget(textinput)
        self.ids.pop('input')
        btn = self.ids.btn
        btn.parent.remove_widget(btn)
        self.ids.pop('btn')


class ViewHowItWorks(FloatLayout):
    root = []
    lang = Language()

    def press_on(self, text):
        if text == 'back':
            self.root.target_view = 'home'
            self.root.remove_w('temp_view')
            self.root.draw_view()

    def give_root(self, root):
        self.root = root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ViewLanguage(FloatLayout):
    root = []
    lang = Language()

    def press_on(self, text):
        if text == 'back':
            self.root.target_view = 'home'
            self.root.remove_w('temp_view')
            self.root.draw_view()
        elif text == 'ru':
            self.root.ids['temp_view'].ua.background_normal = 'src/btn_main_other.png'
            self.root.ids['temp_view'].ru.background_normal = 'src/btn_main.png'
            user_store = self.root.store.get('user')
            user_store['lang'] = 'ru'
            self.root.store.store_put('user', user_store)

        elif text == 'ua':
            self.root.ids['temp_view'].ru.background_normal = 'src/btn_main_other.png'
            self.root.ids['temp_view'].ua.background_normal = 'src/btn_main.png'
            user_store = self.root.store.get('user')
            user_store['lang'] = 'ua'
            self.root.store.store_put('user', user_store)

    def give_root(self, root):
        self.root = root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ViewHome(FloatLayout):
    root = []
    lang = Language()

    def press_on(self, text):
        if text == 'Exit':
            App.get_running_app().stop()
        elif text == 'how_it_works':
            self.root.target_view = 'how_it_works'
            self.root.remove_w('temp_view')
            self.root.draw_view()
        elif text == 'choose_language':
            self.root.target_view = 'languages'
            self.root.remove_w('temp_view')
            self.root.draw_view()
        elif text == 'all_topics':
            self.root.target_view = 'all_topics'
            self.root.remove_w('temp_view')
            self.root.draw_view()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def give_root(self, root):
        self.root = root

    def topics(self):
        pass

    def how_it_works(self):
        pass

    def choose_language(self):
        pass

    def exit(self):
        App.get_running_app().stop()


class ViewManager(FloatLayout):
    target_view = ''
    root = []
    started = 0
    topic_keys = []
    lang = Language()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pb = None
        self.store = JsonStore('hello.json')
        self.chose_main_view()
        self.draw_view()

    def remove_w(self, w_name='temp_view'):
        self.remove_widget(self.ids[w_name])
        self.ids.pop(w_name)

    def draw_view(self):
        if self.target_view == 'sing_up':
            temp_view = ViewSingUp()
            temp_view.give_root(self)
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].btn.text = self.lang.title('TITLE_BTN_NEXT')
            self.ids['temp_view'].header.text = self.lang.title('TITLE_HI_WHAT_ARE_YOUR_NAME')
        elif self.target_view == 'home':
            temp_view = ViewHome()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.lang.set_lang(self.store.get('user')['lang'])
            self.ids['temp_view'].header.text = self.lang.title('TITLE_HOME_HEADER')
            self.ids['temp_view'].exit.text = self.lang.title('TITLE_BTN_EXIT')
            self.ids['temp_view'].choose_language.text = self.lang.title('TITLE_BTN_CHOOSE_LANGUAGE')
            self.ids['temp_view'].how_it_works.text = self.lang.title('TITLE_BTN_HOW_IT_WORKS')
            self.ids['temp_view'].topics.text = self.lang.title('TITLE_BTN_TOPICS')
            self.ids['temp_view'].know.text = self.lang.title('TITLE_KNOW')
            self.ids['temp_view'].repeat.text = self.lang.title('TITLE_REPEAT')
            self.ids['temp_view'].hair.text = self.lang.title('TITLE_HAIR')

        elif self.target_view == 'how_it_works':
            temp_view = ViewHowItWorks()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].header.text = self.lang.title('TITLE_APP_NEED_FOR_HEADER')
            self.ids['temp_view'].bloc1.text = self.lang.title('TITLE_APP_NEED_FOR_BLOC1')
            self.ids['temp_view'].bloc2.text = self.lang.title('TITLE_APP_NEED_FOR_BLOC2')
            self.ids['temp_view'].bloc3.text = self.lang.title('TITLE_APP_NEED_FOR_BLOC3')
            self.ids['temp_view'].bloc4.text = self.lang.title('TITLE_APP_NEED_FOR_BLOC4')
            self.ids['temp_view'].bloc5.text = self.lang.title('TITLE_APP_NEED_FOR_BLOC5')
            self.change_scroll_height()

        elif self.target_view == 'languages':
            temp_view = ViewLanguage()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].header.text = self.lang.title('TITLE_LANGUAGE_ASSOCIATION')
            self.ids['temp_view'].ua.text = self.lang.title('TITLE_LANGUAGE_UKRAINIAN')
            self.ids['temp_view'].ru.text = self.lang.title('TITLE_LANGUAGE_RUSSIAN')
            if self.store.get('user')['lang'] == 'ru':
                self.ids['temp_view'].ru.background_normal = 'src/btn_main.png'
            elif self.store.get('user')['lang'] == 'ua':
                self.ids['temp_view'].ua.background_normal = 'src/btn_main.png'

        elif self.target_view == 'all_topics':
            load_view = ViewLoadScreen()
            self.add_widget(load_view)
            self.ids['load_view'] = load_view
            temp_view = ViewChooseTopics()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.ids['temp_view'].opacity = 0
            self.ids['temp_view'].header.text = self.lang.title('TITLE_TOPIC_HEADER')
            self.ids['temp_view'].alert_text.text = self.lang.title('TITLE_TOPIC_UNBLOCK_CHOOSE_TOPIC')
            self.add_etch_top()
            self.ids['temp_view'].opacity = 1

        elif self.target_view[0] == 'topic':
            temp_view = ViewTopic()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].header.text = self.lang.title('TITLE_TOPIC_HEADER')
            self.ids['temp_view'].check_top_action(self.user_topics[self.target_view[1]], self.target_view[1])

        elif self.target_view[0] == 'splitting':
            temp_view = ViewSplitWord()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].split_word()

        elif self.target_view[0] == 'selection':
            temp_view = ViewSelection()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].selection()

    def add_etch_top(self, time_pass=1):
        if self.started == 0:
            self.user_topics = self.store.get('user')['user_topics']
            self.can_choose_topic = True
            for top_name in self.user_topics.keys():
                self.topic_keys.append(top_name)
                if 0.01 < self.user_topics[top_name]['hair_pr'] < 0.9:
                    self.can_choose_topic = False
            if self.can_choose_topic:
                self.ids['temp_view'].alert.opacity = 1

        top_name = self.topic_keys[self.started]
        global temp_data
        self.started += 1
        self.ids['load_view'].my_pb.height = self.ids['load_view'].height / 38 * self.started
        temp_data = f"src/{source_by_top[top_name]}.png"
        layout = TopicLayout()
        layout.top_info_layout.progress_know.size_hint_y = self.user_topics[top_name]['know_pr']
        layout.top_info_layout.progress_repeat.size_hint_y = self.user_topics[top_name]['repeat_pr']
        layout.top_info_layout.progress_hair.size_hint_y = self.user_topics[top_name]['hair_pr']
        layout.btn.text = top_name
        if not self.can_choose_topic and 0.01 == self.user_topics[top_name]['hair_pr']:
            layout.opacity = 0.5
            layout.btn.background_down = 'src/topic.png'
        else:
            layout.btn.bind(on_press=layout.press_on_topic)
        self.ids['temp_view'].topics_grid.add_widget(layout)
        if self.started < 38:
            Clock.schedule_once(self.add_etch_top, 0.001)
        else:
            self.started = 0
            self.topic_keys = []
            self.remove_widget(self.ids['load_view'])
            self.ids.pop('load_view')
            self.add_widget(self.ids['temp_view'])

    def change_scroll_height(self):
        skaler = (((int(self.ids['temp_view'].bloc1.font_size) / 24) - 1) / 10) + 1
        self.ids['temp_view'].header.height = self.ids['temp_view'].header.height * skaler
        self.ids['temp_view'].bloc1.height = self.ids['temp_view'].bloc1.height * skaler
        self.ids['temp_view'].bloc2.height = self.ids['temp_view'].bloc2.height * skaler
        self.ids['temp_view'].bloc3.height = self.ids['temp_view'].bloc3.height * skaler
        self.ids['temp_view'].bloc4.height = self.ids['temp_view'].bloc4.height * skaler
        self.ids['temp_view'].bloc5.height = self.ids['temp_view'].bloc5.height * skaler

        scroll_h = self.ids['temp_view'].header.height
        scroll_h += self.ids['temp_view'].bloc1.height
        scroll_h += self.ids['temp_view'].bloc2.height
        scroll_h += self.ids['temp_view'].bloc3.height
        scroll_h += self.ids['temp_view'].bloc4.height
        scroll_h += self.ids['temp_view'].bloc5.height
        scroll_h += 1000

        self.ids['temp_view'].view_interface.height = scroll_h * ((skaler - 1) * 1.5 + 1)

    def chose_main_view(self):
        if 'user' in self.store:
            self.target_view = ['selection', 'Дом', 'computer', 'компьютер', ['кэм', 'пйу', 'утэ']]  # home
        else:
            self.target_view = 'sing_up'

    def give_root(self, root):
        self.root.append(root)


class MyApp(App):
    def build(self):
        view_manager = ViewManager()
        return view_manager


if __name__ == '__main__':
    MyApp().run()
