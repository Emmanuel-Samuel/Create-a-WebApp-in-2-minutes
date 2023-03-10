# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 10/03/2023
# REVISED DATE: 10/03/2023
# PURPOSE: Create a website in 2 minutes

# import modules
from flask import Flask, render_template, request

# create an instance of the app, gets input as string
app = Flask(__name__)

@app.route('/')
# function returns a home page
def home():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
# function gets input from user
def home_post():
    # gets breath from html
    breadth_input = request.form['breadth_dim']
    # gets height from html
    height_input = request.form['height_dim']
    # constant variable half in area formular defined
    half = 0.5
    # calculates area
    area = float(breadth_input) * float(height_input) * half
    # returns a message with output
    message = "The Area is " + str(area) + " m^2"
    # returns the message and values
    return render_template('index.html', output=message,
                           breadth=breadth_input, height=height_input)

# if you running replit, you need to add this
#app.run(host='0.0.0.0')
app.run(host='')

