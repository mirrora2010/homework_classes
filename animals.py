# 1. Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
class Fauna():
    def __init__(self, name, size, paws, hoofs, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.hoofs = hoofs
        self.wings = wings
        print(self.name, self.size, self.paws, self.hoofs, self.wings)

        def info(self):
            print(self.name, self.size, self.paws, self.hoofs, self.wings)

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'hoofs': self.hoofs,
            'wings': self.wings,
        })


class Birds(Fauna):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Fauna.__init__(self, name_bird, 'small', 2, 'None', 'Yes')


class Cattle(Fauna):
    name_animal = ['Коровы', 'Козы', 'Овцы']

    def __init__(self, name_animal):
        self.name_animal = name_animal
        Fauna.__init__(self, name_animal, 'big', 4, 'Yes', 'None')


class Cows(Cattle):
    def __init__(self, name, size, paws, hoofs, wings):
        super().__init__(name, size, paws, hoofs, wings)
        self.hoofs = 4


Ducks = Birds('Утки')
Chickens = Birds('Куры')
Geese = Birds('Гуси')

Cows = Cattle('Коровы')
Goats = Cattle('Козы')
Sheeps = Cattle('Овцы')

print('\n Класс Птицы:',
      '\n Утки: {}'.format(Ducks),
      '\n Куры: {}'.format(Chickens),
      '\n Гуси: {}'.format(Geese))

print('\n Класс Скот:',
      '\n Коровы: {}'.format(Cows),
      '\n Козы: {}'.format(Goats),
      '\n Овцы: {}'.format(Sheeps))


# 2 Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
class Care():
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def give_food(self):
        self.give_food = 'животное накормлено'

    def give_no_food(self):
        self.give_no_food = 'животное не накормлено'


class Geese(Care):
    def get_eggs(self):
        self.get_eggs = 'яйца собраны'

    def get_no_eggs(self):
        self.get_no_eggs = 'яйца не собраны'


class Сhickens(Geese):
    pass


class Ducks(Geese):
    pass


class Сows(Care):
    def get_milk(self):
        self.get_milk = 'подоена'

    def get_no_milk(self):
        self.get_no_milk = 'не подоена'


class Goats(Сows, Care):
    pass


class Sheeps(Care):
    def get_wool(self):
        self.get_wool = 'подстрижена'

    def get_no_wool(self):
        self.get_no_wool = 'не подстрижена'


goose_white = Geese('Белый', 4, 'гага')
goose_white.give_food()  # гусь накормлен
goose_white.get_eggs()  # яйца собраны

goose_grey = Geese('Серый', 4, 'гага')
goose_grey.give_food()  # гусь накормлен
goose_grey.get_eggs()  # яйца собраны

cow_manya = Сows('Манька', 120, 'мууу')
cow_manya.give_food()  # корова накормлена
cow_manya.get_milk()  # корова подоена

sheep_barashek = Sheeps('Барашек', 30, 'беее')
sheep_barashek.give_food()  # баран накормлен
sheep_barashek.get_wool()  # баран подстрижен

sheep_kudrya = Sheeps('Кудрявый', 35, 'беее')
sheep_kudrya.give_food()  # баран накормлен
sheep_kudrya.get_wool()  # баран подстрижен

chichen_koko = Сhickens('Ко-ко', 2, 'коко')
chichen_koko.give_food()  # курица накормлена
chichen_koko.get_eggs()  # яйца собраны

chichen_kukareku = Сhickens('Кукареку', 3, 'коко')
chichen_kukareku.give_food()  # курица накормлена
chichen_kukareku.get_eggs()  # яйца собраны

duck_kryakva = Ducks('Кряква', 4, 'кря')
duck_kryakva.give_food()  # утка накормлена
duck_kryakva.get_eggs()  # яйца собраны

goat_roga = Goats('Рога', 30, 'мееее')
goat_roga.give_food()  # коза накормлена
goat_roga.get_milk()  # коза подоена

goat_kopyto = Goats('Копыто', 35, 'мееее')
goat_kopyto.give_food()  # коза накормлена
goat_kopyto.get_milk()  # коза подоена

# Необходимо посчитать общий вес всех животных(экземпляров класса); вывести название самого тяжелого животного.

animals = [goose_white, goose_grey, cow_manya, sheep_barashek, sheep_kudrya, chichen_koko, chichen_kukareku,
           duck_kryakva, goat_roga, goat_kopyto]

general_weight = 0
max_weight = 0
for animal in animals:
    print(f'\n{animal.name} весит {animal.weight} кг')
    general_weight += animal.weight
    if max_weight < animal.weight:
        max_weight = animal.weight
print(f'\nОбщий вес всех животных: {general_weight} кг')

for animal in animals:
    if max_weight == animal.weight:
        print(f'\nСамое тяжелое животное {animal.name} - весит {animal.weight} кг')

