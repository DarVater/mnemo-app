from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.core.window import Window
from datetime import datetime

from language import Language

Window.size = 540, 960


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


class ViewSingUp(FloatLayout):
    root = []
    name = ''
    gender = ''
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
        self.user_register('Male')

    def choose_female(self):
        self.user_register('Female')

    def user_register(self, gender):
        self.root.store.put('user',
                            name=self.name,
                            sex=self.gender,
                            age=self.age,
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

    def add_w(self, view):
        if view == 'temp_view':
            temp_view = ViewSingUp()
            temp_view.give_root(self)
            temp_view.size = 333, 333
            self.ids['temp_view'] = temp_view
            self.add_widget(temp_view)
            self.ids['temp_view'].btn.text = self.lang.title('TITLE_BTN_NEXT')
            self.ids['temp_view'].header.text = self.lang.title('TITLE_HI_WHAT_ARE_YOUR_NAME')

    def chose_main_view(self):
        if 'user' in self.store:
            self.target_view = 'home'
        else:
            self.target_view = 'sing_up'

    def draw_view(self):
        if self.target_view == 'sing_up':
            self.add_w('temp_view')

    def give_root(self, root):
        self.root.append(root)

    if 0:
        self.store.put('user', name='Ванька', sex='male', age=17)
        print(self.store.get('tito')['age'])
        self.text = str(self.store.get('tito')['age'])


class MyApp(App):
    def build(self):
        view_manager = ViewManager()
        return view_manager


if __name__ == '__main__':
    MyApp().run()
