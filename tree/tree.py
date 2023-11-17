from colorama import init as crinit
crinit()

from colorama import Fore, Style
from random import randrange

class ChristmasTree():
    def __init__(self):
        # Дефолтное значение для ширины хвои
        self.__max_width_needles = 7
        # Дефолтное значение для ширины ствола
        self.__max_width_trunk = 3
        # Дефолтное значение для высоты хвои (количество слоёв)
        self.__max_height_needles = 1
        # Дефолтное значение для высоты ствола
        self.__max_height_trunk = 2

    # Изменение максимальной ширины хвои
    def set_max_width_needles(self, width: int):
        if (width > 0) and (width % 2 == 1):
            self.__max_width_needles = width
        else:
            print(Fore.RED + "Ошибка!", Style.RESET_ALL)

    # Изменение максимальной ширины ствола
    def set_max_width_trunk(self, width: int):
        if (width > 0) and (width % 2 == 1):
            self.__max_width_trunk = width
        else:
            print(Fore.RED + "Ошибка!", Style.RESET_ALL)

    # Изменение максимальной высоты хвои
    def set_max_height_needles(self, height: int):
        if (height > 0):
            self.__max_height_needles = height
        else:
            print(Fore.RED + "Ошибка!", Style.RESET_ALL)

    # Изменение максимальной высоты ствола
    def set_max_height_trunk(self, height: int):
        if (height > 0):
            self.__max_height_trunk = height
        else:
            print(Fore.RED + "Ошибка!", Style.RESET_ALL)

    # Отрисовка хвои
    def print_needles(self):
        for i in range(1, self.__max_width_needles+2, 2):
            space = int((self.__max_width_needles - i) / 2 )
            if space > 0: 
                for x in range(self.__max_height_needles):
                    print(Fore.GREEN + ' ' * space + '*' * i,  Style.RESET_ALL) 
            else:
                print(Fore.GREEN + '*' * i, Style.RESET_ALL)

    # Отрисовка ствола
    def print_trunk(self):
         for i in range(self.__max_height_trunk):
            space = int((self.__max_width_needles - self.__max_width_trunk) / 2 )
            print(Fore.YELLOW + ' ' * space + '*' * self.__max_width_trunk,  Style.RESET_ALL)
    
    # Отрисовка всей ёлки
    def print_christmas_tree(self):
        self.print_needles()
        self.print_trunk()
