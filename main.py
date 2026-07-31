from auth import get_access_token
from graph import (
    get_drives,
    get_drive_items
)
from config import SITE_ID


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

    print("=" * 80)
    print("DOCUMENT LIBRARIES")
    print("=" * 80)

    drive_id = None

    for drive in drives["value"]:

        print(f"Name       : {drive['name']}")
        print(f"Drive ID   : {drive['id']}")
        print(f"Drive Type : {drive['driveType']}")
        print("-" * 80)

        if drive["driveType"] == "documentLibrary":
            drive_id = drive["id"]

    if drive_id is None:
        print("No document library found.")
        return

    print("\n")

    print("=" * 80)
    print("FILES AND FOLDERS")
    print("=" * 80)

    items = get_drive_items(
        drive_id,
        access_token
    )

    for item in items["value"]:

        if "folder" in item:
            print(f"📁 {item['name']}")
        else:
            print(f"📄 {item['name']}")

        print(f"ID           : {item['id']}")
        print(f"Last Modified: {item['lastModifiedDateTime']}")
        print(f"Size         : {item['size']} bytes")

        print("-" * 80)


if __name__ == "__main__":
    main()