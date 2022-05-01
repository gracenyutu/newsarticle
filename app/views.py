from flask import render_template
from app import app
from .requests import get_news

@app.route("/")
@app.route("/home")
def home():
    '''
    View root page function that returns the home page and its data
    '''
    title = 'Home - Welcome to The best News Articles Website Online'
    return render_template('home.html')

