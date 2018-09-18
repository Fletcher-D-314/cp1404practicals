from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class IDDemo(App):
    def build(self):
        Window.size = (500, 500)
        self.title = "Demoing the id attribute"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root
IDDemo().run()