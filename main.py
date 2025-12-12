from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
Window.maximize()

from screens.screens import* 

class WindowManager(ScreenManager):
    pass

class Hasil_Kali_Dalam(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [
            HKD(name="hkd"),
            Aksioma(name='aksioma'),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
if __name__ == "__main__":
    LabelBase.register(name="TTSlabs", fn_regular="kv/assets/fonts/TTSlabsTrial-Bold.otf")
    LabelBase.register(name="Monradok", fn_regular="kv/assets/fonts/MonradokTrial-Regular.otf")
    LabelBase.register(name="Glacial", fn_regular="kv/assets/fonts/Glacial-Indifference.otf")
    Hasil_Kali_Dalam().run()