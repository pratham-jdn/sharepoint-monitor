from app.auth import get_access_token

from app.graph import get_drives

from app.sharepoint import crawl_drive

from app.monitor import Monitor

from app.config import SITE_ID


def main():

    token = get_access_token()

    if "access_token" not in token:

        print(token)

        return

    access_token = token["access_token"]

    drives = get_drives(
        SITE_ID,
        access_token
    )

    drive_id = None

    for drive in drives["value"]:

        if drive["driveType"] == "documentLibrary":

            drive_id = drive["id"]

            break

    files = crawl_drive(

        drive_id,

        access_token,

        SITE_ID

    )

    monitor = Monitor()

    inserted, skipped = monitor.sync(files)

    print()

    print("=" * 60)

    print("SCAN SUMMARY")

    print("=" * 60)

    print(f"Files Found      : {len(files)}")

    print(f"Inserted         : {inserted}")

    print(f"Already Present  : {skipped}")


if __name__ == "__main__":

    main()