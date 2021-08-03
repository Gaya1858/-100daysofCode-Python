from flask import Flask
from flask import render_template
import random
import datetime
'''
jinja framework rendering Dynamic HTML coding
which is built in with Flask
'''

app = Flask(__name__) # __name__ is a special attribute.
print(__name__)
@app.route('/')
def home_page():
    random_number = random.randint(0,20)
    current_year =datetime.datetime.now().year
    return render_template("gaya.html", num=random_number,year = current_year)
# rendering static files using Flask

if __name__ == "__main__":
    app.run(debug=True)
