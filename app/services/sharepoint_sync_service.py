from app.auth.auth import AuthService
from app.config.config import Config
from app.database.db_connection import Database
from app.database.repositories.file_repository import FileRepository
from app.graph.client import GraphClient
from app.monitor.comparator import Comparator
from app.sharepoint.crawler import SharePointCrawler
from app.utils.logger import logger


class SharePointSyncService:

    def __init__(self):

        self.db = Database()

        self.file_repository = FileRepository(self.db)

        self.comparator = Comparator()

    def authenticate(self):

        logger.info("Authenticating with Microsoft Graph...")

        access_token = AuthService().get_access_token()

        return GraphClient(access_token)

    def crawl_sharepoint(self):

        logger.info("Reading SharePoint...")

        graph = self.authenticate()

        crawler = SharePointCrawler(graph)

        drive = crawler.get_document_library(
            Config.SITE_ID
        )

        files = crawler.crawl_drive(drive)

        logger.info(f"{len(files)} SharePoint items found.")

        return files

    def load_database_snapshot(self):

        logger.info("Loading SQL snapshot...")

        files = self.file_repository.get_all()

        logger.info(f"{len(files)} SQL records loaded.")

        return files

    def compare(self, sql_files, sharepoint_files):

        return self.comparator.compare(
            sql_files,
            sharepoint_files
        )

    def apply_changes(self, result):

        logger.info("Applying database changes...")

        for file in result.new_files:
            self.file_repository.insert(file)

        for file in result.modified_files:
            self.file_repository.update(file)

        for file in result.deleted_files:
            self.file_repository.delete(file.file_id)

        logger.info("Database changes prepared.")

    def sync(self):

        try:

            sharepoint_files = self.crawl_sharepoint()

            sql_files = self.load_database_snapshot()

            result = self.compare(
                sql_files,
                sharepoint_files
            )

            self.apply_changes(result)

            self.db.commit()

            logger.info("Synchronization completed successfully.")

            return result

        except Exception:

            self.db.rollback()

            logger.exception("Synchronization failed.")

            raise

        finally:

            self.db.close()