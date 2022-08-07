
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    def __repr__(self):
        return self.__nome.title()

    def __repr__(self):
        return self.__nome.title()

    @property
    def nome(self):
        return self.nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome