"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def half_devision_predict(number: int = 50) -> int: 
    """ Функция укадывает число метобом половинного деления

    Args:
        number (int, optional): загаданное число. Defaults to 50.

    Returns:
        int: число попыток, потребоваашихся для отгадывания
    """    
    
    # Задаю границы интервала для поиска,
    # в дальнейшем будем делить его по пополам до результата
    pred_min = 1
    pred_max =  101

    count = 0
    while True:
        count += 1
        predict = (pred_min + pred_max) // 2 # Предположение
        if predict > number:
            pred_max = predict
        elif predict < number:
            pred_min = predict
        else:
            break
    return count

def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    values = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in values:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм {predict.__name__} угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(half_devision_predict)
