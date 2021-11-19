from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

Builder.load_file("KV_Files/DemoMenu.kv")


class MainWindow(FloatLayout):
    pass


class DemoMenu(App):
    def build(self):
        main_window = MainWindow()
        return main_window


demomenu = DemoMenu()
demomenu.run()
