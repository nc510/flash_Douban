from flask import Flask  # 载入模块
# 使用pip install flask安装Flask包

from flask import render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    # return 'hello world!'
    return render_template('index.html')


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template('movie.html', movies=datalist)


@app.route('/score')
def score():
    return render_template('score.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/word')
def word():
    return render_template('word.html')


if __name__ == '__main__':
    app.run()
