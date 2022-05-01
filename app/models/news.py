class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name,author,title,description,urlToImage,publishedAt,content):
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        