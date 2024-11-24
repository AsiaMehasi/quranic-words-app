from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class FlashcardApp(App):
    def build(self):
        self.words = [
            {"arabic": "كتب", "meaning": "to write", "root": "ك-ت-ب"},
            {"arabic": "علم", "meaning": "to know", "root": "ع-ل-م"},
        ]
        self.index = 0

        self.layout = BoxLayout(orientation='vertical')
        self.arabic_label = Label(text=self.words[self.index]["arabic"], font_size=50)
        self.meaning_label = Label(text="Tap to reveal meaning", font_size=20)
        self.next_button = Button(text="Next Word", on_press=self.next_word)

        self.layout.add_widget(self.arabic_label)
        self.layout.add_widget(self.meaning_label)
        self.layout.add_widget(self.next_button)

        return self.layout

    def next_word(self, instance):
        self.meaning_label.text = f"Meaning: {self.words[self.index]['meaning']}\nRoot: {self.words[self.index]['root']}"
        self.index = (self.index + 1) % len(self.words)
        self.arabic_label.text = self.words[self.index]["arabic"]

if _name_ == "_main_":
    FlashcardApp().run()
