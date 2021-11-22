import cProfile
from random import randint

def main():
    students = list(range(1, 10))
    students_names = ["Панков", "Гайкин", "Демин", "Летов", "Иванов", "Иванов", "Иванов", "Маратов",
                      "Кузьмов", "Сапогов"]
    students_dict = {el: [students_names[index]] + [randint(2, 5) for i in range(4)] for index, el in
                     enumerate(students)}  # создаю словарь по условию
    print("Словарь:", students_dict)

    [print(val[0], sum(val[1:]) / 4, sep='\t') for val in
     students_dict.values()]  # оформленный вывод

cProfile.run("main(); " * 10000)
