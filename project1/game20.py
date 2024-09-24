import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его, используя бинарный поиск.
       Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # подсчет количества попыток угадывания
    predict = np.random.randint(1, 101) # предсказание искомого числа
    min = 0 # минимальная граница
    max = 101 # максимальная граница

    while number != predict:
        count += 1
        
        if number > predict:
            min = predict # определение новой мин границы поиска искомого числа
        elif number < predict:
            max = predict # определение новой макс границы поиска искомого числа
        predict = (min+max) // 2 # формула для определения следующего предсказываемого числа

    return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов наш алгоритм угадывает искомое число 

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
