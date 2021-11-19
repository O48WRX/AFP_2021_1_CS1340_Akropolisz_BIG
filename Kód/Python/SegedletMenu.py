from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class MainWindow(FloatLayout):
    pass


class SegedWindow(App):
    def build(self):
        segedwindow = MainWindow()
        return segedwindow


segedwindow = SegedWindow()
segedwindow.run()
