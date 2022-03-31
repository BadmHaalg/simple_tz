'''
Схема была проста: есть абитуриент, у него есть результаты сданных экзаменов по математике,
русскому и информатике. Соответственно, у каждого потенциального студента есть сумма баллов
по этим экзаменам. Также есть дополнительные (extra_scores) баллы: за волонтерство, участие
 в олимпиадах и другие активности.

Вам нужно отобрать 20 человек, у которых суммарный балл выше, чем у других. В случае, если не
получается однозначно определить 20 человек (например, 2 человека набрали одинаковое СУММАРНОЕ
количество баллов и претендуют на 20 место в списке, стоит их ранжировать по "профильным"
дисциплинам - "информатике" и "математике").

Напишите функцию find_top_20 *
Функция принимает на вход список сводной информации по абитуриентам (candidates) и возвращает
список с именами 20 человек, набравших наибольшее СУММАРНОЕ количество баллов (с учетом extra баллов),
 которые станут студентами университета. Пример входных данных приведен ниже.
'''

candidates = [
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 86, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 73, "computer_science": 34}, "extra_scores": 1},
    {"name": "Slava", "scores": {"math": 90, "russian_language": 86, "computer_science": 76}, "extra_scores": 1},
    {"name": "Anna", "scores": {"math": 89, "russian_language": 34, "computer_science": 36}, "extra_scores": 1},
    {"name": "Vika", "scores": {"math": 54, "russian_language": 90, "computer_science": 86}, "extra_scores": 1},
    {"name": "Ira", "scores": {"math": 100, "russian_language": 64, "computer_science": 90}, "extra_scores": 1},
    {"name": "Yarik", "scores": {"math": 100, "russian_language": 64, "computer_science": 93}, "extra_scores": 1},
    {"name": "Roma", "scores": {"math": 76, "russian_language": 74, "computer_science": 83}, "extra_scores": 1},
    {"name": "Vova", "scores": {"math": 56, "russian_language": 65, "computer_science": 75}, "extra_scores": 1},
    {"name": "John", "scores": {"math": 23, "russian_language": 33, "computer_science": 63}, "extra_scores": 1},
    {"name": "Khisshov", "scores": {"math": 11, "russian_language": 100, "computer_science": 12}, "extra_scores": 1},
    {"name": "Agent J", "scores": {"math": 99, "russian_language": 99, "computer_science": 63}, "extra_scores": 1},
    {"name": "Ira", "scores": {"math": 64, "russian_language": 87, "computer_science": 62}, "extra_scores": 1},
    {"name": "Roma", "scores": {"math": 65, "russian_language": 65, "computer_science": 63}, "extra_scores": 1},
    {"name": "Vova", "scores": {"math": 64, "russian_language": 87, "computer_science": 63}, "extra_scores": 1},
    {"name": "John", "scores": {"math": 75, "russian_language": 100, "computer_science": 40}, "extra_scores": 1},
    {"name": "Khisshov", "scores": {"math": 76, "russian_language": 86, "computer_science": 34}, "extra_scores": 1},
    {"name": "Agent B", "scores": {"math": 87, "russian_language": 25, "computer_science": 47}, "extra_scores": 1},
    {"name": "Ira", "scores": {"math": 74, "russian_language": 48, "computer_science": 67}, "extra_scores": 1},
    {"name": "Roma", "scores": {"math": 90, "russian_language": 85, "computer_science": 64}, "extra_scores": 1},
    {"name": "Vova", "scores": {"math": 74, "russian_language": 73, "computer_science": 21}, "extra_scores": 1},
    {"name": "John", "scores": {"math": 55, "russian_language": 44, "computer_science": 52}, "extra_scores": 1},
    {"name": "Khisshov", "scores": {"math": 55, "russian_language": 44, "computer_science": 52}, "extra_scores": 1},
    {"name": "Agent J", "scores": {"math": 77, "russian_language": 88, "computer_science": 52}, "extra_scores": 1},
]


def find_top_20(candidates_list):
    candidates_sum = []
    for candidate in candidates_list:
        # создадим список кортежей со сводной
        # информацией: имя, сумма баллов, сумма балов по профильным предметам
        name = candidate['name']
        sum_score = candidate['scores']['math'] + candidate['scores']['russian_language'] + \
                    candidate['scores']['computer_science'] + candidate['extra_scores']
        profile = candidate['scores']['math'] + candidate['scores']['computer_science']
        candidates_sum.append((name, sum_score, profile))
    # отсортируем список по двум условиям задания
    candidates_sum = sorted(candidates_sum, key=lambda x: (-x[1], -x[2]))
    # нам нужен только список имен студентов
    list_of_winner = []
    for candidate in candidates_sum:
        list_of_winner.append(candidate[0])
    # выведем список 20-ти счастливчиков
    return list_of_winner[:20]


print(len(find_top_20(candidates)))
print(find_top_20(candidates))