from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (480, 850)


def get_ingridients(m):
    print([m])
    salt = str(round(15 * m / 1000, 1))
    nitro = str(round(10 * m / 1000, 1))
    dextrose = str(round(5 * m / 1000, 1))
    starts = str(round(0.5 * m / 1000, 1))
    salting_time = str(round(2 * m / 500))
    return {
        'salt': salt,
        'nitro': nitro,
        'dextrose': dextrose,
        'starts': starts,
        'salting_time': salting_time,
    }


class Container(GridLayout):
    text_input = ObjectProperty()
    salt = ObjectProperty()
    nitro = ObjectProperty()
    dextrose = ObjectProperty()
    starts = ObjectProperty()
    salting_time = ObjectProperty()

    def calculate(self):
        try:
            mass = float(self.text_input.text)
        except:
            mass = 0.0
        ingridients = get_ingridients(m=mass)
        self.salt.text = ingridients.get('salt')
        self.nitro.text = ingridients.get('nitro')
        self.dextrose.text = ingridients.get('dextrose')
        self.starts.text = ingridients.get('starts')
        self.salting_time.text = ingridients.get('salting_time')


class MyApp(App):
    def build(self):
        return Container()

    pass


if __name__ == '__main__':
    app = MyApp()
    app.run()
