from pymongo import MongoClient


client = MongoClient()

class ShoppingDB(object):
    """База данных"""
    def __init__(self):
        #self.category = client.category_db
        self.db = client.shopping_db
        self.SHOP = {
            'category': '',
            'product': '',
            'count': 0
        }

    def new_category(self, category):
        '''создать запись в БД с катигорией'''
        self.SHOP['category'] = category
        self.db.shopping.insert(self.SHOP)
