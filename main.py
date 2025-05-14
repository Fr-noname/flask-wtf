import os

from flask import render_template, Flask, url_for, redirect, request
from classes import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'


@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        type_prof = "Научные симуляторы"
        image_dir = url_for('static', filename='img/train.PNG')
    else:
        type_prof = "Внешние Насосы :D"
        image_dir = url_for('static', filename='img/train1.PNG')

    return render_template("training.html", title=type_prof, type_prof=type_prof,
                           image_dir=image_dir)


@app.route('/list_prof/<type_prof>')
def list_profs(type_prof):
    list_prof = ["Ведьмак", "Раб_1", "Раб_2", "Раб_3", "Рабовладелец", "Чернорабочий",
                 "Шахтер", "Повар", "Собиратель", "Воин", "Едаделатель", "Приготовитель"]
    return render_template("list_prof.html", list_prof=list_prof, types=type_prof)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    return render_template("answer.html", title="Анкета", person={'surname': 'QW', 'name': 'bob',
                                                                  'education': 'high',
                                                                  'profession': 'inhere', 'sex': 'male',
                                                                  'motivation': 'Want',
                                                                  'ready': 'True'},
                           css=url_for('static', filename='css/answer_style.css'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('login.html', title='Авторизация', form=form,
                           css=url_for('static', filename='css/aut_style.css'),
                           img=url_for('static', filename='img/photo.png'))


@app.route('/distribution')
def distribution():
    user_list = ["Акакий", "Ясос Б.", "Яна Ц.", "Даздраперма", "Персострат"]
    return render_template('distribution.html', title='Расселение', user_list=user_list)


@app.route('/table/<sex>/<int:year>')
def table(sex, year):
    if sex == "male" and int(year) <= 21:
        img2 = "male.png"
        img = "голубой.png"
    elif sex == "male" and int(year) > 21:
        img2 = "male.png"
        img = "синий.png"
    elif sex == "female" and int(year) <= 21:
        img2 = "female.png"
        img = "бледнорозовый.png"
    else:
        img2 = "female.png"
        img = "розовый.png"
    return render_template('table.html', title='Дизайн', css=url_for("static", filename="css/table.css"),
                           img=url_for("static", filename=f"img/{img}"),
                           img2=url_for("static", filename=f"img/{img2}"))


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"static/img/cash/{len(os.listdir('static/img/shlack'))}.png")
    return render_template('galery.html', title='Дизайн',
                           imgs=[url_for("static", filename=f"img/shlack/{file}")
                                 for file in os.listdir('static/img/shlack')])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
