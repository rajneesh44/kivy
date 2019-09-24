'''
In this file we will be adding buttons on an interface using kivy
'''
import kivy
from kivy.app import App
from  kivy.uix.floatlayout import FloatLayout



	


class MyApp(App):				#App is creating a constructor itself so we dont have to use init function.
	def build(self):
		return FloatLayout()


		




if __name__ == "__main__":
	MyApp().run()