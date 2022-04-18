from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

from language import Language


Window.size = 540, 960


class ViewButton(Button):
    text = 'asdasd'
    def on_touch_down(self, touch):
        if 'temp_view' in App.get_running_app().root.ids:
            App.get_running_app().root.remove_w('temp_view')
        else:
            App.get_running_app().root.add_w('temp_view')


class ViewSingUp(FloatLayout):
    root = []
    name = ''
    lang = Language()

    def give_root(self, root):
        self.root = root

    def next(self):
        temp_view = self.root.ids['temp_view']
        if temp_view.header.text == self.lang.title('TITLE_HI_WHAT_ARE_YOUR_NAME'):
            name = temp_view.input.text
            next_allowed = True
            if len(name) > 10:
                temp_view.help_text.text = self.lang.title('TITLE_NAME_NOT_LONGER')
                next_allowed = False
            not_allowed_character = '\'1234567890!@#$%^&*()_+=-";:.,/\\*`~'
            for character in name:
                if character in not_allowed_character:
                    next_allowed = False
                    temp_view.help_text.text = self.lang.title('TITLE_NAME_ONLY_CHARACTERS')



class ViewManager(FloatLayout):
    target_view = ''
    root = []
    lang = Language()

    def __init__(self , **kwargs):
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
