from app.monitor.monitor import Monitor


def main():

    print("=" * 70)
    print("FULL SYNCHRONIZATION TEST")
    print("=" * 70)

    result = Monitor().run()

    print()

    print("Synchronization completed successfully.")

    print()

    print(result.summary)

    print()

    print("=" * 70)


if __name__ == "__main__":
    main()