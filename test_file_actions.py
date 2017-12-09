import os

class FileActions():

    def __init__(self, file):
        self.file = file

    def write_file(self, texts):
        file = open(self.file, "w+")
        for text in texts:
            file.write(text + "\n")
        file.close()

    def try_to_remove_file(self):
        if os.path.isfile(self.file):
            os.remove(self.file)


# Test

from unittest import mock

@mock.patch('builtins.open')
def test_write_file(mock_open):
    file = FileActions('example1.txt').write_file(['Oi', 'Me chamo Daniel'])

    mock_open.assert_called_with('example1.txt', "w+")
    assert 'example1.txt' not in os.listdir(os.getcwd())


@mock.patch('builtins.open')
@mock.patch('os.path')
@mock.patch('os.remove')
def test_write_and_remove_file(mock_rm, mock_path, mock_open):
    file = FileActions('example1.txt')
    file.write_file(['Oi', 'Me chamo Daniel'])

    mock_path.isfile.return_value = False

    file.try_to_remove_file()

    mock_path.isfile.assert_called_with(file.file)
    mock_rm.assert_not_called()
