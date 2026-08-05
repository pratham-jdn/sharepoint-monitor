import pyodbc

from app.config.config import Config
from app.utils.logger import logger


class Database:

    def __init__(self):

        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={Config.SQL_SERVER};"
            f"DATABASE={Config.SQL_DATABASE};"
            "Trusted_Connection=yes;"
        )

        self.connection = pyodbc.connect(connection_string)

        self.connection.autocommit = False

        self.cursor = self.connection.cursor()

        logger.info("Connected to SQL Server")

    def commit(self):

        self.connection.commit()

        logger.info("Transaction Committed")

    def rollback(self):

        self.connection.rollback()

        logger.info("Transaction Rolled Back")

    def close(self):

        self.cursor.close()

        self.connection.close()

        logger.info("Database Connection Closed")