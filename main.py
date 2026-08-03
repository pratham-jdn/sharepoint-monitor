from app.auth import get_access_token
from app.graph import get_drives
from app.config import SITE_ID
from app.sharepoint import crawl_drive


def main():

    token = get_access_token()

    if "access_token" not in token:
        print(token)
        return

    access_token = token["access_token"]

    print("\nAuthentication Successful!\n")

    drives = get_drives(
        SITE_ID,
        access_token
    )

    drive_id = None

    print("=" * 80)
    print("DOCUMENT LIBRARIES")
    print("=" * 80)

    for drive in drives["value"]:

        print(f"Name : {drive['name']}")
        print(f"ID   : {drive['id']}")
        print("-" * 80)

        if drive["driveType"] == "documentLibrary":
            drive_id = drive["id"]

    if drive_id is None:
        print("No document library found.")
        return

    print()

    print("=" * 80)
    print("RECURSIVE SHAREPOINT CRAWL")
    print("=" * 80)

    all_files = crawl_drive(
        drive_id,
        access_token
    )

    print()

    print("=" * 80)
    print(f"TOTAL FILES FOUND : {len(all_files)}")
    print("=" * 80)

    for file in all_files:
        print(file["path"])


if __name__ == "__main__":
    main()