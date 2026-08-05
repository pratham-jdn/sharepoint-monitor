from app.auth.auth import AuthService
from app.graph.client import GraphClient
from app.config.config import Config


def main():

    print("=" * 60)
    print("GRAPH CLIENT TEST")
    print("=" * 60)

    access_token = AuthService().get_access_token()

    graph = GraphClient(access_token)

    site = graph.get(f"/sites/{Config.SITE_ID}")

    print()

    print("SUCCESS")

    print()

    print("Site Name :", site["displayName"])
    print("Site URL  :", site["webUrl"])

    print()

    print("=" * 60)


if __name__ == "__main__":
    main()