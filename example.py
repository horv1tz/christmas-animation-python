# Обязательный импорт
from tree import ChristmasTree 

# Создание "дерева"
tree = ChristmasTree()

# Установка максимально ширишы хвои
tree.set_max_width_needles(7)

# Установка максимально ширишы ствола
tree.set_max_width_trunk(3)

# Отдельная отрисовка хвои
tree.print_needles()

# Отдельная отрисовка ствола
tree.print_trunk()

# Отрисовка всей ёлки
tree.print_crismass_tree()