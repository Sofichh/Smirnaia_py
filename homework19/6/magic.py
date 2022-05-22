class Water:

    def __add__(self, other):
        if isinstance(other, Fire):
            return Vapor()
        if isinstance(other, Air):
            return Lightning()
        if isinstance(other, Land):
            return Lava()


class Air:

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other, Fire):
            return Lightning()
        if isinstance(other, Land):
            return Dust()


class Land:

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Air):
            return Dust()


class Fire:

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Land):
            return Lava()
        elif isinstance(other, Water):
            return Vapor()
        else:
            return None


class Lightning:
    res = 'Молния - объединение огня и воздуха'


class Lava:
    res = 'Лава - объединение огня и земли'


class Vapor:
    res = 'Пар  - объединение огня и воды'


class Dirt:
    res = 'Грязь - объединение земли и воды'


class Dust:
    res = 'Пыль - объединение земли и воздуха'


class Storm:
    res = 'Шторм - бъединение воды и воздуха'