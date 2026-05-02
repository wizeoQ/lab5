import numpy as np
from typing import Union, Callable, List, Optional
    

def ex(exercise_number: Union[str, int, float]) -> None:
    """
    Выводит в консоль упражнение с указанным в аргументе номером.
    """
    print("==========")
    print("Задание ", exercise_number)


def eq(equal_quantity: int=5) -> None:
    """
    Выводит в консоль знак "=" в количестве, указанном в аргументе.
    """
    print("=" * equal_quantity)


def d(dash_quantity: int=5) -> None:
    """
    Выводит в консоль знак "-" в количестве, указанном в аргументе.
    """
    print("-" * dash_quantity)


def n() -> None:
    """
    Выводит в консоль:༺•༻
    """
    print("༺•༻")


def l(line: int=5) -> None:
    """
    Выводит в консоль знак "─" в количестве, указанном в аргументе.
    """
    print("─" * line)


def ln() -> None:
    """
    Выводит в консоль ───────✧───────
    """
    print("───────✧───────")
    


def yes_or_not(function_yes: Callable[[], None]=lambda: None,
               function_not: Callable[[], None]=lambda: None
               ) -> None:
    """
    Выводит выбор между двумя функциями (y/n) в консоль
    
    yes_or_not(Func_yes, Func_not)
    В случае ввода "Y"(или y, д, Д, 1) (Yes):
        выполняется функция из первого аргумента.
    В случае ввода "N"(или n, н, Н, 0) (No):
        выполняется функция из второго аргумента.
    По умолчанию в обоих случаях функции ничего не делают.
    """
    print("(y/n)", end="")
    while True:
        out_flag = input("> ")
        if out_flag in "yY1дД" and out_flag != "":
            function_yes()
            break
        elif out_flag in "nN0нН" and out_flag != "":
            function_not()
            break
        else:
            print("(y/n)", end="")


def simple_complex(x: Union[int, float, complex],
                   round_digitals: int=3,
                   is_print: bool=False,
                   is_i: bool=True,
                   is_return: bool=True
                   ) -> Optional[str]:
    """
    Преобразует комплексное число в удобно-читаемую строку.
    
    В случае nan и inf выводит соответствующее сообщение.
    x - комплексное число
    round_digitals - число знаков для округления
    is_print - выводить ли строку в консоль
    is_i - обозначение мнимой единицы:
        True - Математическая - "i"
        False - Инженерная - "j"
    is_return - возвращать ли строку в result
    """
    rnd = int(round_digitals)
    if is_i: unit = "i"
    if not is_i: unit = "j"
    if np.isnan(x): x_ir, x_ii = "nan","" # случай nan
    elif np.isinf(x): x_ir, x_ii = "inf","" # случай inf
    else:
        x_ir = round(float(np.real(x)), rnd)
        x_ii = round(float(np.imag(x)), rnd)
        if float(x_ir) == int(x_ir): x_ir = int(x_ir)
        if float(x_ii) == int(x_ii): x_ii = int(x_ii)
        if x_ir == 0 and x_ii != 0: x_ir = "" # число не вещественное
        if x_ii == 0: x_ii = "" # число не мнимое
        elif x_ii > 0 and x_ir != "": x_ii = " + " + str(x_ii) + unit
        elif x_ii > 0 and x_ir == "": x_ii = str(x_ii) + unit
        elif x_ii < 0 and x_ir != "": x_ii = " - " + str(abs(x_ii)) + unit
        elif x_ii < 0 and x_ir == "": x_ii = str(x_ii) + unit
    result = str(x_ir) + str(x_ii)
    if is_print: print(result)
    if is_return: return result


def multi_input(allow_linspace: bool=True) -> List[float]:
    """
    Просит у пользователя ввести число, массив или диапазон.
    
    Даёт возможность определить в консоли переменную как значение, 
    массив (через запятую) или диапазон (с началом, концом
    и количеством элементов).
    Чтобы отключить возможность ввода диапазона, нужно
    ввести аргумент 0.
    """    
    # Ввод данных
    print("Для ввода массива используйте запятые.", sep="")
    if allow_linspace:
        print("Для ввода диапазона введите d.", end="")
    x=input("> ")
    # Ввод диапазона
    if x != 'd' or not allow_linspace:
        try:
            x = list(map(float, (x.split(','))))
        except ValueError:
            print("Неверный тип данных.", end = "")
            while True:
                try:
                    x = input('> ')
                    if x == 'd' and allow_linspace: break
                    x = list(map(float, x.split(',')))
                    break
                except ValueError: 
                    print("Неверный тип данных.", end="")
        points = 1
    # Ввод t
    if x == 'd' and allow_linspace:
        l()
        print("Введите начало диапазона", end="")
        while True:
            try:
                start = float(input("> "))
                break
            except ValueError: print("Неверный тип данных.", end="")
        l()
        print("Введите конец диапазона", end="")
        while True:
            try:
                end = float(input("> "))
                break
            except ValueError: print("Неверный тип данных.", end="")
        l()
        print("Введите количество элементов", end="")
        while True:
            try:
                points = int(input("> "))
                x = np.linspace(start, end, points)
                x = list(map(float, x))
                break
            except (ValueError, TypeError):
                print("Неверный тип данных" ,end="")
                print(" или отрицательное значение.", end="")
    # Крайние случаи
    if points == 0:
        print("Значения отсутствуют.")
        x = []
    return x


def defend_input(complex_allow: bool=False,
                 nan_inf_allow: bool=False
                 ) -> Union[float, complex]:
    """
    Ввод float или complex с защитой от ValueError
    
    return(float)
    complex_allow позволяет работать с комплексными числами.
    nan_inf_allow позволяет работать с nan и inf.
    """
    while True:
        try:
            if complex_allow: x = complex(input("> "))
            if not complex_allow: x = float(input("> "))
            if not nan_inf_allow and np.isnan(x): raise ValueError
            if not nan_inf_allow and np.isinf(x): raise ValueError
            return x
        except ValueError:
            print("Неверный тип данных.", end="")


def greek_alphabet() -> None:
    """
    Выводит в консоль греческий алфавит,знак корня и
    знак умножения для копипаста.
    """
    print("Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ")
    print("Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω")
    print("α β γ δ ε ζ η θ ι κ λ μ")
    print("ν ξ ο π ρ σ τ υ φ χ ψ ω")
    print("√ ⋅")


def character_range(start: str, end: str) -> str:
    """
    Выводит алфавит символов.
    
    Возвращает строку из всех символов, которые находятся
    внутри unicode в промежутке от стартового символа
    до конечного символа.
    """
    alphabet = "".join(map(chr, range(ord(start), ord(end) + 1)))
    return alphabet


def alphabet(language: str="ru+eng") -> str:
    """
    Возвращает весь алфавит одной строкой.
    
    На выбор 3 алфавита:
        "ru" - русский алфавит
        "eng" - английский алфавит
        "ru+eng" - русский и английский алфавит
    """
    result = ""
    if language == "ru":
        ru_lowercase = list(character_range("а", "я"))
        ru_lowercase.insert(6, "ё")
        ru_uppercase = list(character_range("А", "Я"))
        ru_uppercase.insert(6, "Ё")
        result = "".join(ru_lowercase + ru_uppercase)
    elif language == "eng":
        eng_lowercase = list(character_range("a", "z"))
        eng_uppercase = list(character_range("A", "Z"))
        result = "".join(eng_lowercase + eng_uppercase)
    elif language == "ru+eng":
        result = alphabet("ru") + alphabet("eng")
    return result
