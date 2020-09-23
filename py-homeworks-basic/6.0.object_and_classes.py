# Задание 1
class Bird:
    food = ("трава", "семена")
    collect_eggs = 'Собрали яйца'


class Goose(Bird):
    voice = ("Га-га-га", "Шшшшшшш")
    food = "семена"

    def __init__(self, name):
        self.name = name

    def собрать_яйца(self):
        print('собрали яйца')


class Chiken(Bird):
    voice = ("Кудах-Кудах")
    food = "семена"

    def __init__(self, name):
        self.name = name


class Duck(Bird):
    voice = ("Кряяя-Кряяяя")
    food = "семена"

    def __init__(self, name):
        self.name = name


class Animal:
    food = ("трава")


class Cow(Animal):
    voice = ("Мууууууу")
    food = "трава"
    milk = 'подоили'

    def __init__(self, name):
        self.name = name


class Sheep(Animal):
    voice = ("Бээээээ")
    food = "трава"

    def __init__(self, name, cut):
        self.name = name
        self.cut = cut


class Goat(Animal):
    voice = ("Мээээ")
    food = "трава"
    milk = 'подоили'

    def __init__(self, name):
        self.name = name


# Задание 2
class beards:
    def __init__(self, name, weight, species):
        self.name = name
        self.weight = weight
        self.species = species


class animal:
    def __init__(self, name, weight, species):
        self.name = name
        self.weight = weight
        self.species = species


goose1 = beards('Серый', 5, 'goose1')
goose2 = beards('Белый', 6, 'goose2')
chiken1 = beards('Ко-Ко', 7, 'chiken1')
chiken2 = beards('Какуреку', 8, 'chiken2')
duck = beards('Кряква', 9, 'duck')

cow = animal('Манька', 56, 'cow')
sheep1 = animal('Барашек', 11, 'sheep1')
sheep2 = animal('Кудрявый', 12, 'sheep2')
goat1 = animal('Рога', 123, 'goat1')
goat2 = animal('Копыта', 14, 'goat2')

list_beards = goose1.__dict__, goose2.__dict__, chiken1.__dict__, chiken2.__dict__, duck.__dict__, cow.__dict__, sheep1.__dict__, sheep2.__dict__, goat1.__dict__, goat2.__dict__

num_sum_beards = goose1.weight + goose2.weight + chiken1.weight + chiken2.weight + duck.weight
num_sum_animals = cow.weight + sheep1.weight + sheep2.weight + goat1.weight + goat2.weight

num_max_animals = max(goose1.weight, goose2.weight, chiken1.weight, chiken2.weight, duck.weight, cow.weight,
                      sheep1.weight, sheep2.weight, goat1.weight, goat2.weight)

for i in list_beards:
    if num_max_animals in i.values():
        maxi = i.get('species')

print(f"""
Общий вес птиц = {num_sum_beards}
Общий вес животных = {num_sum_animals}
Cамая тяжелое животное: {maxi}
""")


# Задания 3 и 4
class Track:
    name_track = 'Highway to Hell'
    duration_track = int(3)

    def show(self):
        print(f"<{self.name_track}-{self.duration_track}>")


class Album:
    name_album = 'Back in Black'
    group = 'AC/DC'
    list_track1 = {'Hells Bells': 4, 'Shoot to Thrill': 5, 'What Do You Do for Money Honey': 3,
                   'Givin the Dog a Bone': 3}
    list_track2 = {'Have a Drink on Me': 2,
                   'Shake a Leg': 5, 'Rock And Roll Aint Noise Pollution': 6}

    def get_track(self):
        for i, j in self.list_track1.items():
            print(f"Название трека: {i}, длина трека: {j}мин.")

    def add_track(self, new_track, new_duration):
        self.list_track1.update({new_track: new_duration})
        print(self.list_track1)

    def get_duration(self):
        print(f"Длительность альбома: {sum(self.list_track1.values())} минут")

    def get_duration_all_album(self):  # Задание 4
        print(f"Длительность альбома1: {sum(self.list_track1.values())} минут")
        print(f"Длительность альбома2: {sum(self.list_track2.values())} минут")


res = Album()
res2 = Track()

res2.show()
res.get_track()
res.add_track('New', 4)
res.get_duration()
res.get_duration_all_album()
