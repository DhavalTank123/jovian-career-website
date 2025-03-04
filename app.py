from flask import Flask,render_template,jsonify
app = Flask(__name__)   # here app is object and Flask is class we pass argument _name_ = _main_

JOBS = [
    {
        "id":"1",
        "title":"Data Analyst",
        "location":"Bangaluru,India",
        "salary":"Rs 10,00,000"
    },
     {
        "id":"2",
        "title":"Data Scientist",
        "location":"Delhi,India",
        "salary":"Rs 15,00,000"
    },
     {
        "id":"3",
        "title":"Frontend",
        "location":"Remote",

    },
      {
        "id":"4",
        "title":"Backend",
        "location":"San Francisco ,USA",
        "salary":"Rs 20,00,000"
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name="Job")

@app.route("/api/jobs")
def job_list():
    return jsonify(JOBS)

if __name__== '__main__':
    app.run(host='127.0.0.1',debug=True)  #app.run is Flask method to run a Flask app