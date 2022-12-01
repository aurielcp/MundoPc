from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._idComputadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''

if __name__ == '__main__':
    monitor1 = Monitor('Philips', '6in')
    monitor2 = Monitor('Acer', '8in')
    teclado1 = Teclado('Usb', 'Lg')
    teclado2 = Teclado('Cable', 'Hp')
    raton1 = Raton('Usb', 'Hp')
    raton2 = Raton('Acer', 'Bluetooth')
    computadora1 = Computadora('Gamer', monitor1, teclado1, raton1)
    print(computadora1)