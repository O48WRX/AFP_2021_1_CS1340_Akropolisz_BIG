from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file("KV_Files/MainMenu.kv")

Window.clearcolor = (0, .6, 0, 1)

class MainMenu(Screen):
    pass
class MainWindow(FloatLayout):
    pass

class CreateCollage(Screen):
    pass

screen_manager = ScreenManager()


