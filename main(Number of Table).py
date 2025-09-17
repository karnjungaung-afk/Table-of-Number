from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# /c:/Users/karnj/OneDrive/Documents/Kivy-basic/main(Number of Table).py

Window.size = (360, 400)


class TableApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # input row
        input_row = BoxLayout(size_hint_y=None, height=40, spacing=10)
        self.num_input = TextInput(hint_text='Enter a number (e.g. 5)',
                                   input_filter='int',
                                   multiline=False)
        generate_btn = Button(text='Generate Table', size_hint_x=None, width=140)
        generate_btn.bind(on_release=self.generate_table)
        input_row.add_widget(self.num_input)
        input_row.add_widget(generate_btn)

        # scroll area for results
        self.scroll = ScrollView()
        self.results_layout = GridLayout(cols=1, spacing=4, size_hint_y=None)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        self.scroll.add_widget(self.results_layout)

        root.add_widget(input_row)
        root.add_widget(self.scroll)
        return root

    def generate_table(self, *args):
        text = (self.num_input.text or '').strip()
        # clear previous
        self.results_layout.clear_widgets()
        if not text:
            self.results_layout.add_widget(Label(text='Please enter a number.', size_hint_y=None, height=30))
            return
        try:
            n = int(text)
        except ValueError:
            self.results_layout.add_widget(Label(text='Invalid number.', size_hint_y=None, height=30))
            return

        # generate table lines: "i X n = result"
        for i in range(1, 13):
            line = f"{n} X {i} = {i * n}"
            lbl = Label(text=line, size_hint_y=None, height=30)
            self.results_layout.add_widget(lbl)


if __name__ == '__main__':
    TableApp().run()