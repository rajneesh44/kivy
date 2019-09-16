'''
In this file we will be adding buttons on an interface using kivy
'''
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self,**kwargs):
		super(MyGrid,self).__init__(**kwargs)
		self.cols = 2
		self.add_widget(Label(text="Name: "))
		self.name= TextInput(multiline=False)
		self.add_widget(self.name)

		self.add_widget(Label(text="Last: "))
		self.lastname= TextInput(multiline=False)
		self.add_widget(self.lastname)

		self.add_widget(Label(text="Email: "))
		self.email= TextInput(multiline=False)
		self.add_widget(self.email)

		self.submit = Button(text="Submit",font_size=40)
		self.add_widget(self.submit)



class MyApp(App):				#App is creating a constructor itself so we dont have to use init function.
	def build(self):
		return MyGrid()


if __name__ == "__main__":
	MyApp().run()