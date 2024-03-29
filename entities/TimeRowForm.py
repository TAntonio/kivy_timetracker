__author__ = 'dandro'

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

WINDOW_SIZE = 400, 768


class TimeRowForm(Widget):
	def __init__(self, top, **kwargs):
		super(TimeRowForm, self).__init__(**kwargs)

		self.start_top = top
		self.label_top = self.start_top - 50
		self.text_project_top = self.label_top - 27
		self.text_description_top = self.text_project_top - 91
		self.submit_button_top = self.text_description_top - 40

		self.add_widget(Label(text="Add New Row", size=(100, 30), pos=(10, self.label_top)))

		self.text_project = TextInput(hint_text='Project Name', multiline=False, size=(WINDOW_SIZE[0] - 20, 30),
			pos=(10, self.text_project_top), background_color=(1, 1, 1, 0.2), background_normal='fake',
			background_active='fake')
		self.add_widget(self.text_project)

		self.text_description = TextInput(hint_text='Task Description', multiline=True, size=(WINDOW_SIZE[0] - 20, 80),
			pos=(10, self.text_description_top), background_color=(1, 1, 1, 0.2), background_normal='fake',
			background_active='fake')
		self.add_widget(self.text_description)

		self.submit_button = Button(text="Add Log", size=(100, 30), pos=(WINDOW_SIZE[0] - 110, self.submit_button_top))
		self.submit_button.bind(on_press=self.add_new_row)
		self.add_widget(self.submit_button)

	def add_new_row(self, button):
		self.parent.dispatch('on_row_added', self.text_project.text, self.text_description.text)