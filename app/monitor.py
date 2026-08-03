from app.database import Database


class Monitor:

    def __init__(self):

        self.db = Database()

    def sync(self, files):

        inserted = 0

        skipped = 0

        for file in files:

            if self.db.file_exists(file["id"]):

                skipped += 1

            else:

                self.db.insert_file(file)

                inserted += 1

        self.db.close()

        return inserted, skipped