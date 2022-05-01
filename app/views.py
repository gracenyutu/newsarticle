from flask import render_template
from app import app
from .requests import get_sources,get_news,search_articles,articles_source

@app.route("/")
@app.route("/home")
def home():
    '''
    View root page function that returns the home page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources("business")
    sports_news = get_sources("sports")
    return render_template('sources.html')

@app.route('/newsArticles')
def newsArticles():

    '''
    View news page function that returns the news details page and its data
    '''
    health_articles = get_news('health')
    education_articles = get_news('technology')

    return render_template('news.html',health=health_articles, technology=education_articles)

@app.route('/search/<article_name>')
def articleSearch(article_name):
    """
    function that returns the searched articles
    """
    search_article_name = article_name.split("")
    search_name_format = "+".join(search_article_name)
    searched_articles = search_articles(search_name_format)

    return render_template('search.html',articles = searched_articles)

@app.route('/articles/<id>')
def sourceArticles(id):
    all_articles = articles_source(id)
    print(all_articles)
    source = id
    return render_template('sourcearticles.html', articles = all_articles, source = source)