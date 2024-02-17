import csv

import numpy as np
from flask import Flask, render_template

rng = np.random.default_rng()

with open("static/million.csv") as f:
    reader = csv.reader(f)
    songlist = [row[1] for row in reader]

app = Flask(__name__)
data = {"len":1200,"song":"test" }

# @app.route("/index", methods=['GET', 'POST'])
def index_get():
    num = rng.integers(0,len(songlist)-1)
    print(songlist[num])
    return render_template("index.html",song= f"{num}", songname = songlist[num],len=1200) # templatesフォルダ内のindex.htmlを表示する

def index_post():
    num = rng.integers(0,len(songlist)-1)
    return render_template("index.html",song= f"{num}",songname = songlist[num],len=1200) # templatesフォルダ内のindex.htmlを表示する


if __name__ == "__main__":
    app.add_url_rule("/index",view_func=index_post,methods=["POST"])
    app.add_url_rule("/index",view_func=index_get,methods=["GET"])
    app.run()