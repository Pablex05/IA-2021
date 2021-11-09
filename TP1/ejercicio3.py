import sys
import os
import time
from random import randrange, randint

# Ejercicio 3: Agente basado en objetivo
# Objetivo: Limpiar las baldosas en la menor cantidad posible de movimientos

# La aspiradora no distingue tipos de manchas, solo sabe si el piso está limpio o sucio
# Conoce el tamaño del pasillo y recuerda si ya limpió una baldosa
# Termina cuando ya limpio todas las baldosas


def limpiarConsola():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # detecta si se esta usando Windows
        command = 'cls'  # cambia el comando a cls
    os.system(command)


class Baldosa:
    def __init__(self):
        self.sucio = randrange(4)
        self.limpiado = False

    def mostrar(self):
        if self.sucio == 0:
            return "[ ]"  # Limpio
        elif self.sucio == 1:
            return "[+]"  # Poco sucio - Necesita una pasada
        elif self.sucio == 2:
            return "[X]"  # Sucio - Necesita dos pasadas
        elif self.sucio == 3:
            return "[#]"  # Mancha permanente - No se limpia nunca

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
        out = " "
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
        self.posicion = randrange(size)
        mitad = size / 2
        if self.posicion >= mitad:
            self.direccion = "Derecha"
        else:
            self.direccion = "Izquierda"
        self.piso = piso
        self.movimientos = 0

    def mostrar(self):
        out = ""
        for i in range(self.piso.size):
            if self.posicion == i:
                out += "[A]"
            elif self.piso.baldosas[i].limpiado:
                out += "[-]"
            else:
                out += "[ ]"
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
            print("Dirección cambiada a: " + self.direccion)
            self.mover()

    def iniciar(self):
        while self.piso.limpiadas() < self.piso.size:
            limpiarConsola()
            self.mostrar()
            # limpiado = false --> sucio | limpiado = true --> limpio
            if self.piso.baldosas[self.posicion].limpiado is False:
                for j in range(2):
                    # sucio = 0 --> limpio
                    if self.piso.baldosas[self.posicion].sucio != 0:
                        print("Limpiando ..." + self.piso.baldosas[self.posicion].mostrar())
                        self.movimientos += 1
                        self.piso.baldosas[self.posicion].limpiar()
                    elif self.piso.baldosas[self.posicion].sucio == 0:
                        print("Baldosa ya limpia")
                        self.movimientos += 1
                        break
                print("Seteando a limpiado [" + str(self.posicion) + "]")
                self.piso.baldosas[self.posicion].limpiado = True
            elif self.piso.baldosas[self.posicion].limpiado is True:
                print("Ya fue limpiada, pasando a la siguiente")
                self.movimientos += 1
            self.mover()
            time.sleep(2)


if __name__ == '__main__':
    size = randint(1, 15)
    piso = Piso(size)
    aspiradora = Aspiradora(piso)
    aspiradora.iniciar()
    print("La aspiradora termino de limpiar")
    print("Movimientos realizados: " + str(aspiradora.movimientos))
    sys.exit()
