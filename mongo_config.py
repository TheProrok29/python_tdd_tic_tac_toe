from pymongo import MongoClient


class TicTacToeCollection:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['tic_tac_toe']
        self.my_col = self.db['game']
        print(self.db.list_collection_names())

    def get_db_collection_name(self):
        return self.my_col.name

    def get_db_name(self):
        return self.db.name
