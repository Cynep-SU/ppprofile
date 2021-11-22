import cProfile
import pstats
cProfile.run("""
def main():
    y = int(input("Введите количество строк\\n"))
    if 50 < y or y < 12:
        print("При таких значениях я не могу работать нормально")
        raise ValueError
    x = y * 2
    Even = True
    if y % 2 == 1:
        Even = False
    if (x // 6) % 2 == 1:
        x += 1
    center = y // 2 - 1
    has_text = (x * 11 // 18) >= 22
    texts = ["CODE THE WORLD", "www.itmathrepetitor.ru"]
    template_str = "[" * ((x * 5) // 12 + (1 if Even else 0)) + " " * (x // 12)
    template_str_small = "[" + template_str[1:x // 4 - 2].replace("[", ":") + "["  #
    template_str_small += " " * (len(template_str) - len(template_str_small))
    print(template_str + "".join(reversed(template_str)).replace("[", "]"))
    for line in range(1, y - 1):
        if line < y // 6 or line > y - 1 - y // 6:
            string = "[" + template_str[1:].replace("[", ":")
        elif line == y // 6 or line == y - 1 - y // 6:
            template_str_copy = list(template_str)
            template_str_copy[template_str.rfind("[")] = ":"
            template_str_copy = "".join(template_str_copy)
            string = "[" + template_str[1: x // 4 - 1].replace("[", ":") + template_str_copy[
                                                                           x // 4 - 1:]
        else:
            if line == center and has_text:
                string = template_str_small[:(len(template_str_small) - len(texts[0]) // 2)]
                print(string + texts[0] + "".join(reversed(string)).replace("[", "]"))
                continue
            elif line == center + 1 and has_text:
                string = template_str_small[:(len(template_str_small) - len(texts[1]) // 2)]
                print(string + texts[1] + "".join(reversed(string)).replace("[", "]"))
                continue
            else:
                string = template_str_small
        print(string + "".join(reversed(string)).replace("[", "]"))
    print(template_str + "".join(reversed(template_str)).replace("[", "]"))


if __name__ == '__main__':
    cycle_do = True
    while cycle_do:
        try:
            main()
            cycle_do = False
            input()
        except ValueError:
            import os
            import time

            for i in range(12):
                os.system('cls' if os.name == 'nt' else 'clear')
                print("ОШИБКА!!! НАЧИНАЮ ПЕРЕЗАГРУЗКУ" + "." * (i % 3 + 1))
                time.sleep(0.2)
            os.system('cls' if os.name == 'nt' else 'clear')
            """, "Logs")
stats = pstats.Stats("Logs")
stats.strip_dirs()
stats.sort_stats("time")
stats.print_stats(5)
