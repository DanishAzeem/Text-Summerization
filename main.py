from flask import Flask, redirect, url_for, render_template, request, flash
from text_summary import summarizer

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('App.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        if  request.form['rawtext'] == '':             
            text = 'null'
        else:
            text = request.form['rawtext']
        Sum_ratio = request.form['Sum_ratio']
        keywords = summarizer(text, Sum_ratio)

    return render_template('App.html', keywords = keywords, rawtext = text)


# @app.route('/puppy/<name>')
# def puppy(name):
#     # return "<h1>This is page for {}</h1>".format(name)
#     return "<h1>Upper case: {}</h1>".format(name.upper())
if __name__ == '__main__':
    app.run()

