from app.services.sharepoint_sync_service import SharePointSyncService


def main():

    print("=" * 60)
    print("SYNC SERVICE TEST")
    print("=" * 60)

    service = SharePointSyncService()

    graph = service.authenticate()

    sharepoint_files = service.crawl_sharepoint(graph)

    sql_files = service.load_database_snapshot()

    print()

    print(f"SharePoint Files : {len(sharepoint_files)}")

    print(f"SQL Files        : {len(sql_files)}")

    print()

    print("=" * 60)


if __name__ == "__main__":
    main()