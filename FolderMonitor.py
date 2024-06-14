import os
import time
import threading
from Document import Document

class FolderMonitor:
    FOLDER_PATH = Document.folder_path

    def __init__(self):
        self.current_files = set()

    def start_file_monitoring(self):
        self.current_files = self.list_files()

        def monitor():
            while True:
                updated_files = self.list_files()

                for file in updated_files:
                    if file not in self.current_files:
                        print(f"File added: {file}")

                for file in self.current_files:
                    if file not in updated_files:
                        print(f"File deleted: {file}")

                for file in updated_files:
                    current_file = os.path.join(self.FOLDER_PATH, file)
                    if os.path.exists(current_file) and time.time() - os.path.getmtime(current_file) <= 5:
                        print(f"File modified: {file}")

                self.current_files = updated_files
                time.sleep(5)

        threading.Thread(target=monitor).start()

    def list_files(self):
        return set(os.listdir(self.FOLDER_PATH))