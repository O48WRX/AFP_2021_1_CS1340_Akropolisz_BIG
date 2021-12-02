from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.video import Video
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file("KV_Files/MainMenu.kv")

# itt lehet állítani színt a háttérhez.
Window.clearcolor = (48 / 255, 48 / 255, 48 / 255, 1)

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

# Help screen létrehozása


class Help(Screen):
    pass

# Screen manager deklarálása

class SelectFile1(Screen):
    pass


class SelectFile2(Screen):
    pass


class SelectFile3(Screen):
    pass


class SelectFile4(Screen):
    pass


class MyCollage(Screen):
    pass



class Screen_manager(ScreenManager):
    path_data1 = ObjectProperty(SelectFile1)
    path_data2 = ObjectProperty(SelectFile2)
    path_data3 = ObjectProperty(SelectFile3)
    path_data4 = ObjectProperty(SelectFile4)


screen_manager = Screen_manager()

# Screenek hozzáadása a button-ök által hivatkozott nevekkel
screen_manager.add_widget(MainMenu(name="main_menu"))
screen_manager.add_widget(CreateCollage(name="user_collage"))
screen_manager.add_widget(Demo(name="demo"))
screen_manager.add_widget(Help(name="help"))
screen_manager.add_widget(SelectFile1(name="vid1_fileselect"))
screen_manager.add_widget(SelectFile2(name="vid2_fileselect"))
screen_manager.add_widget(SelectFile3(name="vid3_fileselect"))
screen_manager.add_widget(SelectFile4(name="vid4_fileselect"))
screen_manager.add_widget(MyCollage(name="my_collage"))
# App létrehozása


class VideoCreator(App):
    def build(self):
        return screen_manager

# App futtatása

vc_app = VideoCreator()
vc_app.run()
