from flask import Flask, url_for
from flask import render_template
from flask import request
import csv

# virtualenv env # создание вирт. окружение
# source env/bin/activate
# pip install Flask

app = Flask(__name__)


@app.route('/')
def index():
	rules = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

	return render_template('index.html', appname=__name__, content=rules)

def command(id):
	return f'running command with {id}'

app.add_url_rule('/command/<id>', 'command', command)


@app.route('/add/message', methods=['POST'])
def add_message():
	f = 'database.csv'
	with open(f, 'w') as csvfile:
        fieldnames = ['№ of process', 'RANDOM VALUE']
        csv_writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
        csv_writer.writerow(fieldnames)
	with open(f, 'a') as csvfile:
        csv_writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
        for i in range(n_iter):
            n = random.randint(a, b)
            csv_writer.writerow([request.form['username'], request.form['msgtxt']])
	return 'adding message'


if __name__ == '__main__':
    app.run()
