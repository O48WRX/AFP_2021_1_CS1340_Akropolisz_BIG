import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
cwd = (os.getcwd())
os.environ["Kivy_HOME"] = cwd + "/conf"

from kivy import Config
from kivy.app import App
from kivy.uix.widget import Widget


class MainWindow(App):
    def build(self):
        return Widget()


MainWindow().run()

