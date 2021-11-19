from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

Builder.load_file("KV_Files/UserCreate.kv")


class MainWindow(FloatLayout):
    pass


class UserCreate(App):
    def build(self):
        main_window = MainWindow()
        return main_window


usercreate = UserCreate()
usercreate.run()
