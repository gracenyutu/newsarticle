# from app import app
import urllib.request,json

from .models import News, Sources

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

# News = news.News
# Sources = sources.Sources

def configure_request(app):
    global api_key,base_url,source_url,news_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_url = app.config['SOURCE_ARTICLES_URL']
    news_url = app.config['NEWS_ARTICLES_APL_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('original_title')
        description = news_item.get('description')
        url= news_item.get('url')
        urlToImage= news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(name,author,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results

def get_news(name):
    get_news_details_url = base_url.format(name,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            name = news_details_response.get('name')
            author = news_details_response.get('author')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            url= news_details_response.get('url')
            urlToImage = news_details_response.get('urlToImage')
            publishedAt = news_details_response.get('publishedAt')
            content = news_details_response.get('content')

            news_object = News(name,author,title,description,urlToImage,publishedAt,content)

    return news_object

def get_sources(category):
    """
    function that gets response from the api call
    """    
    sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)

        sources_outcome = None

        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome

def process_new_sources(sources_list):
    sources_outcome = []

    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")
        
        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)
    
    return sources_outcome

def articles_source(source):
    sources_a_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(source,api_key)

    with urllib.request.urlopen(sources_a_url) as url:
        art_data = url.read()
        response = json.loads(art_data)
        source_articles = None
        if response['articles']:
            source_articles_list = response['articles']
            source_articles = process_articles_source(source_articles_list)
    return source_articles

def process_articles_source(article_list):
    source_articles = []
    for art in article_list:
        source = art.get("source")
        author = art.get('author')
        title = art.get('title')
        description = art.get('description')
        url = art.get('url')
        urlToImage = art.get('urlToImage')
        publishedAt = art.get('publishedAt')
        content = art.get('content')
        
        article_object = News(source,author,title,description,url,urlToImage,publishedAt)
        source_articles.append(article_object)
    return source_articles

def search_articles(article_name):
    search_url = news_url.format(article_name,api_key)

    with urllib.request.urlopen(search_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)

        search_results = None

        if search_response['articles']:
            search_results = search_response['articles']
            search_outcome = process_search(search_results)
    return search_outcome

    
