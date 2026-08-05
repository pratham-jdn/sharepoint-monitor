from app.database.db_connection import Database


class ScanRepository:

    def __init__(self):

        self.db = Database()