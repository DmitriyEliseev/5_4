class House:
    houses_history = []

    def __new__(cls, name, number_of_floors):
        cls.houses_history.append(name)
        return super(House, cls).__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def validate_type(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Аргумент должен быть объектом класса House")

    def go_to(self, new_floor):
        floor = 0
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor} - Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def compare(self, other):
        self.validate_type(other)

    def __eq__(self, other):
        self.compare(other)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        self.compare(other)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        self.compare(other)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        self.compare(other)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        self.compare(other)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        self.compare(other)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        self.validate_type(other)
        if isinstance(other, int):
            self.number_of_floors += other
        return self

    def __radd__(self, other):
        self.validate_type(other)
        return self.__add__(other)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)