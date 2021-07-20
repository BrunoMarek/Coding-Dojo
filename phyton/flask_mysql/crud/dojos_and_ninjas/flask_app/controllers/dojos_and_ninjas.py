import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninjas


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_dojos()
    return render_template('dojos.html', dojos = dojos)


@app.route('/dojos/new', methods=['POST'])
def new_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojos_id>')
def dojo_show(dojos_id):
    data = {
        'id': dojos_id
    }
    dojo = Dojo.get_dojosid(data)
    

    return render_template('dojo_show.html', dojo= dojo)


@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_dojos()
    return render_template('new_ninja.html', dojos=dojos)


@app.route('/ninjas/create', methods = ['POST'])
def create_ninja():
    ninja = Ninjas.create_ninja(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{dojo_id}')

