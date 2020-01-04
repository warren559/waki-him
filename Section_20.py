# 157 Your First Website
# Flask is a Python Framework that has all the tools and the functions to build a website
# import the Flask class rom the flask module
from flask import Flask, render_template
# create a instance of the flask class
app = Flask(__name__)

# decorator
@app.route('/')  # url to view your home page

# write a function which will define what your webpage will do
def home():
    # 158 HTML Templates
    # Next we will learn how to return a HTML template
    # we are going to use the render_template method of the flask library
    # render_template acesses a html file stored in your python files directory and displays the html in the requested url
    return render_template('home.html')  # this file is stored in the templates folder

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

# 167 Creating a Python Virtual Environment
# to run our program we use Python which is from our main application
# this not a good practice
# good practice is to have aclean installation of python - no libraries installed which you do not need
# for this wee need a virtual environment
# install virtualenv
# nest create a virtual environment
# next we will deploy this website on the cloud

# Deploying the website to a live Server
# in Python we deploy the application through the Terminal
# so we are going to create our new app (on heroku) through using the command line
# to upload files to heroku we are going to use git
# git is installed by defualt if you have heroku belt
