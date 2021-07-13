from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "lol im a secret key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name=request.form['name'], location=request.form['location'], language=request.form['language'], comment=request.form['comment'])

@app.route('/return', methods=['POST'])
def comeback():
    
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
