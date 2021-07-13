from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "lol im a secret key"


@app.route('/')
def number():
    if 'number' not in session:
        session['number'] = random.randint(1, 101)
    return render_template('index.html')


@app.route('/game', methods=['POST'])
def game():
    if int(request.form['numberx']) == session['number']:
        session['result'] = 'You got it'
    elif int(request.form['numberx']) > session['number']:
        session['result'] = 'Too high'
    else:
        session['result'] = "Too low"
    
    return redirect('/')

@app.route('/playagain')
def play_Again():
    session.pop('number')
    session.pop('result')
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)
