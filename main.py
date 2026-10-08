import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        lbl = Label(text="ЭГТР-6 Фото\nСреда готова!", font_size='24sp', halign='center')
        btn = Button(text="Выход", size_hint=(1, 0.2))
        btn.bind(on_release=lambda x: App.get_running_app().stop())
        layout.add_widget(lbl)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MainApp().run()
