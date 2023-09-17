# Record console application
"""
Record console application with following options for crud operations:
- Add new archive
- Add new record
- Insert content into record (erasing previous and adding new content)
- Add content to record (appending existing content)
- List all records
- Show record
- Delete record
- Exit
"""

import os
from record_utils import *

if not os.path.exists("archives"):
    os.mkdir("archives")


while True:
    print("""Options:
    1 - Add new archive
    2 - Add new record
    3 - Insert content into record
    4 - Add content to record
    5 - List all records
    6 - Show record
    7 - Delete record
    8 - Exit""")
    option = int(input("Enter number of option to execute: "))

    if option == 1:
        archive_name = input("Enter name of archive: ")
        add_archive(archive_name)
    elif option == 2:
        record_name = input("Enter name of record: ")
        add_record(record_name)
    elif option == 3:
        record_name = input("Enter name of record: ")
        content = input("Enter content for record: ")
        insert_content_into_record(record_name, content)
    elif option == 4:
        record_name = input("Enter name of record: ")
        content = input("Enter content for record: ")
        add_content_to_record(record_name, content)
    elif option == 5:
        list_out_archives()
    elif option == 6:
        record_name = input("Enter name of record: ")
        show_content_from_record(record_name)
    elif option == 7:
        record_name = input("Enter name of record: ")
        delete_record(record_name)
    elif option == 8:
        break
