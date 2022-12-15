import csv
import random


def get_students():
    with open('students.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return [rw for rw in reader]


def get_students_fio_tasks():
    with open('students.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return {rw['fio']: int(rw['tasks']) for rw in reader}


def get_tasks():
    with open('tasks.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return {int(rw['tsk_id']): rw['task'] for rw in reader}


def get_free_tasks():
    return list(set(get_tasks().keys()) - set(map(lambda x: x[1], get_students_fio_tasks().items())))


def give_id_task(fio):
    students = get_students()
    free_tasks = get_free_tasks()
    if free_tasks == []:
        return 'No free tasks'

    with open('students.csv', 'wt', encoding='utf-8') as csv_file:
        fieldnames = ['fio', 'tasks']
        writer = csv.DictWriter(csv_file, fieldnames, lineterminator="\r")
        writer.writeheader()

        id_st = students.index({'fio': fio, 'tasks': '-1'})
        id_task = random.choice(free_tasks)
        students[id_st]['tasks'] = id_task

        for i in students:
            writer.writerow(i)

        return get_tasks()[id_task]
