from flask import Flask
app = Flask(__name__)   # here app is object and Flask is class we pass argument _name_ = _main_
@app.route("/")
def hello_world():
    return "Hello world!"

if __name__== '__main__':
    app.run(host='127.0.0.1',debug=True)  #app.run is Flask method to run a Flask app