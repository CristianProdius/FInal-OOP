import os
from datetime import datetime

class Document:
    folder_path = "/home/cristian/Documents/University/OOP/FInal-OOP"

    def __init__(self, file_name):
        self.file_name = file_name
        self.creation_date = self.get_creation_time()
        self.update_date = self.get_last_update_time()

    def get_file_name(self):
        return os.path.splitext(self.file_name)[0]

    def get_file_extension(self):
        return os.path.splitext(self.file_name)[1][1:]

    def get_creation_time(self):
        return datetime.fromtimestamp(os.path.getctime(self.get_folder_path()))

    def get_last_update_time(self):
        return datetime.fromtimestamp(os.path.getmtime(self.get_folder_path()))

    def get_folder_path(self):
        return os.path.join(self.folder_path, self.file_name)

    def get_basic_info(self):
        return f"File name: {self.get_file_name()}\n" \
               f"File extension: {self.get_file_extension()}\n" \
               f"Date created: {self.get_creation_time()}\n" \
               f"Date last update: {self.get_last_update_time()}"