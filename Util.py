import os
from Document import Document

class Util:

    @staticmethod
    def get_file_names():
        file_names = []
        if os.path.isdir(Document.folder_path):
            for file in os.listdir(Document.folder_path):
                if os.path.isfile(os.path.join(Document.folder_path, file)):
                    file_names.append(file)
        return file_names

    @staticmethod
    def get_files():
        files = []
        if os.path.isdir(Document.folder_path):
            for file in os.listdir(Document.folder_path):
                if os.path.isfile(os.path.join(Document.folder_path, file)):
                    files.append(os.path.join(Document.folder_path, file))
        return files