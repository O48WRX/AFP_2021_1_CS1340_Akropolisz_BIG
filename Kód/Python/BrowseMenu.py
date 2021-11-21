from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file("KV_Files/Browse.kv")


class MainWindow(FloatLayout):
    pass


class BrowseMenu(App):
    def build(self):
        main_window = MainWindow()
        return main_window

browsemenu = BrowseMenu()
browsemenu.run()
