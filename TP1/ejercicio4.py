"""
Sensores: sensor de piso-pared, sensor de piso manchado
Actuadores: limpiar, avanzar, girar y detectar
Entorno: el piso
        -parcialmente observable (no ve el piso en tiempo real, y en el bloque donde esta parado no distingue el tipo de mancha)
        -agente individual (un sólo agente en el sistema)
        -estocastico (el estado va a estar determinado por lo que hizo el agente, por el estado anterior y otro elemento externo del entorno -> "generador de manchas")
        -secuencial (por el tipo de movimiento ya que la decision de hacia que lado moverse afectará las futuras deciciones y como estará el entorno)
        -estático (el entorno sólo cambia luego de una acción del agente, no mientras el agente delibera que decision tomar)
        -discreto (está formado por valores discretos como los tipos de suciedad, las direcciones y la cantidad de baldosas)
"""

import os, sys
from random import randint, choice
from time import sleep

random_movement = randint(1, 2)
block = randint(5, 10)


class Floor:
    def __init__(self, size, stage_list, stains_floor, position, move):
        self.size = size
        self.stage = stage_list
        self.stains_floor = stains_floor
        self.position = position
        self.move = move

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_stage_list(self):
        return self.stage

    def set_stage_list(self, stage_list):
        self.stage = stage_list

    def get_stains_floor(self):
        return self.stains_floor

    def set_stains_floor(self, stains_floor):
        self.stains_floor = stains_floor

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def move_left(self):
        self.position -= 1

    def move_right(self):
        self.position += 1

    def get_move(self):
        return self.move

    def set_move(self, move):
        self.move = move


class Funcion:

    @staticmethod
    def clean_floor():
        print('The floor is already clean')

    @staticmethod
    def stage(block):
        return [x for x in range(block)]

    @staticmethod
    def position_initial(block):
        return choice(block)

    @staticmethod
    def generate_floor(block):
        floor = []
        state = [' ', '+', 'x', '#']

        for i in range(block):
            floor.append(choice(state))
        return floor

    @staticmethod
    def show_main_information(size_floor, stage_list, stains_floor, position):
        print(f'Map size: {size_floor}')
        print(f'Floor number block: {stage_list}')
        print(f'Dirt: {stains_floor}')
        print(f'Initial block position: {position}')
        input('\nPress any key to start the vacuum cleaner work...')
        print()

    @staticmethod
    def check_the_floor(stains_floor, position):
        if stains_floor[position] == 'x':
            stains_floor[position] = '+'
        elif stains_floor[position] == '+':
            stains_floor[position] = ' '
        return stains_floor

    @staticmethod
    def auto_floor():
        ambient = Floor(
            block,
            Funcion.stage(block),
            Funcion.generate_floor(block),
            Funcion.position_initial(Funcion.stage(block)),
            random_movement
        )
        return ambient


def main():
    movement_counter = 0
    aspirated = 0
    ambient = Funcion.auto_floor()

    Funcion.show_main_information(
        ambient.get_size(),
        ambient.get_stage_list(),
        ambient.get_stains_floor(),
        ambient.get_position()
    )

    position_left = ambient.get_position()
    position_right = abs(ambient.get_stage_list()[-1] - ambient.get_position())

    if position_left < position_right:
        ambient.set_move(1)
    else:
        ambient.set_move(2)

    while True:

        try:

            new_stain_position = randint(0, ambient.get_size() - 1)

            floor_in_position = ambient.get_stains_floor()

            if not floor_in_position[new_stain_position] == '#' or floor_in_position[new_stain_position] == 'x':

                if floor_in_position[new_stain_position] == '+':
                    floor_in_position[new_stain_position] = 'x'

                elif floor_in_position[new_stain_position] == ' ':
                    floor_in_position[new_stain_position] = '+'

            os.system('clear')

            vacuum_cleaner_position = [' ' for _ in range(ambient.get_size())]
            vacuum_cleaner_position[ambient.get_position()] = "@"

            print(f'Press CTRL+C to stop pressing!')
            print(f'The vacuum cleaner is on the block: {ambient.get_position()}')
            print(f'Current state of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')

            if ambient.get_stains_floor()[ambient.get_position()] == 'x' or '+' or '#':

                if ambient.get_stains_floor()[ambient.get_position()] == '#':
                    aspirated += 2
                    print('Block cleaned')

                elif ambient.get_stains_floor()[ambient.get_position()] == 'x':
                    ambient.set_stains_floor(
                        Funcion.check_the_floor(ambient.get_stains_floor(), ambient.get_position()))
                    ambient.set_stains_floor(
                        Funcion.check_the_floor(ambient.get_stains_floor(), ambient.get_position()))
                    aspirated += 2
                    print('Block cleaned')

                elif ambient.get_stains_floor()[ambient.get_position()] == '+':
                    ambient.set_stains_floor(
                        Funcion.check_the_floor(ambient.get_stains_floor(), ambient.get_position()))
                    aspirated += 1
                    print('Block cleaned')

            if ambient.get_position() == ambient.get_stage_list()[0]:
                ambient.set_move(2)
            elif ambient.get_position() >= ambient.get_stage_list()[-1]:
                ambient.set_move(1)

            ambient.move_left() if ambient.get_move() == 1 else ambient.move_right()

            sleep(3)
            movement_counter += 1

        except KeyboardInterrupt:
            os.system('clear')
            print(f'Final position: Block {ambient.get_position()}')
            print(f'Number of movements: {movement_counter} | Number of clean actions: {str(aspirated)}')
            print(f'Final condition of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')

            sys.exit(0)


if __name__ == '__main__':
    main()