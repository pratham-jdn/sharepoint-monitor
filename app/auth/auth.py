from msal import ConfidentialClientApplication

from app.config import (
    CLIENT_ID,
    CLIENT_SECRET,
    AUTHORITY,
    GRAPH_SCOPE
)


def get_access_token():

    app = ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=AUTHORITY
    )

    token = app.acquire_token_for_client(
        scopes=GRAPH_SCOPE
    )

    return token