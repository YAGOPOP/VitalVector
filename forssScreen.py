from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.lang import Builder

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