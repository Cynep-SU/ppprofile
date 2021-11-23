import cProfile
from typing import List


# функция, генерирующая матрицу со случайными значениями с заданными
# строчками и столбцами
def create_list(col: int, row: int) -> List[List[int]]:
    return [[7 for g in range(row)] for i in range(col)]


def main():
    # Генерируем с помощью функций несколько матриц с миллионом элементов
    create_list(100000, 10)
    create_list(1000, 1000)
    create_list(10, 100000)


cProfile.run("main()")
