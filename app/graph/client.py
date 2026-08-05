import requests

from app.config.config import Config


class GraphClient:

    def __init__(self, access_token):

        self.headers = {

            "Authorization": (
                f"Bearer {access_token}"
            )
        }

    def get(self, endpoint):

        response = requests.get(

            Config.GRAPH_BASE_URL + endpoint,

            headers=self.headers
        )

        if response.status_code != 200:

            raise Exception(

                f"Graph API Error\n"

                f"{response.status_code}\n"

                f"{response.text}"
            )

        return response.json()