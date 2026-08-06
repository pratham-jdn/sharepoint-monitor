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

    @property
    def has_changes(self):

        return (
            len(self.new_files)
            + len(self.modified_files)
            + len(self.deleted_files)
        ) > 0

    @property
    def summary(self):

        return {
            "new": len(self.new_files),
            "modified": len(self.modified_files),
            "deleted": len(self.deleted_files),
            "unchanged": len(self.unchanged_files),
            "total": self.total_files,
        }