from flask import Flask
from flask import render_template
import random
import datetime
import requests
'''
jinja framework rendering Dynamic HTML coding
which is built in with Flask
'''
agify_url ="https://genderize.io/"
app = Flask(__name__) # __name__ is a special attribute.
print(__name__)
@app.route('/')
def home_page():
    random_number = random.randint(0,20)
    current_year =datetime.datetime.now().year
    return render_template("gaya.html", num=random_number,year = current_year)
# rendering static files using Flask

@app.route("/guess/<name>")
def guess_func(name):
    g_url =f"https://api.genderize.io?name={name}"
    response = requests.get(g_url)
    gen = response.json()
    gender =gen["gender"]

    a_url= f"https://api.agify.io?name={name}"
    response1 =requests.get(a_url)
    age1 =response1.json()
    age =age1["age"]
    return render_template("gaya.html",person_name =name.title(),person_gender =gender,person_age=age)


if __name__ == "__main__":
    app.run(debug=True)
