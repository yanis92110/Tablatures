from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class TablatureApp(App):
    def build(self):
        self.tablature = [
            ["--"], ["--"], ["--"], ["--"], ["--"], ["--"]
        ]

        # Création de l'interface
        root = BoxLayout(orientation="vertical")

        # Label du nom du fichier
        self.nom_fichier_input = TextInput(text="Nom du fichier", multiline=False, font_size=20, size_hint_y=None, height=40)
        root.add_widget(self.nom_fichier_input)

        # Zone pour afficher la tablature
        self.tablature_display = ScrollView()
        self.tablature_text = TextInput(font_size=16, readonly=True, size_hint=(1, None), height=300)
        self.tablature_display.add_widget(self.tablature_text)
        root.add_widget(self.tablature_display)

        # Grid de boutons pour les notes
        grid = GridLayout(cols=17, spacing=5, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        for i in range(6):
            for j in range(17):
                button = Button(text=str(j), on_press=lambda instance, x=i, y=j: self.ajouter_note(x, y))
                grid.add_widget(button)

        root.add_widget(grid)

        # Boutons de fonction
        button_layout = BoxLayout(size_hint_y=None, height=50)
        button_layout.add_widget(Button(text="Finir la corde", on_press=self.ajouter_note_harmonieux))
        button_layout.add_widget(Button(text="Vide", on_press=self.corde_vide))
        button_layout.add_widget(Button(text="Supprimer", on_press=self.supprimer_corde))
        button_layout.add_widget(Button(text="Enregistrer", on_press=self.sauvegarder_tablature))
        button_layout.add_widget(Button(text="Quitter", on_press=self.quitter_application))
        root.add_widget(button_layout)

        return root

    def afficher_tablature(self):
        self.tablature_text.text = ""
        cordes_noms = ["E ", "A ", "D ", "G ", "B ", "e "]
        for i, corde in enumerate(self.tablature):
            ligne = cordes_noms[i] + "| " + " ".join(str(note) for note in corde) + "\n"
            self.tablature_text.text += ligne

    def ajouter_note(self, corde, case):
        index_corde = int(corde)  # Convertit l'entrée en index (0-5)
        if 0 <= index_corde < 6:
            if case == "p":
                case = case + "-"
            elif case == "⌢":
                case = "⌢" + " "
            elif case < 10:
                case = str(case) + "-"
            self.tablature[index_corde].append(case)
        self.afficher_tablature()

    def ajouter_note_harmonieux(self, instance):
        max_len = max(len(c) for c in self.tablature)
        for corde in self.tablature:
            while len(corde) < max_len:
                corde.append("--")
        self.afficher_tablature()

    def corde_vide(self, instance):
        for corde in self.tablature:
            corde.append("--")
        self.afficher_tablature()

    def supprimer_corde(self, instance):
        for corde in self.tablature:
            corde.pop()
        self.afficher_tablature()

    def sauvegarder_tablature(self, instance):
        try:
            nom_fichier = self.nom_fichier_input.text
            with open(f"{nom_fichier}.txt", "w") as fichier:
                for corde in self.tablature:
                    fichier.write(" ".join(str(note) for note in corde) + "\n")
            print("Tablature enregistrée avec succès")
        except Exception as e:
            print(f"Erreur : {e}")

    def quitter_application(self, instance):
        self.stop()


if __name__ == "__main__":
    TablatureApp().run()
