'''
In this file we will be adding buttons on an interface using kivy
'''
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget 

class NewGrid(Widget):
	pass
	

class NewApp(App):				#App is creating a constructor itself so we dont have to use init function.
	def build(self):
		return NewGrid()


if __name__ == "__main__":
	NewApp().run()