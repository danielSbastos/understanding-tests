import os

# TEST

class FileActions():

    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        file = open(self.file_name, "w+")
        self.file = file

    def write_file(self, texts):
        for text in texts:
            self.file.write(text + "\n")

    def close_file(self):
        self.file.close()

    def try_to_remove_file(self):
        if self.file_exists():
            os.remove(self.file_name)

    def file_exists(self):
        return os.path.isfile(self.file_name)
