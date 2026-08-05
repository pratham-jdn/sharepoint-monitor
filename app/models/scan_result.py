from dataclasses import dataclass


@dataclass
class ScanResult:

    total_files: int

    new_files: int

    modified_files: int

    deleted_files: int

    unchanged_files: int