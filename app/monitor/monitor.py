from app.services.sharepoint_sync_service import SharePointSyncService
from app.utils.logger import logger


class Monitor:

    def run(self):

        logger.info("=" * 60)
        logger.info("Starting SharePoint Monitor")
        logger.info("=" * 60)

        service = SharePointSyncService()

        result = service.sync()

        logger.info("")
        logger.info("Synchronization Summary")
        logger.info("-" * 60)
        logger.info(f"New Files       : {len(result.new_files)}")
        logger.info(f"Modified Files  : {len(result.modified_files)}")
        logger.info(f"Deleted Files   : {len(result.deleted_files)}")
        logger.info(f"Unchanged Files : {len(result.unchanged_files)}")
        logger.info(f"Total Files     : {result.total_files}")

        return result