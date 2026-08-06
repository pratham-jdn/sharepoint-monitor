from app.database.db_connection import Database


class HistoryRepository:

    def __init__(self, db: Database):

        self.db = db