from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

#app size
Window.size = (300, 500)

Builder.load_file('calc.kv')

class CalcLayout(Widget):
  def clear(self):
    self.ids.calc_input.text = '0'

  def button_input(self, button):
    # variable for text
    existing_input = self.ids.calc_input.text

    if existing_input == "Error":
      existing_input = ''

    # handle zero 
    if existing_input == '0':
      self.ids.calc_input.text = ''
      self.ids.calc_input.text = f'{button}'
    else:
      #add to string the nubmer upon button press
      self.ids.calc_input.text = f'{existing_input}{button}'

  def math_sign(self, sign):
    existing_input = self.ids.calc_input.text

    # insert signs to text
    self.ids.calc_input.text = f'{existing_input}{sign}'

  def result(self):
    existing_input = self.ids.calc_input.text

    try:
      answer = eval(existing_input)
      self.ids.calc_input.text = str(answer)
    except:
      self.ids.calc_input.text = "Error"

class CalcApp(App):
  def build(self):
    return CalcLayout()
  
if __name__ == '__main__':
  CalcApp().run()

