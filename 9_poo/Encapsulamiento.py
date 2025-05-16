class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.obtener_saldo())  # Salida: 150
# cuenta.__saldo  # Error: AttributeError (por ser privado)
