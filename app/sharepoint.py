from app.graph import (
    get_root_items,
    get_folder_items
)


def crawl_drive(
        drive_id,
        access_token,
        folder_id=None,
        current_path="",
        level=0,
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

        indent = "    " * level

        if "folder" in item:

            print(f"{indent}📁 {item['name']}")

            next_path = (
                f"{current_path}/{item['name']}"
                if current_path
                else item["name"]
            )

            crawl_drive(
                drive_id,
                access_token,
                item["id"],
                next_path,
                level + 1,
                files
            )

        else:

            print(f"{indent}📄 {item['name']}")

            files.append({
                "id": item["id"],
                "name": item["name"],
                "path": (
                    f"{current_path}/{item['name']}"
                    if current_path
                    else item["name"]
                ),
                "size": item["size"],
                "last_modified": item["lastModifiedDateTime"],
                "download_url": item.get(
                    "@microsoft.graph.downloadUrl"
                )
            })

    return files