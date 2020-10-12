class Main:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        return print('omnomnom')

    def speak(self):
        return print(self.voice)


class Birds(Main):
    def get_eggs(self):
        return print('eggs collected')


class MilkyWay(Main):
    def get_milk(self):
        return print('milk collected')


class Animals(Main):
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        return print('omnomnom')

    def speak(self):
        return print(self.voice)


# создаём класс для каждого животного:
class Goose(Main):
    animal_type = 'Гуси'
    # переопределяем атрибут voice для каждого животного в его классе:
    voice = 'gagaga'


class Chicken(Main):
    animal_type = 'Куры'
    voice = 'kokoko'


class Duck(Main):
    animal_type = 'Утки'
    voice = 'quack'


class Cow(Main):
    animal_type = 'Коровы'
    voice = 'mooooo'


class Goat(Main):
    animal_type = 'Козы'
    voice = 'beeeee'


class Sheep(Main):
    animal_type = 'Овечки'
    voice = 'meeeee'

    def get_wool(self):
        return print('wool collected')


res = Chicken()


res.speak()
