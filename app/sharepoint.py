from app.graph import (
    get_root_items,
    get_folder_items
)


def crawl_drive(
    drive_id,
    access_token,
    site_id,
    folder_id=None,
    current_path="",
    files=None
):

    if files is None:
        files = []

    if folder_id is None:

        response = get_root_items(
            drive_id,
            access_token
        )

    else:

        response = get_folder_items(
            drive_id,
            folder_id,
            access_token
        )

    for item in response["value"]:

        if "folder" in item:

            next_path = (
                f"{current_path}/{item['name']}"
                if current_path
                else item["name"]
            )

            crawl_drive(

                drive_id,

                access_token,

                site_id,

                item["id"],

                next_path,

                files

            )

        else:

            files.append({

                "id": item["id"],

                "name": item["name"],

                "parent_path": current_path,

                "size": item.get("size"),

                "etag": item.get("eTag"),

                "ctag": item.get("cTag"),

                "created": item.get("createdDateTime"),

                "modified": item.get("lastModifiedDateTime"),

                "created_by":
                    item.get("createdBy", {})
                        .get("user", {})
                        .get("displayName"),

                "modified_by":
                    item.get("lastModifiedBy", {})
                        .get("user", {})
                        .get("displayName"),

                "web_url":
                    item.get("webUrl"),

                "drive_id":
                    drive_id,

                "site_id":
                    site_id

            })

    return files