import requests


def call_graph_api(endpoint, access_token):

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()

    raise Exception(
        f"\nGraph API Error\n\n"
        f"Status Code : {response.status_code}\n"
        f"Response    : {response.text}"
    )


def get_drives(site_id, access_token):

    endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"

    return call_graph_api(endpoint, access_token)


def get_drive_items(drive_id, access_token):

    endpoint = (
        f"https://graph.microsoft.com/v1.0/drives/"
        f"{drive_id}/root/children"
    )

    return call_graph_api(endpoint, access_token)