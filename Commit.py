from datetime import datetime
import os
from Document import Document

class Commit:
    def __init__(self, commit_time, files):
        self.commit_time = commit_time
        self.files = files

    def __str__(self):
        return "Created snapshot at: " + str(self.commit_time) + "\n" + self.print_files()

    def print_files(self):
        return "\n".join(self.files)

    @staticmethod
    def make_commit():
        commit = Commit(datetime.now(), os.listdir(Document.folder_path))
        with open("commit.txt", "w") as writer:
            writer.write(str(commit.commit_time))
            writer.write("\n")
            for file in commit.files:
                writer.write(file)
                writer.write("\n")

    @staticmethod
    def get_latest_commit():
        latest_commit = None
        try:
            with open("commit.txt", "r") as reader:
                lines = reader.readlines()
                commit_time = datetime.strptime(lines[0].strip(), "%Y-%m-%d %H:%M:%S.%f")
                files = [line.strip() for line in lines[1:]]
                latest_commit = Commit(commit_time, files)
        except Exception as e:
            print(e)
        return latest_commit