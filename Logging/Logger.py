import os
import datetime
from getpass import getuser

class Logger:
    def __init__(self, inputed_file_name="app.log"):
        self.file_name = inputed_file_name
        self.log_date_format = "[%Y-%m-%d %H:%M:%S.%f]"

    def log(self, interaction_message):
        log_message = self.generate_unique_identifier() + " " + self.get_time_in_log_format() + " " + interaction_message
        self.write_log_to_file(log_message)

    def get_time_in_log_format(self):
        return datetime.datetime.now().strftime(self.log_date_format)

    def generate_unique_identifier(self):
        return getuser() + "/" + os.name

    def write_log_to_file(self, content):
        try:
            with open(self.file_name, 'a') as file:
                file.write(content + "\n")
        except IOError:
            print("An error occurred while writing to the log file.")