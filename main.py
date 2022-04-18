from kivy.app import App
from kivy.uix.layout import Layout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.label import Label

class ViewManager(Label):
    target_view = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store = JsonStore('hello.json')
        self.store.put('tito', name='Mathieu', org='kivy', age=27)

        print(self.store.get('tito')['age'])
        self.text = str(self.store.get('tito')['age'])

class Main(App):
    def build(self):
        return ViewManager()


if __name__ == '__main__':
    Main().run()
