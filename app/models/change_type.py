from enum import Enum


class ChangeType(Enum):

    NEW = "New"

    MODIFIED = "Modified"

    DELETED = "Deleted"

    UNCHANGED = "Unchanged"