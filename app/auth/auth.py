from msal import ConfidentialClientApplication

from app.config.config import Config
from app.utils.logger import logger


class AuthService:

    def __init__(self):

        self.app = ConfidentialClientApplication(

            client_id=Config.CLIENT_ID,

            client_credential=Config.CLIENT_SECRET,

            authority=Config.AUTHORITY
        )

    def get_access_token(self):

        token = self.app.acquire_token_for_client(

            scopes=Config.GRAPH_SCOPE
        )

        if "access_token" not in token:

            logger.error(token)

            raise Exception(
                "Authentication Failed"
            )

        logger.info(
            "Authentication Successful"
        )

        return token["access_token"]