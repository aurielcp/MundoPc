class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'Id Monitor: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

if __name__ == '__main__':
    monitor1 = Monitor('Philips', '6in')
    print(monitor1)
    monitor2 = Monitor('Acer', '8in')
    print(monitor2)