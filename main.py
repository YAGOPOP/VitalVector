from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from EkgsScreen import *
from ForssScreen import *

__version__ = "0.90.0.1"

class VitalVector(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ForssScreen())
        sm.add_widget(EkgsScreen())
        return sm
    

if __name__ == '__main__':
    VitalVector().run()