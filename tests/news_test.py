import unittest
from app.models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("ars-technica",'Ars Technica','Ars Staff','The weekends best deals','Dealmaster also has deals','"https://cdn.arstechnica.net/wp-content/uploads/2022/04/dealmaster427-760x380.jpg','1 with 1 posters participating\r\nIts the weekend')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()