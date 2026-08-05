from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    # Azure AD

    TENANT_ID = os.getenv("TENANT_ID")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    # SharePoint

    SITE_ID = os.getenv("SITE_ID")

    # SQL Server

    SQL_SERVER = os.getenv(
        "SQL_SERVER",
        "localhost"
    )

    SQL_DATABASE = os.getenv(
        "SQL_DATABASE",
        "SharePointMonitorDB"
    )

    # Microsoft Graph

    AUTHORITY = (
        f"https://login.microsoftonline.com/{TENANT_ID}"
    )

    GRAPH_SCOPE = [
        "https://graph.microsoft.com/.default"
    ]

    GRAPH_BASE_URL = (
        "https://graph.microsoft.com/v1.0"
    )