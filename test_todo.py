import os

class FileActions():

    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        file = open(self.file_name, "w+")
        self.file = file

    def write_file(self, texts):
        for text in texts:
            self.file.write(text + "\n")
        self.file.close()

    def try_to_remove_file(self):
        if os.path.isfile(self.file_name):
            os.remove(self.file_name)


from doubles import allow, expect

def test_write_file():
    file = FileActions('example1.txt')

    expect(file).open_file
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
