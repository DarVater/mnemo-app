from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.core.window import Window
from datetime import datetime

from language import Language
from word_by_topics import words_by_lvl

Window.size = 540, 960


class ViewChooseTopics(FloatLayout):
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
            self.root.store.put('user', lang='ru')
        elif text == 'ua':
            self.root.ids['temp_view'].ru.background_normal = 'src/btn_main_other.png'
            self.root.ids['temp_view'].ua.background_normal = 'src/btn_main.png'
            self.root.store.put('user', lang='ua')

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


class TopicInfoLayout(BoxLayout):
    pass


class TopicLayout(BoxLayout):
    pass


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
                etch_top_word[top_word] = {'cont_repeat': 0, 'ans_speed': 64}
            user_topics[top] = {'know_pr': 0.01,
                                'repeat_pr': 0.01,
                                'hair_pr': 0.01,
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
            self.root.store.put('user', lang='ru')
        elif text == 'ua':
            self.root.ids['temp_view'].ru.background_normal = 'src/btn_main_other.png'
            self.root.ids['temp_view'].ua.background_normal = 'src/btn_main.png'
            self.root.store.put('user', lang='ua')

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
    lang = Language()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store = JsonStore('hello.json')
        self.chose_main_view()
        self.draw_view()

    def remove_w(self, w_name):
        self.remove_widget(self.ids['temp_view'])
        self.ids.pop('temp_view')

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
            temp_view = ViewChooseTopics()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view

            self.add_widget(temp_view)
            self.ids['temp_view'].header.text = self.lang.title('TITLE_TOPIC_HEADER')
            self.ids['temp_view'].alert_text.text = self.lang.title('TITLE_TOPIC_UNBLOCK_CHOOSE_TOPIC')
            self.add_etch_top()

    def add_etch_top(self):
        user_topics = self.store.get('user')['user_topics']
        for top_name in user_topics.keys():
            print(top_name, user_topics[top_name] )
            layout = TopicLayout()
            layout.top_layout.progress_know.size_hint_y = user_topics[top_name]['know_pr']
            layout.top_layout.progress_repeat.size_hint_y = user_topics[top_name]['repeat_pr']
            layout.top_layout.progress_hair.size_hint_y = user_topics[top_name]['hair_pr']
            layout.btn.text = top_name
            self.ids['temp_view'].topics_grid.add_widget(layout)

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
            self.target_view = 'home' # home all_topics
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
