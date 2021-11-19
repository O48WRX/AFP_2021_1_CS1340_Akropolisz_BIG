import os

from kivy.lang import Builder
from kivy import Config
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

os.environ["KIVY_NO_CONSOLELOG"] = "1"
cwd = (os.getcwd())
os.environ["Kivy_HOME"] = cwd + "/conf"
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", "1")
Config.set("graphics", "borderless", "0")

Config.write()

Builder.load_file("KV_Files/MainWindow.kv")


class MainWindow(FloatLayout):
    pass


class MainMenu(App):
    def build(self):
        main_window = MainWindow()
        return main_window

mainmenu = MainMenu()
mainmenu.run()

