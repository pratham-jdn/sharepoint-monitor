from app.services.sharepoint_sync_service import SharePointSyncService


def main():

    print("=" * 70)
    print("SYNC SERVICE TEST")
    print("=" * 70)

    service = SharePointSyncService()

    sharepoint_files = service.crawl_sharepoint()

    sql_files = service.load_database_snapshot()

    print()

    print(f"SharePoint Files : {len(sharepoint_files)}")

    print(f"SQL Files        : {len(sql_files)}")

    print()

    print("=" * 70)


if __name__ == "__main__":
    main()