from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

LIST = ["hey", "there", "duuuude"]


class IDDemo(App):
    def build(self):
        self.title = "Lable Lists"
        self.root = Builder.load_file('dynamic_kivy_widgets.kv')
        return self.root


    def make_labels(self):
        for name in LIST:
            button = Button(text=name)
            print(button)