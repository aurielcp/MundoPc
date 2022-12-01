'''Creacion clase Raton'''
from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, marca, tipoEntrada):
        super().__init__(tipoEntrada, marca)
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones

    def __str__(self):
        return f'Id Raton: {self._idRaton}, {super().__str__()}'

if __name__ == '__main__':
    raton1 = Raton('Usb', 'Hp')
    print(raton1)
    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)