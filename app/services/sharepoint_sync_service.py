from app.auth.auth import AuthService
from app.config.config import Config
from app.database.repositories.file_repository import FileRepository
from app.graph.client import GraphClient
from app.monitor.comparator import Comparator
from app.sharepoint.crawler import SharePointCrawler
from app.utils.logger import logger


class SharePointSyncService:

    def __init__(self):

        self.repository = FileRepository()

        self.comparator = Comparator()

    def authenticate(self):

        logger.info("Authenticating...")

        access_token = AuthService().get_access_token()

        return GraphClient(access_token)

    def crawl_sharepoint(self, graph):

        logger.info("Reading SharePoint...")

        crawler = SharePointCrawler(graph)

        drive = crawler.get_document_library(
            Config.SITE_ID
        )

        files = crawler.crawl_drive(drive)

        logger.info(
            f"{len(files)} SharePoint items discovered."
        )

        return files

    def load_database_snapshot(self):

        logger.info(
            "Reading SQL Snapshot..."
        )

        files = self.repository.get_all()

        logger.info(
            f"{len(files)} records loaded from SQL."
        )

        return files