from colorama import init as crinit
crinit()

from colorama import Fore, Style

class ChristmasTree():
    def __init__(self):
        # Дефолтное значение для ширины хвои
        self.__max_width_needles = 7
        # Дефолтное значение для ширины ствола
        self.__max_width_trunk = 3

    def set_max_width_needles(self, width: int):
        if (width > 0) and (width % 2 == 1):
            self.__max_width_needles = width
        else:
            print(Fore.RED + "Ошибка!", Style.RESET_ALL)

    def set_max_width_trunk(self, width: int):
        if (width > 0) and (width % 2 == 1):
            self.__set_max_width_trunk = width
        else:
            print(Fore.RED + "Ошибка!", Style.RESET_ALL)

    def print_needles(self):
        for i in range(1, self.__max_width_needles+2, 2):
            space = int((self.__max_width_needles - i) / 2 )
            if space > 0: 
                print(Fore.GREEN + ' ' * space + '*' * i,  Style.RESET_ALL)
            else:
                print(Fore.GREEN + '*' * i, Style.RESET_ALL)

    def print_trunk(self):
         for i in range(1, 3):
            space = int((self.__max_width_needles - self.__max_width_trunk) / 2 )
            print(Fore.YELLOW + ' ' * space + '*' * self.__max_width_trunk,  Style.RESET_ALL)
    
    def print_crismass_tree(self):
        self.print_needles()
        self.print_trunk()