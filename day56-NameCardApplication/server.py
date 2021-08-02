from flask import Flask
from flask import render_template

app = Flask(__name__) # __name__ is a special attribute.
print(__name__)
@app.route('/')
def home_page():
    return render_template("index.html")
# rendering static files using Flask

if __name__ == "__main__":
    app.run(debug=True)
