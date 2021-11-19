from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class MainWindow(FloatLayout):
    pass


class DemoMenu(App):
    def build(self):
        main_window = MainWindow()
        return main_window

demomenu = DemoMenu()
demomenu.run()