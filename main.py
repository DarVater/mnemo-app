from kivy.app import App
from kivy.uix.layout import Layout


class ViewManager(Layout):
    target_view = 'sing_up'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Main(App):
    def build(self):
        return ViewManager()


if __name__ == '__main__':
    Main().run()
