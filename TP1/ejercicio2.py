import random
import os
import time


class Baldosa:

    def __init__(self):
        self.sucio = random.randrange(4)
        self.limpiado = False

    def mostrar(self):
        if self.sucio == 0:
            return "[   ]"
        elif self.sucio == 1:
            return "[ + ]"
        elif self.sucio == 2:
            return "[ x ]"
        elif self.sucio == 3:
            return "[ # ]"

    def limpiar(self):
        if self.sucio == 1:
            self.sucio = 0
        elif self.sucio == 2:
            self.sucio = 1


class Piso:
    baldosas = []

    def __init__(self, size):
        self.size = size
        for i in range(self.size):
            self.baldosas.append(Baldosa())

    def mostrar(self):
        out = ""
        for i in range(self.size):
            out += self.baldosas[i].mostrar()
        return out

    def limpiadas(self):
        contador = 0
        for i in range(self.size):
            if self.baldosas[i].limpiado:
                contador += 1
        return contador


class Aspiradora:
    def __init__(self, piso):
        self.posicion = random.randrange(size)
        self.direccion = "Derecha"
        self.piso = piso
        self.movimientos = 0

    def mostrar(self):
        out = ""
        for i in range(self.piso.size):
            if self.posicion == i:
                out += "[ A ]"
            elif self.piso.baldosas[i].limpiado:
                out += "[ p ]" #la "p" es que paso
            else:
                out += "[   ]"
        print(out)
        print(self.piso.mostrar())

    def mover(self):
        try:
            if self.direccion == "Derecha":
                movimiento = 1
            else:
                movimiento = -1
            self.piso.baldosas[self.posicion + movimiento]
            if (self.posicion + movimiento) < 0:
                raise
            print("Moviendo hacia la  " + self.direccion)
            self.movimientos += 1
            self.posicion = self.posicion + movimiento
        except:
            if self.direccion == "Derecha":
                self.direccion = "Izquierda"
            else:
                self.direccion = "Derecha"
            self.mover()

    def iniciar(self):
        while self.piso.limpiadas() < self.piso.size:
            os.system("clear")
            self.mostrar()
            for j in range(2):
                if self.piso.baldosas[self.posicion].sucio != 0 or self.piso.baldosas[self.posicion].limpiado:
                    self.movimientos += 1
                    self.piso.baldosas[self.posicion].limpiar()
            self.piso.baldosas[self.posicion].limpiado = True
            self.mover()
            time.sleep(1)


if __name__ == '__main__':
    rango_piso = [5, 15]
    size = int(random.randint(rango_piso[0], rango_piso[1]))
    piso = Piso(size)
    aspiradora = Aspiradora(piso)
    aspiradora.iniciar()

