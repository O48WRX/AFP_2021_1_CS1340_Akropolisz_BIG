from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file("KV_Files/MainMenu.kv")

# itt lehet állítani színt a háttérhez.
Window.clearcolor = (0, .6, 0, 1)

# Screenek létrehozása
# MainMenu Screen létrehozása


class MainMenu(Screen):
    pass

# CreateCollage Screen létrehozása


class CreateCollage(Screen):
    pass

# Demo screen létrehozása


class Demo(Screen):
    pass


# Screen manager deklarálása


screen_manager = ScreenManager()

# Screenek hozzáadása a button-ök által hivatkozott nevekkel
screen_manager.add_widget(MainMenu(name="main_menu"))
screen_manager.add_widget(CreateCollage(name="user_collage"))
screen_manager.add_widget(Demo(name="demo"))

# App létrehozása


class VideoCreator(App):
    def build(self):
        return screen_manager

# App futtatása


vc_app = VideoCreator()
vc_app.run()
