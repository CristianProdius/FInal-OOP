from datetime import datetime
import os
from Commit import Commit
from Document import Document

class StatusCommand:
    @staticmethod
    def invoke():
        last_commit = Commit.get_latest_commit()
        if last_commit is None:
            print("No commits found.")
            return
        last_commit_time = last_commit.commit_time
        last_commit_files = last_commit.files

        current_files = os.listdir(Document.folder_path)
        current_files = [os.path.join(Document.folder_path, file) for file in current_files]

        no_change_files = set()
        modified_files = set()
        deleted_files = set(last_commit_files)
        created_files = set()

        for file in current_files:
            if os.path.basename(file) in last_commit_files:
                deleted_files.remove(os.path.basename(file))

                last_modified_time = datetime.fromtimestamp(os.path.getmtime(file))

                if last_modified_time > last_commit_time:
                    modified_files.add(file)
                else:
                    no_change_files.add(file)
            else:
                created_files.add(file)

        status_message = f"Last commit made at: {last_commit_time}\nFrom that time there are the following changes:\n"

        status_message += StatusCommand.add_file_info(no_change_files, "No changes")
        status_message += StatusCommand.add_file_info(modified_files, "Modified")
        status_message += StatusCommand.add_file_info(created_files, "Created")

        if deleted_files:
            status_message += "Deleted files:\n"
            for file in deleted_files:
                status_message += f"{file}\n"

        print(status_message)

    @staticmethod
    def add_file_info(files, category):
        if files:
            file_info = f"{category} files:\n"
            for file in files:
                file_info += f"{os.path.basename(file)}\n"
            return file_info
        return ""