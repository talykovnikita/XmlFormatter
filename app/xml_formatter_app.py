import pyperclip
import xml.dom.minidom
from pyexpat import ExpatError


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import XmlLexer


class XMlFormatterApp(App):
    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)

        self.title = config.get(
            "GUI",
            "program_title",
        )
        self.main_layout = BoxLayout(padding=[25], spacing=5, orientation="vertical")
        self.text_boxes_layout = BoxLayout(spacing=5, size_hint=(1, 0.96))

        self.input_textbox = CodeInput(lexer=XmlLexer())
        self.input_textbox.bind(text=self.format_input)

        self.output_textbox = CodeInput(lexer=XmlLexer(), readonly=1)

        self.copy_button = Button(
            text=config.get("GUI", "copy_button_text"),
            on_press=self.copy_to_clipboard,
            size_hint=(1, 0.04),
        )

        self.error_message = config.get("GUI", "error_message")

    def format_input(self, instance, text):
        try:
            lines = text.split("\n")
            non_empty_lines = [line.strip() for line in lines if line.strip() != ""]
            one_line = "".join(non_empty_lines)
            dom = xml.dom.minidom.parseString(one_line)
            self.output_textbox.text = dom.toprettyxml()
        except ExpatError:
            self.output_textbox.text = self.error_message

    def copy_to_clipboard(self, instance):
        pyperclip.copy(self.output_textbox.text)

    def build(self):
        self.text_boxes_layout.add_widget(self.input_textbox)
        self.text_boxes_layout.add_widget(self.output_textbox)

        self.main_layout.add_widget(self.text_boxes_layout)
        self.main_layout.add_widget(self.copy_button)
        return self.main_layout
