import csv

with open('students.csv', mode="w", encoding='utf-8') as csv_file:
    fieldnames = ['fio', 'tasks']
    writer = csv.DictWriter(csv_file, fieldnames, lineterminator="\r")
    writer.writeheader()

    for i in (
            {'fio': 'Горелкин Андрей Владимирович', 'tasks': -1},
            {'fio': 'Царева Анастасия Валерьевна', 'tasks': -1},
            {'fio': 'Леонова Мирина Батьковна', 'tasks': -1},
            {'fio': 'Канеки Ван Гогович', 'tasks': -1},
    ):
        writer.writerow(i)

with open('tasks.csv', mode="w", encoding='utf-8') as csv_file:
    fieldnames = ['tsk_id', 'task']
    writer = csv.DictWriter(csv_file, fieldnames, lineterminator="\r")
    writer.writeheader()
    for i in range(1, 11):
        writer.writerow({'tsk_id': i, 'task': f'Задание {i}'})
