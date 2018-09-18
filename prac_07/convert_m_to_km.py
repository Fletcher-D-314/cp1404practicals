from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class IDDemo(App):
    def build(self):
        Window.size = (600, 240)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_calculation(self):
        try:
            value = float(self.root.ids.input_miles.text)
            if value >0:
                kilometers = value * MILES_TO_KM
                self.root.ids.output_miles.text = str(kilometers)
            else:
                self.root.ids.input_miles.text = "0.0"
        except ValueError:
            self.root.ids.input_miles.text = "0.0"

    def handle_up_down(self, increment):
        try:
            value = float(self.root.ids.input_miles.text) + increment
            self.root.ids.input_miles.text = str(value)
        except ValueError:
            self.root.ids.input_miles.text = "0.0"

IDDemo().run()
