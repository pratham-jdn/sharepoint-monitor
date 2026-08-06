from app.graph.client import GraphClient
from app.models.file_metadata import FileMetadata


class SharePointCrawler:

    def __init__(self, graph_client: GraphClient):

        self.graph = graph_client

    def get_document_library(self, site_id):

        response = self.graph.get(
            f"/sites/{site_id}/drives"
        )

        for drive in response["value"]:

            if drive["driveType"] == "documentLibrary":

                return drive

        raise Exception("Document Library not found.")

    def crawl_drive(self, drive):

        files = []

        self.__crawl_folder(

            drive_id=drive["id"],

            folder_id="root",

            current_path="",

            current_drive=drive["id"],

            current_site=drive.get(
                "sharepointIds",
                {}
            ).get(
                "siteId",
                ""
            ),

            files=files

        )

        return files

    def __crawl_folder(

        self,

        drive_id,

        folder_id,

        current_path,

        current_drive,

        current_site,

        files

    ):

        response = self.graph.get(

            f"/drives/{drive_id}/items/{folder_id}/children"

        )

        for item in response["value"]:

            path = (

                f"{current_path}/{item['name']}"

                if current_path

                else item["name"]

            )

            is_folder = "folder" in item

            # -----------------------------
            # Recurse into folders
            # -----------------------------
            if is_folder:

                self.__crawl_folder(

                    drive_id=drive_id,

                    folder_id=item["id"],

                    current_path=path,

                    current_drive=current_drive,

                    current_site=current_site,

                    files=files

                )

                continue

            # -----------------------------
            # Store ONLY files
            # -----------------------------
            files.append(

                FileMetadata(

                    file_id=item["id"],

                    name=item["name"],

                    item_type="File",

                    parent_path=current_path,

                    web_url=item.get("webUrl"),

                    drive_id=current_drive,

                    site_id=current_site,

                    size=item.get("size", 0),

                    etag=item.get("eTag"),

                    ctag=item.get("cTag"),

                    created_date=item.get(
                        "createdDateTime"
                    ),

                    modified_date=item.get(
                        "lastModifiedDateTime"
                    ),

                    created_by=item.get(
                        "createdBy",
                        {}
                    ).get(
                        "user",
                        {}
                    ).get(
                        "displayName"
                    ),

                    modified_by=item.get(
                        "lastModifiedBy",
                        {}
                    ).get(
                        "user",
                        {}
                    ).get(
                        "displayName"
                    ),

                    downloaded=False,

                    download_path=None,

                    status="Active",

                    last_scan=None

                )

            )