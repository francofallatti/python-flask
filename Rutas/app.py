from flask import Flask

app = Flask(__name__)

##https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing

@app.route('/')
def index():
  return "Hellow World!"

@app.route('/hola')
def hola():
  return "Hola!"

@app.route('/user/<string:user>')
def user(user):
  return "Hola " + user

@app.route('/numero/<int:num>')
def numero(num):
  return "Numero: {}".format(num)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
  return "ID: {id}, nombre de usuario: {username}"  

@app.route('/suma/<float:n1>/<float:n2>')
def sumar(n1, n2):
  return "La suma es: {}".format(n1 + n2)

@app.route('/default/')
@app.route('/default/<string:dft>')
def dft(dft="Holaa"):
  return "dft es: " + dft

if __name__ == "__main__":
  app.run(debug=True)