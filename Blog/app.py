from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

import os

##"sqlite:///C:\\Users\\fran\\Desktop\\Code\\Python Flask\\Blog\\blog.db"
dbdir= "sqlite:///" + os.path.abspath(os.getcwd())+ "\\blog.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##defino modelo de tabla
class Post(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime, default=datetime.now)
	texto = db.Column(db.String, nullable=False)

@app.route("/")
def inicio():
	posts = Post.query.order_by(Post.fecha.desc()).all() 
	return render_template("inicio.html", posts=posts)


@app.route('/agregar')
def agregar():
  return render_template('agregar.html')

@app.route('/crear', methods=["POST"])
def crear_post():
  titulo = request.form.get("titulo")
  texto = request.form.get("texto")
  post = Post(titulo=titulo, texto=texto)
  db.session.add(post)
  db.session.commit()
  return redirect('/')

@app.route('/borrar', methods=["POST"])
def borrar():
  port_id = request.form.get('post_id')
  post = db.session.query(Post).filter(Post.id==port_id).first()
  db.session.delete(post)
  db.session.commit()
  return redirect('/')

if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)
