from app.auth.auth import AuthService


def main():

    print("=" * 60)
    print("AUTHENTICATION TEST")
    print("=" * 60)

    auth = AuthService()

    token = auth.get_access_token()

    print()

    print("SUCCESS")

    print()

    print("Access Token Length :", len(token))

    print("First 50 Characters :")

    print(token[:50] + "...")

    print()

    print("=" * 60)


if __name__ == "__main__":
    main()