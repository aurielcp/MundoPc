from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.contadorRatones += 1
        super().__init__(tipoEntrada, marca)
        self._idRaton = Teclado.contadorRatones

    def __str__(self):
        return f'Id Teclado: {self._idRaton}, {super().__str__()}'

if __name__ == '__main__':
    teclado1 = Teclado('Usb', 'Lg')
    print(teclado1)
    teclado2 = Teclado('Cable', 'Hp')
    print(teclado2)