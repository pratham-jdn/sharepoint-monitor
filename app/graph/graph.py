import requests


GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"


def call_graph_api(endpoint, access_token):

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()

    raise Exception(
        f"\nGraph API Error\n"
        f"Status Code : {response.status_code}\n"
        f"Response    : {response.text}"
    )


def get_drives(site_id, access_token):

    endpoint = f"{GRAPH_BASE_URL}/sites/{site_id}/drives"

    return call_graph_api(endpoint, access_token)


def get_root_items(drive_id, access_token):

    endpoint = (
        f"{GRAPH_BASE_URL}/drives/"
        f"{drive_id}/root/children"
    )

    return call_graph_api(endpoint, access_token)


def get_folder_items(drive_id, folder_id, access_token):

    endpoint = (
        f"{GRAPH_BASE_URL}/drives/"
        f"{drive_id}/items/{folder_id}/children"
    )

    return call_graph_api(endpoint, access_token)