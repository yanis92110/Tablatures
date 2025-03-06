from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import os

class GameView(BoxLayout):
    def __init__(self):
        super(GameView,self).__init__()

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.text_input = TextInput(hint_text="Écris quelque chose")
        btn = Button(text="Valider", on_press=self.afficher_texte)

        layout.add_widget(self.text_input)
        layout.add_widget(btn)
        return layout

    def afficher_texte(self, instance):
        print("Texte entré :", self.text_input.text)
        return GameView()

appli=MyApp()

appli.run()
