from dotenv import load_dotenv
import os

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SITE_ID = os.getenv("SITE_ID")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_DRIVER = os.getenv("SQL_DRIVER")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

GRAPH_SCOPE = [
    "https://graph.microsoft.com/.default"
]