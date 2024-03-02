from kivy.app import App
from forssScreen import forssScreen


__version__ = "0.46.1.5"




class VitalVector(App):
    def build(self):
        return forssScreen()

if __name__ == "__main__":
    VitalVector().run()





















# from kivy.config import Config
#
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
#
# from kivy.uix.label import Label
# from kivy.uix.widget import Widget
#
# Config.set("graphics", "resizable", 0)
# Config.set("graphics", "width", 400)
# Config.set("graphics", "height", 500)
