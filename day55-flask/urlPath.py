'''
Working Flask URL paths and the Flask debugger
debug mode on: it helps us narrow down the issues
rendering HTML elements
'''
from flask import Flask
app =Flask(__name__)

'''
Variable Rules
You can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
'''
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p> Thos is my first paragraph</p>' \
           '<img src ="https://media2.giphy.com/media/We4OBLi8bjPD5m2Smv/200w.webp?cid=ecf05e475d9rj751a1mk6qvw5csn7cnfk2363g3s4g8ud6ei&rid=200w.webp&ct=g">'


def make_bold(function):
    def wrapper():
        return '<b>'+function()+'</b>'
    return wrapper
def make_em(function):
    def wrapper():
        return '<em>'+function()+'</em>'
    return wrapper
def make_uLine(function):
    def wrapper():
        return '<u>'+function()+'</u>'
    return wrapper
@app.route('/bye')
@make_bold
@make_em
@make_uLine
def say_bye():
    return "<u><em><b>Bye!</b></em></u>"

@app.route('/username/<name>/<int:number>') # just '/<name>'--- variable path and is not going to work and we
#have to stop and rerun the server everytime.We should make debug mode on

def greet(name,number):
    return f"Hello {name}, you are a {number} old!"


if __name__ =="__main__":
    app.run(debug=True)
    # debugmode on: narrow down any issue. And whenever we update the and save the file it will update in the browser at
    #the same time.
