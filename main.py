import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require('1.11.1') 
class MyKivyApp(App):
    def build(self):         
        lable= Label(text ="Hello World !",
        color =(225,0,0,0),  font_size=100)
        return lable
MyKivyApp().run()