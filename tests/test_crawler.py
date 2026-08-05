from app.auth.auth import AuthService
from app.config.config import Config
from app.graph.client import GraphClient
from app.sharepoint.crawler import SharePointCrawler


def main():

    print("=" * 60)
    print("SHAREPOINT CRAWLER TEST")
    print("=" * 60)

    access_token = AuthService().get_access_token()

    graph = GraphClient(access_token)

    crawler = SharePointCrawler(graph)

    drive = crawler.get_document_library(Config.SITE_ID)

    print(f"Document Library : {drive['name']}")
    print()

    files = crawler.crawl_drive(drive)

    file_count = 0
    folder_count = 0

    for item in files:

        if item.item_type == "Folder":
            folder_count += 1
        else:
            file_count += 1

    print("=" * 60)
    print("CRAWL SUMMARY")
    print("=" * 60)

    print(f"Folders : {folder_count}")
    print(f"Files   : {file_count}")
    print(f"Total   : {len(files)}")

    print()
    print("First 10 Items")
    print("-" * 60)

    for item in files[:10]:

        print(f"{item.item_type:7} | {item.parent_path}/{item.name}")

    print("=" * 60)


if __name__ == "__main__":
    main()