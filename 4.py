
students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}


def make_report_about_top3(student_scores: dict):
    scores_list = []
    # создаем список кортежей
    for name, score in student_scores.items():
        scores_list.append((name, score))
    # сортируем по убыванию среднего балла
    scores_list.sort(key=lambda x: -x[1])
    # работаем с excel
    import xlsxwriter, os
    workbook = xlsxwriter.Workbook('for_olga_petrovna_with_love.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Имя')
    worksheet.write('B1', 'Рейтинг')
    # проходи по первым трем записям списка и записываем их в excel-файл
    for i, el in enumerate(scores_list[:3], start=2):
        worksheet.write(f'A{i}', el[0])
        worksheet.write(f'B{i}', el[1])
    workbook.close()
    # получаем путь к созданому файлу
    path = os.path.abspath('for_olga_petrovna_with_love.xlsx')

    return path


print(make_report_about_top3(students_avg_scores))
