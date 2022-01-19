from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello World"

@app.route('/cookie/set')
def set_cookie():
  resp = make_response(render_template("index.html"))
  resp.set_cookie("username", "Fran")
  
  return resp


@app.route('/cookie/read')
def read_cookie():
  username = request.cookies.get("username", None) #recupero valor d ela cookie
  
  if username == None:
    return "La cookie no existe"
  
  return username

if __name__ == "__main__":
  app.run(debug=True)