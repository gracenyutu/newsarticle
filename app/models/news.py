class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,author,title,description,urlToImage,content):
        self.id =id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        