

class Conta:

    CODIGO_BANCO = "002"

    def __init__(self, numero, titular, saldo=0.0, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"


    def __str__(self):
        return f"Conta numero {self.__numero} - Titular {self.__titular}"

    def __repr__(self):
        return f"Conta numero {self.__numero} - Titular {self.__titular}"

    def extrato(self):
        print(f"Saldo do titular {self.__titular}: {self.__saldo}")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        saldo_disponivel = (self.__saldo + self.__limite)
        return valor_a_sacar <= saldo_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")



    def transferir(self, conta_a_receber, valor):
        self.saca(valor)
        conta_a_receber.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"

    @classmethod
    def codigo_banco(cls):
        cls.codigo_banco()

    @limite.setter
    def limite(self, limite):
        if limite >= 0:
            self.__limite = limite
        else:
            raise ValueError("Limite must be positive")