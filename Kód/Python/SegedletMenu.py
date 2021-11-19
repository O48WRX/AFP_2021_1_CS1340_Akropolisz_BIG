from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App

Builder.load_file("KV_Files/Segedlet.kv")

class MainWindow(FloatLayout):
    pass


class SegedWindow(App):
    def build(self):
        segedwindow = MainWindow()
        return segedwindow


segedwindow = SegedWindow()
segedwindow.run()
