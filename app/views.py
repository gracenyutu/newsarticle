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

@app.route('/news/<str:name>')
def news(name):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(name)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)