from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty

from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color

class CanvasExample1(Widget):
    pass
class CanvasExample2(Widget):
    pass
class CanvasExample3(Widget):
    pass
class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500,60,500), close=True, width=3)
            Color(0,1,0,0.5, mode='rgba')
            Line(circle=(400,200,50), width=2)
            Line(rectangle=(700,500,150,100), width=5)
            Rectangle(pos=(700,300), size=(150,100))

class CanvasExample5(Widget):
    pass

class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello")
    count = NumericProperty(0)
    count_enabled = BooleanProperty(False)

    def on_button_clicked(self):
        print('Button clicked')
        if self.count_enabled:
            self.count = self.count + 1
            self.my_text = f'Button clicked {self.count} times'
    def on_toggle_button_state(self, widget):
        print('Toggle state: ' + widget.state)
        if widget.state == 'normal':
            widget.text = 'OFF'
            self.count_enabled = False
        else:
            widget.text = 'ON'
            self.count_enabled = True
    def on_text_validate(self, widget, label):
        print('on_text_validate')
        label.text = widget.text
        print(label.xablau)
            

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'rl-bt'
        # self.padding = dp(10)
        self.spacing = (dp(10),dp(20))
        for i in range(100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = 'vertical'
    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     b3 = Button(text='C')
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass


if __name__ == '__main__':
    TheLabApp().run()