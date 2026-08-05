from app.models.comparison_result import ComparisonResult


class Comparator:

    def compare(

        self,

        previous_files,

        current_files

    ):

        previous = {

            file.file_id: file

            for file in previous_files

        }

        current = {

            file.file_id: file

            for file in current_files

        }

        new_files = []

        modified_files = []

        deleted_files = []

        unchanged_files = []

        for file_id, current_file in current.items():

            if file_id not in previous:

                new_files.append(current_file)

                continue

            previous_file = previous[file_id]

            if current_file.etag != previous_file.etag:

                modified_files.append(current_file)

            else:

                unchanged_files.append(current_file)

        for file_id, previous_file in previous.items():

            if file_id not in current:

                deleted_files.append(previous_file)

        return ComparisonResult(

            new_files=new_files,

            modified_files=modified_files,

            deleted_files=deleted_files,

            unchanged_files=unchanged_files

        )