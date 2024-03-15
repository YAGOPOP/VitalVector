from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ListProperty

class EkgsScreen(Screen):
    Builder.load_file("EkgsScreen.kv")

    backolor = ListProperty([.95, .78, .71, 1])


    currentSquaresValue = 0
    current4SSValue = 0


    ButtonsFontSize = StringProperty("20sp")
    LabelsFontSize = StringProperty("40sp")



    def updateLabels(self):
        if self.currentSquaresValue == 0:
            self.current4SSValue = 0
        if self.current4SSValue < 0:
            self.current4SSValue = 0
        self.ids.squaresLabel.text = "Клеточки: " + str(self.currentSquaresValue)
        self.ids.forSSLabel.text = "ЧСС: " + str(self.current4SSValue)


    def countSquaresAnd4SS(self, instance, speed = 25):
        self.currentSquaresValue = int(str(self.currentSquaresValue) + instance.text)
        if self.currentSquaresValue != 0:
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
        self.countSquaresAnd4SS(instance)