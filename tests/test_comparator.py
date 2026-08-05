from app.models.file_metadata import FileMetadata
from app.monitor.comparator import Comparator


previous = [

    FileMetadata(

        file_id="1",

        name="A.docx",

        item_type="File",

        parent_path="/",

        web_url="",

        drive_id="",

        site_id="",

        size=100,

        etag="111",

        ctag="",

        created_date=None,

        modified_date=None,

        created_by="",

        modified_by="",

        downloaded=False,

        download_path=None,

        status="Active",

        last_scan=None

    ),

    FileMetadata(

        file_id="2",

        name="B.docx",

        item_type="File",

        parent_path="/",

        web_url="",

        drive_id="",

        site_id="",

        size=100,

        etag="222",

        ctag="",

        created_date=None,

        modified_date=None,

        created_by="",

        modified_by="",

        downloaded=False,

        download_path=None,

        status="Active",

        last_scan=None

    )

]


current = [

    FileMetadata(

        file_id="1",

        name="A.docx",

        item_type="File",

        parent_path="/",

        web_url="",

        drive_id="",

        site_id="",

        size=100,

        etag="111",

        ctag="",

        created_date=None,

        modified_date=None,

        created_by="",

        modified_by="",

        downloaded=False,

        download_path=None,

        status="Active",

        last_scan=None

    ),

    FileMetadata(

        file_id="2",

        name="B.docx",

        item_type="File",

        parent_path="/",

        web_url="",

        drive_id="",

        site_id="",

        size=100,

        etag="999",

        ctag="",

        created_date=None,

        modified_date=None,

        created_by="",

        modified_by="",

        downloaded=False,

        download_path=None,

        status="Active",

        last_scan=None

    ),

    FileMetadata(

        file_id="3",

        name="C.docx",

        item_type="File",

        parent_path="/",

        web_url="",

        drive_id="",

        site_id="",

        size=100,

        etag="333",

        ctag="",

        created_date=None,

        modified_date=None,

        created_by="",

        modified_by="",

        downloaded=False,

        download_path=None,

        status="Active",

        last_scan=None

    )

]


result = Comparator().compare(

    previous,

    current

)

print()

print("New Files       :", len(result.new_files))

print("Modified Files  :", len(result.modified_files))

print("Deleted Files   :", len(result.deleted_files))

print("Unchanged Files :", len(result.unchanged_files))

print("Total           :", result.total_files)