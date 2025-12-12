from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class HKD(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/hkd.kv")
        super().__init__(**kwargs)