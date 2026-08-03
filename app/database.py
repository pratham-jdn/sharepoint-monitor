import pyodbc

from app.config import (
    SQL_SERVER,
    SQL_DATABASE,
    SQL_DRIVER
)


class Database:

    def __init__(self):

        connection_string = (
            f"DRIVER={{{SQL_DRIVER}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"Trusted_Connection=yes;"
            f"TrustServerCertificate=yes;"
        )

        self.connection = pyodbc.connect(connection_string)

        self.cursor = self.connection.cursor()

    def file_exists(self, file_id):

        query = """
        SELECT COUNT(*)
        FROM SharePointFiles
        WHERE FileId=?
        """

        self.cursor.execute(query, file_id)

        count = self.cursor.fetchone()[0]

        return count > 0

    def insert_file(self, file):

        query = """
        INSERT INTO SharePointFiles
        (
            FileId,
            Name,
            ItemType,
            ParentPath,
            WebUrl,
            DriveId,
            SiteId,
            Size,
            ETag,
            CTag,
            CreatedDate,
            ModifiedDate,
            CreatedBy,
            ModifiedBy
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?,?,?,?,?
        )
        """

        self.cursor.execute(

            query,

            file["id"],

            file["name"],

            "File",

            file["parent_path"],

            file["web_url"],

            file["drive_id"],

            file["site_id"],

            file["size"],

            file["etag"],

            file["ctag"],

            file["created"],

            file["modified"],

            file["created_by"],

            file["modified_by"]

        )

        self.connection.commit()

    def close(self):

        self.cursor.close()

        self.connection.close()