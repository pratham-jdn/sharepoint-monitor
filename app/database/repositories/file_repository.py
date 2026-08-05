from datetime import datetime

from app.database.db_connection import Database
from app.models.file_metadata import FileMetadata


class FileRepository:

    def __init__(self):

        self.db = Database()

    def get_all(self):

        query = """
        SELECT *
        FROM SharePointFiles
        """

        self.db.cursor.execute(query)

        rows = self.db.cursor.fetchall()

        files = []

        for row in rows:

            files.append(

                FileMetadata(

                    file_id=row.FileId,

                    name=row.Name,

                    item_type=row.ItemType,

                    parent_path=row.ParentPath,

                    web_url=row.WebUrl,

                    drive_id=row.DriveId,

                    site_id=row.SiteId,

                    size=row.Size,

                    etag=row.ETag,

                    ctag=row.CTag,

                    created_date=row.CreatedDate,

                    modified_date=row.ModifiedDate,

                    created_by=row.CreatedBy,

                    modified_by=row.ModifiedBy,

                    downloaded=row.Downloaded,

                    download_path=row.DownloadPath,

                    status=row.Status,

                    last_scan=row.LastScan

                )

            )

        return files

    def exists(self, file_id):

        query = """
        SELECT COUNT(*)
        FROM SharePointFiles
        WHERE FileId=?
        """

        self.db.cursor.execute(query, file_id)

        return self.db.cursor.fetchone()[0] > 0

    def insert(self, file: FileMetadata):

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

            ModifiedBy,

            Downloaded,

            DownloadPath,

            Status,

            LastScan

        )

        VALUES

        (

            ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?

        )
        """

        self.db.cursor.execute(

            query,

            file.file_id,

            file.name,

            file.item_type,

            file.parent_path,

            file.web_url,

            file.drive_id,

            file.site_id,

            file.size,

            file.etag,

            file.ctag,

            file.created_date,

            file.modified_date,

            file.created_by,

            file.modified_by,

            file.downloaded,

            file.download_path,

            file.status,

            datetime.now()

        )


    def update(self, file: FileMetadata):

        query = """
        UPDATE SharePointFiles

        SET

            Name=?,

            ItemType=?,

            ParentPath=?,

            WebUrl=?,

            DriveId=?,

            SiteId=?,

            Size=?,

            ETag=?,

            CTag=?,

            CreatedDate=?,

            ModifiedDate=?,

            CreatedBy=?,

            ModifiedBy=?,

            Downloaded=?,

            DownloadPath=?,

            Status=?,

            LastScan=?

        WHERE FileId=?
        """

        self.db.cursor.execute(

            query,

            file.name,

            file.item_type,

            file.parent_path,

            file.web_url,

            file.drive_id,

            file.site_id,

            file.size,

            file.etag,

            file.ctag,

            file.created_date,

            file.modified_date,

            file.created_by,

            file.modified_by,

            file.downloaded,

            file.download_path,

            file.status,

            datetime.now(),

            file.file_id

        )


    def delete(self, file_id):

        query = """
        DELETE FROM SharePointFiles
        WHERE FileId=?
        """

        self.db.cursor.execute(query, file_id)


    def close(self):

        self.db.close()