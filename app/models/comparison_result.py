from dataclasses import dataclass
from typing import List

from app.models.file_metadata import FileMetadata


@dataclass
class ComparisonResult:

    new_files: List[FileMetadata]

    modified_files: List[FileMetadata]

    deleted_files: List[FileMetadata]

    unchanged_files: List[FileMetadata]

    @property
    def total_files(self):

        return (
            len(self.new_files)
            + len(self.modified_files)
            + len(self.deleted_files)
            + len(self.unchanged_files)
        )