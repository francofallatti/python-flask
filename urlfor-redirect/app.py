from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return "holis"

@app.route('/start')
def start():
  
  return url_for("index", next="login")

@app.route('/google')
def to_google():
  return redirect("https://www.google.com")

#las 2 funciones en conjunto
@app.route('/post/<int:id>')
def post(id):
  return "post: {}".format(id)

@app.route('/today')
def today():
  return redirect(url_for("post", id=50, next= "edit"))

if __name__ == "__main__":
  app.run(debug=True)