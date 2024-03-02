from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

__version__ = "0.45.3"


class forssScreen(BoxLayout):
    Builder.load_file('VitalVectorDesign.kv')


    roundation = 1

    currentAgeValue = 0
    current4SSValue = 0

    ageLabel = ObjectProperty()
    forSSLabel = ObjectProperty()

    sootn = Window.size[0] / Window.size[1]

    ButtonsFontSize = NumericProperty(round(sootn * Window.size[0] * 0.047))
    fontAllowance = ButtonsFontSize

    def updateLabels(self):
        if self.currentAgeValue == 0:
            self.current4SSValue = 0
        self.ageLabel.text = str(self.currentAgeValue)
        self.forSSLabel.text = str(self.current4SSValue)


    def countAgeAnd4SS(self, instance):
        self.currentAgeValue = int(str(self.currentAgeValue) + instance.text)
        self.current4SSValue = round((220 - self.currentAgeValue) * 0.85, self.roundation)
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
        self.current4SSValue = round((220 - self.currentAgeValue) * 0.85, self.roundation)
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
#
#
# class l3App(App):
#
#     def update_label(self):
#         self.lbl.text = self.formula
#
#     def count_res(self, instance):
#         self.formula = str(eval(self.formula))
#         self.update_label()
#
#     def add_num(self, instance):
#         if self.formula == "0":
#             self.formula = ""
#         self.formula += str(instance.text)
#         print(self.formula)
#         self.update_label()
#
#     def add_oper(self, instance):
#         self.formula += str(instance.text)
#         self.update_label()
#
#     def build(self):
#         self.formula = "0"
#         bl = BoxLayout(orientation="vertical", padding = [15])
#
#         gl = GridLayout(cols=4, spacing=5, size_hint = (1, .6))
#
#         self.lbl = Label(text="",
#                             font_size = 40,
#                             halign = "right",
#                             size_hint = (1, .4),
#                             valign = "center",
#                             text_size = (400 - 50, 500 * .4))
#
#         bl.add_widget(self.lbl)
#
#         bl.add_widget(gl)
#
#         gl.add_widget(Button(text="7", on_press = self.add_num))
#         gl.add_widget(Button(text="8", on_press = self.add_num))
#         gl.add_widget(Button(text="9", on_press = self.add_num))
#         gl.add_widget(Button(text="*", on_press = self.add_oper))
#
#         gl.add_widget(Button(text="4", on_press = self.add_num))
#         gl.add_widget(Button(text="5", on_press = self.add_num))
#         gl.add_widget(Button(text="6", on_press = self.add_num))
#         gl.add_widget(Button(text="-", on_press = self.add_oper))
#
#         gl.add_widget(Button(text="1", on_press = self.add_num))
#         gl.add_widget(Button(text="2", on_press = self.add_num))
#         gl.add_widget(Button(text="3", on_press = self.add_num))
#         gl.add_widget(Button(text="+", on_press = self.add_oper))
#
#         gl.add_widget(Button(text="/", on_press = self.add_oper))
#         gl.add_widget(Button(text="0", on_press = self.add_num))
#         gl.add_widget(Button(text=".", on_press = self.add_num))
#         gl.add_widget(Button(text="=", on_press = self.count_res))
#
#         return bl
#
#
# if __name__ == "__main__":
#     l3App().run()
