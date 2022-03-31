
names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(names: list, birthday_years: list, genders: list):
    # для начала сведём информацию в один список
    list_of_students = []
    for i in range(len(names)):
        list_of_students.append((names[i], birthday_years[i], genders[i]))
    # теперь проходим по списку и сортируем - призывник или нет
    list_of_inductees = []
    list_of_unknown = []
    for student in list_of_students:
        if None not in student:
            if student[2] == 'Male' and 18 <= 2021 - student[1] <= 30:
                list_of_inductees.append(student[0])
        else:
            list_of_unknown.append(student[0])
    # вывводим два полученных списка
    return f'призывники - {list_of_inductees},\n' \
           f'неизвестно - {list_of_unknown}'


print(get_inductees(names, birthday_years, genders))
