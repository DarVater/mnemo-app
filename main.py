import random
import time
from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from language import Language
from word_by_topics import words_by_lvl_A1 as words_by_lvl
from assosiator import Associator

error_catch = False  # False True
if not error_catch:
    Window.size = 540, 960


class SelectionPart(BoxLayout):
    def write_word(self, btn):
        text = btn.parent.children[1].text
        if len(text) > 1:
            btn.parent.children[1].background_normal = 'src/lighted.png'
            root = btn.parent.parent.parent.parent.parent.parent
            index_part = btn.parent.parent.children[10].index
            root.kit[index_part] = text
            for n in range(10):
                btn.parent.parent.children[n].background_normal = 'src/transparent.png'
                btn.parent.parent.children[n].background_down = 'src/transparent.png'
            root.check_kit()
            index_part = len(root.part_place.children) - 1 - index_part
            root.part_place.children[index_part].background_normal = 'src/lighted.png'


class WordPart(Button):
    pass


class SubLabel(Label):
    pass


class LongSubLabel(SubLabel):
    pass


class ViewSelection(GridLayout):
    words_by_group = {}
    lang = Language()
    all_compares = None
    root = None
    kit = None
    next_allowed = False

    def press_on_next(self, btn):
        if self.next_allowed:
            if btn == self.lang.title('TITLE_REMEMBERING_READY'):
                if self.helper.text == self.lang.title('TITLE_REMEMBERING_IMAGINATION'):
                    self.back.parent.remove_widget(self.back)
                    self.helper.text = self.lang.title('TITLE_REMEMBERING_RESIZE')
                elif self.helper.text == self.lang.title('TITLE_REMEMBERING_RESIZE'):
                    self.helper.text = self.lang.title('TITLE_REMEMBERING_ACTION')
                    self.next_allowed = False
                    Clock.schedule_once(self.next_allowed_true, 1)
                elif self.helper.text == self.lang.title('TITLE_REMEMBERING_ACTION'):
                    self.helper.text = self.lang.title('TITLE_REMEMBERING_DETAILS')
                    self.next_allowed = False
                    Clock.schedule_once(self.next_allowed_true, 6)
                elif self.helper.text == self.lang.title('TITLE_REMEMBERING_DETAILS'):
                    self.helper.text = self.lang.title('TITLE_REMEMBERING_SPEAK')
                    self.next_allowed = False
                    Clock.schedule_once(self.next_allowed_true, 1)
                elif self.helper.text == self.lang.title('TITLE_REMEMBERING_SPEAK'):
                    self.save_learn_word()
                    self.return_on_topic()
            else:
                self.compulsion()
                self.root.target_view.append(self.kit)

    def return_on_topic(self):
        self.root.target_view = ['topic', self.root.target_view[1]]
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def save_learn_word(self):
        user_store = self.root.store.get('user')
        top_name = self.root.target_view[1]
        user_store['user_topics'][top_name]['etch_top_word'][self.root.target_view[2]][
            'last_word_connect'] = round(time.time())
        user_store['user_topics'][top_name]['etch_top_word'][self.root.target_view[2]][
            'objects'] = self.kit
        user_store['user_topics'][top_name]['etch_top_word'][self.root.target_view[2]]['word_split'] = \
            self.root.target_view[-2]
        user_store = self.calculate_topic_progress2(user_store)
        self.root.store.put('user',
                            name=user_store['name'],
                            sex=user_store['sex'],
                            age=user_store['age'],
                            lang=user_store['lang'],
                            user_topics=user_store['user_topics'],
                            amail=user_store['amail'],
                            )

    def calculate_bar2(self, half, f_sum):
        if f_sum <= half:
            return round((0.5 / half) * f_sum, 2)
        else:
            return 1 + round(1 / half * (f_sum - half), 2)

    def calculate_topic_progress2(self, user_store):
        know = 0.01
        repeat = 0.01
        hair = 0.01
        top_name = self.root.target_view[1]
        user_store['user_topics'][top_name]['etch_top_word']
        time_repeat_by_number_repeat = {0: 3600 * 0.333,
                                        1: 3600 * 2,
                                        2: 3600 * 18,
                                        3: 3600 * 24 * 7,
                                        4: 3600 * 24 * 60,
                                        5: 3600 * 24 * 365,
                                        }
        word_count = len(user_store['user_topics'][top_name]['etch_top_word'])
        user_store['user_topics'][top_name]['time_to_repeat'] = 0
        for word in user_store['user_topics'][top_name]['etch_top_word']:
            last_word_connect = user_store['user_topics'][top_name]['etch_top_word'][word][
                'last_word_connect']
            cont_repeat = user_store['user_topics'][top_name]['etch_top_word'][word]['cont_repeat']
            time_to_repeat_top = user_store['user_topics'][top_name]['time_to_repeat']
            step_to_repeat_word = time_repeat_by_number_repeat[cont_repeat]
            if last_word_connect != 0 and (
                    time_to_repeat_top > last_word_connect + step_to_repeat_word or time_to_repeat_top == 0):
                user_store['user_topics'][top_name][
                    'time_to_repeat'] = round(last_word_connect + step_to_repeat_word)
            if last_word_connect != 0:
                hair += 1
                if cont_repeat > 0:
                    repeat += 1
                if cont_repeat == 5:
                    know += 1
        user_store['user_topics'][top_name]['know_pr'] = self.calculate_bar2(word_count / 2, know)
        user_store['user_topics'][top_name]['repeat_pr'] = self.calculate_bar2(word_count / 2, repeat)
        user_store['user_topics'][top_name]['hair_pr'] = self.calculate_bar2(word_count / 2, hair)
        return user_store

    def next_allowed_true(self, t):
        self.next_allowed = True

    def compulsion(self):
        self.scroll_space.remove_widget(self.scroll_space.children[0])
        for word in self.kit:
            word_part = WordPart()
            word_part.text = word
            word_part.size_hint_y = None
            word_part.height = '100sp'
            self.scroll_space.add_widget(word_part)
        self.next_btn.text = self.lang.title('TITLE_REMEMBERING_READY')
        self.next_btn.pos_hint = {'center_x': .5, 'center_y': .5}
        self.next_btn.size_hint_x = 0.7
        self.helper = LongSubLabel()
        self.helper.size_hint_y = 1
        self.helper.pos_hint = {'center_x': .5, 'center_y': .5}
        self.helper.text = self.lang.title('TITLE_REMEMBERING_IMAGINATION')
        self.scroll_space.add_widget(self.helper)

    def save_word(self):
        self.show_next_word()

    def show_next_word(self):
        self.root.target_view = ['topic', self.root.target_view[1]]
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def press_on_back(self):
        self.root.target_view.pop(-1)
        self.root.target_view[0] = 'splitting'
        self.root.remove_w('temp_view')
        self.root.draw_view()

    def choose_word(self, btn):
        for n in range(10):
            btn.parent.children[n].background_normal = 'src/transparent.png'
            btn.parent.children[n].background_down = 'src/transparent.png'
        btn.parent.children[10].children[1].background_normal = 'src/input.png'
        btn.background_normal = 'src/lighted.png'
        btn.background_down = 'src/lighted.png'
        index_part = len(self.part_place.children) - 1 - self.words_by_group[btn.text]
        self.part_place.children[index_part].background_normal = 'src/lighted.png'
        self.kit[self.words_by_group[btn.text]] = btn.text
        self.check_kit()

    def check_kit(self):
        self.next_allowed = True
        if '' in self.kit:
            self.next_allowed = False
        if self.next_allowed:
            self.next_btn.background_normal = 'src/btn_main.png'
            self.next_btn.background_down = 'src/btn_main_pressed.png'

    def selection(self):
        topic_name = self.lang.title(f"TITLE_TOP_NAME_{self.root.target_view[1].upper()}")
        self.header.text = topic_name + f"\n{self.root.target_view[2].lower()} = {self.root.target_view[3].lower()}"
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
        self.lang.set_lang(self.root.store.get('user')['lang'])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accept_btn = None
        self.helper = None


class VersionBtn(Button):
    pass


class SplitBtn(VersionBtn):
    pass


class ViewSplitWord(FloatLayout):
    root = []
    lang = Language()
    broken_word = {}

    def split_word(self):
        topic_name = self.lang.title(f"TITLE_TOP_NAME_{self.root.target_view[1].upper()}")
        self.header.text = topic_name + f"\n{self.root.target_view[2].lower()} = {self.root.target_view[3].lower()}"
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
    repeating_list = []
    answer_versions = []
    right_answers = {}
    helpers_by_word = {}
    timer_start = 0
    target_word = ''
    repeat = False
    check_answers = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store = JsonStore('hello.json')
        self.lang.set_lang(self.store.get('user')['lang'])

    def choose_version(self, btn):
        if self.check_answers:  # Check was showing answers
            if self.right_answers[self.target_word] == btn.text:
                self.store = JsonStore('hello.json')
                user_store = self.root.store.get('user')
                top_name = self.root.target_view[1]
                en_word = self.right_answers[self.target_word]

                ''' 
                        0: 3600 * 0.333,
                        1: 3600 * 2,
                        2: 3600 * 18,
                        3: 3600 * 24 * 7,
                        4: 3600 * 24 * 60,
                        5: 3600 * 24 * 365,
                                        
                                        
                
                '''
                if self.repeat:
                    self.repeating_list.pop(self.repeating_list.index(self.target_word))
                    if self.learning.text == self.lang.title('TITLE_TOPIC_BTN_OBJECTS'):
                        if user_store['user_topics'][top_name]['etch_top_word'][en_word]['cont_repeat'] < 5:
                            user_store['user_topics'][top_name]['etch_top_word'][en_word]['cont_repeat'] += 1
                    if self.learning.text == self.lang.title('TITLE_TOPIC_BTN_FORGET'):
                        user_store['user_topics'][top_name]['etch_top_word'][en_word]['cont_repeat'] = 1
                    if self.learning.text == self.lang.title('TITLE_TOPIC_BTN_BAD'):
                        user_store['user_topics'][top_name]['etch_top_word'][en_word]['cont_repeat'] = 0
                        user_store['user_topics'][top_name]['etch_top_word'][en_word]['last_word_connect'] = 0
                else:
                    self.learning_list.pop(self.learning_list.index(self.target_word))
                    user_store['user_topics'][top_name]['etch_top_word'][en_word]['cont_repeat'] = 5
                self.objects.text = ''
                self.splited.text = ''
                user_store['user_topics'][top_name]['etch_top_word'][en_word]['last_word_connect'] = round(
                    time.time())
                ans_speed = round(time.time()) - self.timer_start
                user_store['user_topics'][top_name]['etch_top_word'][en_word]['ans_speed'] = ans_speed
                user_store = self.calculate_topic_progress(user_store)
                self.root.store.put('user',
                                    name=user_store['name'],
                                    sex=user_store['sex'],
                                    age=user_store['age'],
                                    lang=user_store['lang'],
                                    user_topics=user_store['user_topics'],
                                    amail=user_store['amail']
                                    )

                if self.repeat:
                    if len(self.repeating_list) > 0:
                        self.repeating_mod()
                    else:
                        self.repeat = False
                        self.press_on('back')
                else:
                    self.learning_mod()
                self.clear_answers()
            else:
                if self.repeat:
                    btn.background_normal = 'src/btn_main_other.png'
                    btn.background_down = 'src/btn_main_other.png'
                else:
                    self.learn_word()

    def calculate_topic_progress(self, user_store):
        know = 0.01
        repeat = 0.01
        hair = 0.01
        top_name = self.root.target_view[1]
        time_repeat_by_number_repeat = {0: 3600 * 0.333,
                                        1: 3600 * 2,
                                        2: 3600 * 18,
                                        3: 3600 * 24 * 7,
                                        4: 3600 * 24 * 60,
                                        5: 3600 * 24 * 365,
                                        }
        word_count = len(user_store['user_topics'][top_name]['etch_top_word'])
        user_store['user_topics'][top_name]['time_to_repeat'] = 0
        for word in user_store['user_topics'][top_name]['etch_top_word']:
            last_word_connect = user_store['user_topics'][top_name]['etch_top_word'][word][
                'last_word_connect']
            cont_repeat = user_store['user_topics'][top_name]['etch_top_word'][word]['cont_repeat']
            time_to_repeat_top = user_store['user_topics'][top_name]['time_to_repeat']
            step_to_repeat_word = time_repeat_by_number_repeat[cont_repeat]
            if last_word_connect != 0 and (
                    time_to_repeat_top > last_word_connect + step_to_repeat_word or time_to_repeat_top == 0):
                user_store['user_topics'][top_name][
                    'time_to_repeat'] = round(last_word_connect + step_to_repeat_word)
            if last_word_connect != 0:
                hair += 1
                if cont_repeat > 0:
                    repeat += 1
                if cont_repeat == 5:
                    know += 1
        user_store['user_topics'][top_name]['know_pr'] = self.calculate_bar(word_count / 2, know)
        user_store['user_topics'][top_name]['repeat_pr'] = self.calculate_bar(word_count / 2, repeat)
        user_store['user_topics'][top_name]['hair_pr'] = self.calculate_bar(word_count / 2, hair)
        return user_store

    def calculate_bar(self, half, f_sum):
        if f_sum <= half:
            return round(0.5 / half * f_sum, 2)
        else:
            return 1 + round(1 / half * (f_sum - half), 2)

    def learn_word(self, btn=''):
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
        self.learning.bind(on_release=self.learn_word)
        self.answers.text = self.lang.title('TITLE_TOPIC_BTN_ANSWERS')
        self.target_word = self.learning_list[random.randint(0, len(self.learning_list)) - 1]
        self.header.text = self.target_word

    def repeating_mod(self):
        self.learning.text = self.lang.title('TITLE_TOPIC_BTN_OBJECTS')
        self.learning.bind(on_release=self.show_helper)
        self.answers.text = self.lang.title('TITLE_TOPIC_BTN_ANSWERS')
        self.target_word = self.repeating_list[random.randint(0, len(self.repeating_list)) - 1]
        self.header.text = self.target_word

    def show_helper(self, btn):
        if btn.text == self.lang.title('TITLE_TOPIC_BTN_BAD'):
            pass
        elif btn.text == self.lang.title('TITLE_TOPIC_BTN_FORGET'):
            self.splited.text = ', '.join(self.helpers_by_word[self.right_answers[self.target_word]]['word_split'])
            self.objects.text = ', '.join(self.helpers_by_word[self.right_answers[self.target_word]]['objects'])
            btn.text = self.lang.title('TITLE_TOPIC_BTN_BAD')
        else:
            btn.text = self.lang.title('TITLE_TOPIC_BTN_FORGET')
            self.objects.text = ', '.join(self.helpers_by_word[self.right_answers[self.target_word]]['objects']).lower()

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
        self.repeating_list = []
        self.answer_versions = []
        self.right_answers = {}
        time_repeat_by_number_repeat = {0: 3600 * 0.333,
                                        1: 3600 * 2,
                                        2: 3600 * 18,
                                        3: 3600 * 24 * 7,
                                        4: 3600 * 24 * 60,
                                        5: 3600 * 24 * 365,
                                        }
        if top['hair_pr'] < 2:
            if 1 and (round(time.time()) > top['time_to_repeat'] and top['time_to_repeat'] != 0):
                self.repeat = True
            else:
                for word in top['etch_top_word']:
                    ask_word = words_by_lvl[self.root.store.get('user')['lang']][top_name][word]
                    self.answer_versions.append(word)
                    if top['etch_top_word'][word]['last_word_connect'] == 0:
                        self.right_answers[ask_word] = word
                        self.learning_list.append(ask_word)
                self.learning_mod()
        else:
            self.repeat = True
        if self.repeat:
            for word in top['etch_top_word']:
                ask_word = words_by_lvl[self.root.store.get('user')['lang']][top_name][word]
                self.answer_versions.append(word)

                last_word_connect = round(time.time()) - top['etch_top_word'][word]['last_word_connect']
                time_past_from_repeat = time_repeat_by_number_repeat[top['etch_top_word'][word]['cont_repeat']]
                if top['etch_top_word'][word]['last_word_connect'] != 0 and last_word_connect > time_past_from_repeat:
                    self.helpers_by_word[word] = {'objects': top['etch_top_word'][word]['objects'],
                                                  'word_split': top['etch_top_word'][word]['word_split']}
                    self.right_answers[ask_word] = word
                    self.repeating_list.append(ask_word)

                if top['etch_top_word'][word]['last_word_connect'] == 0:
                    self.learning_list.append(ask_word)
            self.repeating_mod()


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
        App.get_running_app().root.ids['temp_view'].choose_top(topic_name.top_name)


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
                                'time_to_repeat': 0,
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
            self.root.store.put('user',
                                name=user_store['name'],
                                sex=user_store['sex'],
                                age=user_store['age'],
                                lang=user_store['lang'],
                                user_topics=user_store['user_topics'],
                                amail=user_store['amail']
                                )

        elif text == 'ua':
            self.root.ids['temp_view'].ru.background_normal = 'src/btn_main_other.png'
            self.root.ids['temp_view'].ua.background_normal = 'src/btn_main.png'
            user_store = self.root.store.get('user')
            user_store['lang'] = 'ua'
            self.root.store.put('user',
                                name=user_store['name'],
                                sex=user_store['sex'],
                                age=user_store['age'],
                                lang=user_store['lang'],
                                user_topics=user_store['user_topics'],
                                amail=user_store['amail']
                                )

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
        self.store = JsonStore('hello.json')

    def give_root(self, root):
        self.root = root
        n = 0
        know_pr = 0
        repeat_pr = 0
        hair_pr = 0
        for top_name in self.store.get('user')['user_topics'].keys():
            n += 1
            know_pr += float(self.store.get('user')['user_topics'][top_name]["know_pr"])
            repeat_pr += float(self.store.get('user')['user_topics'][top_name]["repeat_pr"])
            hair_pr += float(self.store.get('user')['user_topics'][top_name]["hair_pr"])
        know_pr = know_pr / n
        repeat_pr = repeat_pr / n
        hair_pr = hair_pr / n

        if know_pr > 1:
            self.progress_know.size_hint_y = 1 + ((know_pr - 1) * 10)
            self.progress_know_text.text = str(50 + round(50 * (know_pr - 1)))
        else:
            self.progress_know.size_hint_y = know_pr
            if round(know_pr, 4) == 0.01:
                self.progress_know_text.text = '0'
            else:
                self.progress_know_text.text = str(round(50 * know_pr))
        if repeat_pr > 1:
            self.progress_repeat.size_hint_y = 1 + ((repeat_pr - 1) * 10)
            self.progress_repeat_text.text = str(50 + round(50 * (repeat_pr - 1)))
        else:
            self.progress_repeat.size_hint_y = repeat_pr
            if round(repeat_pr, 4) == 0.01:
                self.progress_repeat_text.text = '0'
            else:
                self.progress_repeat_text.text = str(round(50 * repeat_pr))
        if hair_pr > 1:
            self.progress_hair.size_hint_y = 1 + ((hair_pr - 1) * 10)
            self.progress_hair_text.text = str(50 + round(50 * (hair_pr - 1)))
        else:
            self.progress_hair.size_hint_y = hair_pr
            if round(hair_pr, 4) == 0.01:
                self.progress_hair_text.text = '0'
            else:
                self.progress_hair_text.text = str(round(50 * hair_pr))

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
    user_topics = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.can_choose_topic = None
        self.top_names_to_repeat = None
        self.other_top_names = None
        self.front_top_names = None
        self.pb = None
        self.store = JsonStore('hello.json')
        self.chose_main_view()
        self.draw_view()
        self.user_topics = None

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
            self.store = JsonStore('hello.json')
            self.user_topics = self.store.get('user')['user_topics']
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
            self.front_top_names = []
            self.other_top_names = []
            self.top_names_to_repeat = []
            self.user_topics = self.store.get('user')['user_topics']
            self.can_choose_topic = True
            for top_name in words_by_lvl[self.store.get('user')['lang']].keys():
                time_to_repeat = self.user_topics[top_name]['time_to_repeat']
                time_now = round(time.time())
                if time_to_repeat != 0 and time_to_repeat < time_now:
                    self.front_top_names.append(top_name)
                    self.top_names_to_repeat.append(top_name)
                elif 0.01 < self.user_topics[top_name]['hair_pr']:
                    self.front_top_names.append(top_name)
                    if self.user_topics[top_name]['hair_pr'] < 0.9:
                        self.can_choose_topic = False
                else:
                    self.other_top_names.append(top_name)
            self.topic_keys = self.front_top_names + self.other_top_names

            if self.can_choose_topic:
                self.ids['temp_view'].alert.opacity = 1
            if len(self.top_names_to_repeat) > 0:
                self.ids['temp_view'].alert.opacity = 1
                alert = self.lang.title('TITLE_ALERT_REPEAT_COUNT_TOPICS').replace('{}',
                                                                                   str(len(self.top_names_to_repeat)))
                self.ids['temp_view'].alert_text.text = alert

        top_name = self.topic_keys[self.started]
        global temp_data
        self.started += 1
        self.ids['load_view'].my_pb.height = self.ids['load_view'].height / 38 * self.started
        temp_data = f"src/{top_name}.png"
        layout = TopicLayout()
        layout.top_info_layout.progress_know.size_hint_y = self.user_topics[top_name]['know_pr']
        if layout.top_info_layout.progress_know.size_hint_y == 0:
            layout.top_info_layout.progress_know.size_hint_y = 0.01
        layout.top_info_layout.progress_repeat.size_hint_y = self.user_topics[top_name]['repeat_pr']
        if layout.top_info_layout.progress_repeat.size_hint_y == 0:
            layout.top_info_layout.progress_repeat.size_hint_y = 0.01
        layout.top_info_layout.progress_hair.size_hint_y = self.user_topics[top_name]['hair_pr']
        if layout.top_info_layout.progress_hair.size_hint_y == 0:
            layout.top_info_layout.progress_hair.size_hint_y = 0.01
        count_words = str(len(self.user_topics[top_name]['etch_top_word']))
        layout.btn.text = self.lang.title(f"TITLE_TOP_NAME_{top_name.upper()}")
        if top_name in self.top_names_to_repeat:
            layout.btn.text += ': ' + self.lang.title("TITLE_TOPIC_NAME_REPEAT")
        else:
            layout.btn.text += ': ' + count_words
        layout.btn.top_name = top_name

        if len(self.top_names_to_repeat) > 0:
            if top_name not in self.top_names_to_repeat:
                layout.opacity = 0.5
                layout.btn.background_down = 'src/topic.png'
            else:
                layout.btn.bind(on_press=layout.press_on_topic)
        else:
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
            self.target_view = 'home'  # home
            # ['splitting', 'Животные', 'cow', 'корова']
            # ['selection', 'Животные', 'animal', 'животное', ['эни', 'мэл']]
        else:
            self.target_view = 'sing_up'

    def give_root(self, root):
        self.root.append(root)


class ViewExcept(BoxLayout):
    pass


class MyApp(App):
    view_manager = None

    def build(self):
        global exeption
        self.icon = 'src/Logo.png'
        if exeption == '':
            self.view_manager = ViewManager()
        else:
            self.view_manager = ViewExcept()
            btn = MainBtn()
            btn.text = 'Send to server'
            btn.bind(on_release=self.send_error)
            self.view_manager.add_widget(btn)
            self.view_manager.except_text.text = f"Error catch\n\n{str(exeption)}!"
        return self.view_manager

    def send_error(self, btn):
        self.view_manager


exeption = ''
if __name__ == '__main__':
    if error_catch:
        try:
            MyApp().run()
        except Exception as e:
            exeption = e
            print(e)
            MyApp().run()
    else:
        MyApp().run()
