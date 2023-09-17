# Utility functions for record app

import os


def add_archive(archive_name):
    if not os.path.exists(f"archives/{archive_name}"):
        os.mkdir(f"archives/{archive_name}")
        print(f"Archive '{archive_name}' successfully created.")
        return
    print(f"Archive with name '{archive_name}' already exists.")


def add_record(record_name):
    if not os.path.exists(f"records/{record_name}"):
        open(f"archives/{record_name}.txt", "w+")
        print(f"Record '{record_name}' successfully created.")
        return
    print(f"Record with name '{record_name}' already exists.")


def list_out_archives():
    for root, dirs, files in os.walk("archives", topdown=False):
        for filename in files:
            print(f"Record: {os.path.join(root, filename)}")
        for dirname in dirs:
            print(f"Archive: {os.path.join(root, dirname)}")


def insert_content_into_record(record_name, content):
    if not os.path.exists(f"archives/{record_name}.txt"):
        print(f"Invalid record name! Record with '{record_name}' doesn't exist.")
        return
    file = open(f"archives/{record_name}.txt", "w")
    file.write(content + "\n")
    file.flush()
    file.close()
    print(f"Content successfully written in '{record_name}'")


def add_content_to_record(record_name, content):
    if not os.path.exists(f"archives/{record_name}.txt"):
        print(f"Invalid record name! Record with '{record_name}' doesn't exist.")
        return
    file = open(f"archives/{record_name}.txt", "a")
    file.write(content + "\n")
    file.flush()
    file.close()
    print(f"Content successfully added in '{record_name}'")


def show_content_from_record(record_name):
    if not os.path.exists(f"archives/{record_name}.txt"):
        print(f"Invalid record name! Record with '{record_name}' doesn't exist.")
        return
    file = open(f"archives/{record_name}.txt", "r")
    content = file.readlines()
    for line in content:
        print(line)
    file.flush()
    file.close()


def delete_record(record_name):
    if not os.path.exists(f"archives/{record_name}.txt"):
        print(f"Invalid record name! Record with '{record_name}' doesn't exist.")
        return
    os.remove(f"archives/{record_name}.txt")
    print(f"Record '{record_name}' successfully deleted.")
