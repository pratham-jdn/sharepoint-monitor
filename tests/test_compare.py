from app.services.sharepoint_sync_service import SharePointSyncService


def main():

    print("=" * 70)
    print("COMPARE TEST")
    print("=" * 70)

    service = SharePointSyncService()

    result = service.compare()

    print()

    print(f"New Files       : {len(result.new_files)}")

    print(f"Modified Files  : {len(result.modified_files)}")

    print(f"Deleted Files   : {len(result.deleted_files)}")

    print(f"Unchanged Files : {len(result.unchanged_files)}")

    print()

    print("=" * 70)


if __name__ == "__main__":
    main()