from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

__version__ = '0.0.1'

with open('bots/token.txt') as f:
	f = f.read()
	if f:
		TOKEN = f
	else:
		TOKEN = 'Введи сюда свой токен'

with open('bots/bot_name.txt') as f:
	f = f.read()
	if f:
		NAME = f
	else:
		NAME = 'Введи сюда обращение к боту\n(либо просто не трогай это поле, чтобы сделать бота без обращения)'
		

class MyApp(App):
	def build(self):
		self.start = False
		self.home_page = BoxLayout(orientation='vertical')
		self.input_token = TextInput(text=TOKEN)
		self.btn_token = Button(text='Сохранить токен', on_press = self.save_token)
		self.input_botname = TextInput(text=NAME)
		self.btn_botname = Button(text='Сохранить обращение', on_press = self.save_botname)
		self.btn_start = Button(text='Запустить бота', on_press = self.bot_start)
		self.home_page.add_widget(self.input_token)
		self.home_page.add_widget(self.btn_token)
		self.home_page.add_widget(self.input_botname)
		self.home_page.add_widget(self.btn_botname)
		self.home_page.add_widget(self.btn_start)
		return self.home_page
	
	def save_token(self, instance):
		with open('bots/token.txt', 'w') as f:
			f.write(self.input_token.text)
			
	def save_botname(self, instance):
		if self.input_botname == NAME:
			return
		with open('bots/bot_name.txt', 'w') as f:
			f.write(self.input_botname.text)
			
	def bot_start(self, instance):
		if self.start:
			instance.text = 'Запустить бота'
		else:
			instance.text = 'Остановить бота'
		self.start = not self.start
if __name__ == '__main__':
	MyApp().run()