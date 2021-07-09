from flask import Flask
from flask.templating import render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi " + str(name) + "!"


@app.route("/repeat/<number>/<word>")
def repeat(word, number):
    str = ""
    num = int(number)
    for i in range(num):
        str += word
    return str

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
