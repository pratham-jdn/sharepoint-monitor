from app.database.db_connection import Database


def main():

    print("=" * 60)

    print("DATABASE TEST")

    print("=" * 60)

    db = Database()

    print()

    print("SUCCESS")

    print()

    print("SQL Connection Established")

    db.close()

    print()

    print("=" * 60)


if __name__ == "__main__":
    main()