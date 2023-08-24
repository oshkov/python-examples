# Задается класс
class Car():
    """Описание машины"""

    def __init__(self, model, color, fuelTank, fuelNow):
        """Свойства машины"""
        self.model = model
        self.color = color
        self.fuelTank = fuelTank
        self.fuelNow = fuelNow

    """Функция перекрашивания авто"""
    def recolor(self, color):
        self.color = color
        print(f'Цвет авто изменен на {color}')

    """Функция заправки авто"""
    def refuel(self, fuel):
        if fuel + self.fuelNow > self.fuelTank:
            print(f'Авто заправлено полностью. В баке {self.fuelTank} л. топлива. Остались лишние {fuel + self.fuelNow - self.fuelTank} л. топлива')
            self.fuelNow = self.fuelTank
        else:
            self.fuelNow = fuel + self.fuelNow
            print(f'Авто заправлено. В баке {self.fuelNow} л. топлива')
        pass


# Создание объекта на подобии класса
nissan = Car('Nissan', 'Черный', 50, 20)

# Вывод атрибутов объекта
print(f'Модель авто: {nissan.model}; цвет авто: {nissan.color}; объём бака {nissan.fuelTank}; в баке {nissan.fuelNow} л. топлива')

# Вызов метода класса
nissan.recolor('Красный')
nissan.refuel(45)

# Добавление атрибутов
nissan.__setattr__('production', 2009)
print(nissan.production)

# Вывод атрибутов экземпляра
print(nissan.__dict__)