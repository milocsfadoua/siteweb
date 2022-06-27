from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/notreequipe')
def notre_equipe():
  return render_template("notreequipe.html")

@app.route('/acceuil')
def acceuil():
  return render_template("acceuil.html")

@app.route('/nosprix')
def nos_prix():
  return render_template("nosprix.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")




app.run(host='0.0.0.0', port=81)
