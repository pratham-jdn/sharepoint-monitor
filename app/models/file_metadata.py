from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class FileMetadata:

    file_id: str

    name: str

    item_type: str

    parent_path: str

    web_url: str

    drive_id: str

    site_id: str

    size: int

    etag: Optional[str]

    ctag: Optional[str]

    created_date: Optional[datetime]

    modified_date: Optional[datetime]

    created_by: Optional[str]

    modified_by: Optional[str]

    downloaded: bool = False

    download_path: Optional[str] = None

    status: str = "Active"

    last_scan: Optional[datetime] = None