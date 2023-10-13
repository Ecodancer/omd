import csv


team_hierarchy = {}  # хранилище данных для иерархии команд (п.1)
depart_dict = {}  # хранилище данных для отчета по департаментам (п.2)
file = 'Corp_Summary.csv'  # файл откуда берём данные
menu = '''
Чтобы вывести в понятном виде иерархию команд -> нажмите 1
Чтобы вывести сводный отчёт по департаментам ->  нажмите 2
Чтобы сохранить отчёт -> нажмите 3
'''  # меню, предлагаемое пользователю на входе (константа)


def preprocessing():
    '''
    Функция предобработки данных, т.к. юзер не заносит никаких данных, только
    просматривает их, то мы заранее обработаем данные.
    Кстати да, т.к. в моей программе ни одной функции не передаются параметры,
    то и аннотировать ничего не пришлось ;)
    '''
    with open(file, encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter=',')
        for row in file_reader:
            info = row[0].split(';')
            department, section, salary = info[1], info[2], info[5]
            if department == 'Департамент':  # скипаем, т.к. это 1-ая строка
                continue
            salary = int(salary)  # переводим зарплату в int
            if department not in depart_dict:
                depart_dict[department] = {'число сотрудников': 1,
                                           'макс. з/п': salary,
                                           'мин. з/п': salary,
                                           'сумма з/п': salary}
            else:
                depart_dict[department]['число сотрудников'] += 1
                depart_dict[department]['макс. з/п'] =\
                    max(salary, depart_dict[department]['макс. з/п'])
                depart_dict[department]['мин. з/п'] =\
                    min(salary, depart_dict[department]['мин. з/п'])
                depart_dict[department]['сумма з/п'] += salary
            if department not in team_hierarchy:
                team_hierarchy[department] = set([section])
            else:
                if section not in team_hierarchy[department]:
                    team_hierarchy[department].add(section)


def tap_one():
    '''
    Выводит иерархию команд. Теперь более красиво :)
    '''
    for department in team_hierarchy:
        print(f'Департамент: {department}')
        print('Входящие в него команды:', end=' ')
        print(*team_hierarchy[department], sep=', ')
        print('=' * 40)


def tap_two():
    '''
    Выводит сводный отчет по департаментам.
    '''
    for depart in depart_dict:
        print('=' * 40)
        print(f'Название -> {depart}')
        print(f'Численность -> {depart_dict[depart]["число сотрудников"]}')
        print(f'''Вилка зарплат -> {depart_dict[depart]['мин. з/п']} - мин.
                 {depart_dict[depart]['макс. з/п']} - макс.''')
        print(f'''Сред. з/п -> {round(depart_dict[depart]["сумма з/п"] /
                  depart_dict[depart]["число сотрудников"], 2)}''')


def tap_three():
    '''
    Сохраняет отчет по департаментам из п.2 в файл "save_docs.csv"
    *появляется в той же папке из которой запускается программа.
    '''
    with open('save_docs.csv', mode='w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=',', lineterminator='\r')
        file_writer.writerow(['Название', 'Численность', 'Вилка', 'Сред. з/п'])
        for depart in depart_dict:
            file_writer.writerow(
                [depart,
                 depart_dict[depart],
                 f'''{depart_dict[depart]['мин. з/п']} - мин.
                 {depart_dict[depart]['макс. з/п']} - макс.''',
                 round(depart_dict[depart]['сумма з/п'] /
                       depart_dict[depart]['число сотрудников'], 2)]
                )


def start():
    '''
    Функция - оболочка модуля, что-то аля main в С
    '''
    preprocessing()
    print(menu)
    vvod = input('Пожалуйста, введите цифру 1/2/3: ')
    while vvod not in ('1', '2', '3'):
        vvod = input('Вы можете ввести только цифру 1/2/3: ')
    if vvod == '1':
        tap_one()
    elif vvod == '2':
        tap_two()
    else:
        tap_three()


if __name__ == '__main__':
    start()
