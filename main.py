from flask import Flask, render_template, url_for
import sqlite3 as sq

app = Flask(__name__)


@app.route('/home/')
@app.route('/')
def home():
    with sq.connect('zodiac.db') as connection:
        cur = connection.cursor()
        cur.execute("""SELECT eng_name, rus_name, date_zodiac, mini_info FROM zodiacs""")
        menu = cur.fetchall()
    return render_template('home.html', title='Home', menu=menu)


@app.route('/home/<name>')
def info_page(name):
    with sq.connect('zodiac.db') as connection:
        cur = connection.cursor()
        cur.execute("""SELECT eng_name, rus_name, date_zodiac, temperament, jobs 
        FROM zodiacs
        WHERE '{}' == eng_name
        """.format(name))
        arr = cur.fetchall()
    if len(arr) == 0:
        return '<h1>Страница не найдена</h1>'
    else:
        return render_template('infopage.html', arr=arr[0], title=arr[0][0])


if __name__ == "__main__":
    app.run(debug=False)
