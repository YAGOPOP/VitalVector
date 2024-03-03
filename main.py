from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.core.window import Window

class ekgsScreen(BoxLayout):
    Builder.load_file('ekgsScreen.kv')

    backolor = ListProperty([.41, 1, .98, 1])


    currentSquaresValue = 0
    current4SSValue = 0

    relativeFontSize = 20

    ButtonsFontSize = StringProperty(str(relativeFontSize) + "sp")
    LabelsFontSize = StringProperty(str(relativeFontSize * 2) + "sp")


    squaresLabel = ObjectProperty()
    forSSLabel = ObjectProperty()
    written4SSLabel = ObjectProperty()
    writtenSquaresLabel = ObjectProperty()


    def updateLabels(self):
        if self.currentSquaresValue == 0:
            self.current4SSValue = 0
        self.squaresLabel.text = str(self.currentSquaresValue)
        self.forSSLabel.text = str(self.current4SSValue)


    def countSquaresAnd4SS(self, instance, speed = 25):
        self.currentSquaresValue = int(str(self.currentSquaresValue) + instance.text)
        if speed == 25:
            self.current4SSValue = round(60 / (self.currentSquaresValue * .04))
        else:
            self.current4SSValue = round(60 / (self.currentSquaresValue * .02))
        self.updateLabels()

    def clear(self, instance):
        self.currentSquaresValue = 0
        self.current4SSValue = 0
        self.updateLabels()

    def DeleteLast(self, instance):
        if self.currentSquaresValue > 9:
            self.currentSquaresValue = int(str(self.currentSquaresValue)[0:-1:])
        else:
            self.currentSquaresValue = 0
        self.current4SSValue = round((220 - self.currentSquaresValue) * 0.85)
        self.updateLabels()

    def knowSize(self):
        li = [Window.width / 10, Window.height / 10]
        return li

class forssScreen(BoxLayout):
    Builder.load_file('forssScreen.kv')

    backolor = ListProperty([.41, 1, .98, 1])


    currentAgeValue = 0
    current4SSValue = 0

    relativeFontSize = 20

    ButtonsFontSize = StringProperty(str(relativeFontSize) + "sp")
    LabelsFontSize = StringProperty(str(relativeFontSize * 2) + "sp")


    ageLabel = ObjectProperty()
    forSSLabel = ObjectProperty()
    written4SSLabel = ObjectProperty()
    writtenAgeLabel = ObjectProperty()


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

__version__ = "0.46.2.7.5"

class forSSwindow(Screen):
    pass

class ekgsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kvfile = Builder.load_file("testmain.kv")

class VitalVector(App):
    def build(self):
        return ekgsScreen()
    

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
