from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello, World!"
    return render_template("login.html")
