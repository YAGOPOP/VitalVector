from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import ListProperty


class ForssScreen(Screen):
    Builder.load_file("ForssScreen.kv")

    backolor = ListProperty([.95, .78, .71, 1])


    currentAgeValue = 0
    current4SSValue = 0

    ButtonsFontSize = StringProperty("20sp")
    LabelsFontSize = StringProperty("40sp")



    def updateLabels(self):
        if self.currentAgeValue == 0:
            self.current4SSValue = 0
        if self.current4SSValue < 0:
            self.current4SSValue = 0
        self.ids.ageLabel.text = "Возраст: " + str(self.currentAgeValue)
        self.ids.forSSLabel.text = "Целевая ЧСС: " + str(self.current4SSValue)


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
        self.countAgeAnd4SS(instance)