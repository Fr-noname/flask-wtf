from flask import render_template, Flask, url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
