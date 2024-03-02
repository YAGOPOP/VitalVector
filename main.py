from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.metrics import Metrics
from kivy.lang import Builder

__version__ = "0.46.1.2"

class forssScreen(BoxLayout):
    Builder.load_file('VitalVectorDesign.kv')


    currentAgeValue = 0
    current4SSValue = 0

    ageLabel = ObjectProperty()
    forSSLabel = ObjectProperty()

    ButtonsFontSize = StringProperty("30sp")
    LabelsFontSize = StringProperty("60sp")

    def updateLabels(self):
        if self.currentAgeValue == 0:
            self.current4SSValue = 0
        self.ageLabel.text = str(self.currentAgeValue)
        self.forSSLabel.text = str(self.current4SSValue)


    def countAgeAnd4SS(self, instance):
        self.currentAgeValue = int(str(self.currentAgeValue) + instance.text)
        self.current4SSValue = round((220 - self.currentAgeValue) * 0.85)
        self.updateLabels()

    def clear(self, instance):
        self.currentAgeValue = 0
        self.current4SSValue = 0
        self.updateLabels()

    def DeleteLast(self, instance):
        if self.currentAgeValue > 9:
            self.currentAgeValue = int(str(self.currentAgeValue)[0:-1:])
        else:
            self.currentAgeValue = 0
        self.current4SSValue = round((220 - self.currentAgeValue) * 0.85)
        self.updateLabels()


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
