import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=27857bb3e52a4d0ea0ba90c05b590694'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY =os.environ.get("NEWS_API_KEY")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}