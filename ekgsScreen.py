from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.lang import Builder

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