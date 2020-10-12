# Задание 1.1
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


# Задание 1.2
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


class Goose(Main):
    animal_type = 'Гуси'
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


goose = Goose('Grey', 6)
chicken = Chicken('Riyba', 3)
duck = Duck('Kria', 4)
cow = Cow('Byrka', 6)
goat = Goat('Pavel', 6)
sheep = Sheep('Valera', 6)

list_main = [goose, chicken, duck, cow, goat, sheep]

for i in list_main:
    print(Main.feed(i), Main.speak(i))


# Задание 2.1
class Track:
    name_track = 'Highway to Hell'
    duration_track = int(3)

    def __str__(self):
        print(f"<{self.name_track}-{self.duration_track}>")


class Album:
    def __str__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        result = []
        for track in self.tracks:
            result.append(track.show())
        return result

    def get_duration(self):
        result = 0
        for track in self.tracks:
            result += track.duration
        return result

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.tracks.append(track)


res = Album()
res2 = Track()

res2.__str__()
res.__str__()


# Задание 2.1
class Track:
    name_track = 'Highway to Hell'
    duration_track = int(6)

    name_track2 = 'The show must go on'
    duration_track2 = int(4)

    def __str__(self):
        print(f"<{self.name_track}-{self.duration_track}>")

    def track1(self, name, lan):
        print(f"{name},{lan}")

    def track2(self, name, lan):
        print(f"{name},{lan}")

    def __gt__(self, other):
        result = self.duration_track > self.duration_track2
        print(result)


class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        result = []
        for track in self.tracks:
            result.append(track.show())
        return result

    def get_duration(self):
        result = 0
        for track in self.tracks:
            result += track.duration
        return result

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.tracks.append(track)


res = Album()
res2 = Track()
