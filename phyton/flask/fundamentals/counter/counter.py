# from flask import Flask, render_template, request, redirect, session


# app = Flask(__name__)
# app.secret_key = "lol im a secret key"

# app.route('/')
# def index ():
    # if 'number_of_times' in session:
    #     session['number_of_times'] += 1

#     return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug = True)




from flask import Flask, render_template, request, redirect, session  
app = Flask(__name__) 
app.secret_key = "lol im a secret key"



@app.route('/')         
def number_of_times():
    if 'number_of_times' in session:
        session['number_of_times'] += 1
    elif not 'number_of_times' in session:
        session['number_of_times'] = 0
    return render_template('index.html') 

@app.route('/count', methods = ['POST'])
def count():
    if request.form['btn'] == '2x':
        session['number_of_times'] += 1
    elif request.form['btn'] == 'reset':
        session['number_of_times'] = 0
    
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":        
    app.run(debug=True)

