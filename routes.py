from app import app
from flask import render_template, request
from vunctions import *


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        fio = request.form['user']
        # print(fio)
        if get_students_fio_tasks()[fio] == -1:
            task = give_id_task(fio)
        else:
            task = get_tasks()[get_students_fio_tasks()[fio]]
        # print(task)
        return render_template('index.html', users=get_students(), task=task)
    # print(get_students())
    return render_template('index.html', users=get_students())

