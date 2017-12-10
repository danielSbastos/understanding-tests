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



# Test

from unittest import mock

@mock.patch('test_file_actions.FileActions.write_file')
@mock.patch('builtins.open')
def test_write_file(mock_open, mock_write):
    file = FileActions('example1.txt')
    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])

    mock_open.assert_called_with('example1.txt', 'w+')
    mock_write.assert_called_with(['Oi', 'Me chamo Daniel'])


@mock.patch('test_file_actions.FileActions.write_file')
@mock.patch('test_file_actions.os')
@mock.patch('builtins.open')
def test_write_and_delete_file(mock_open, mock_os, mock_write):
    file = FileActions('example1.txt')
    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.try_to_remove_file()

    mock_open.assert_called_with('example1.txt', 'w+')
    mock_write.assert_called_with(['Oi', 'Me chamo Daniel'])
    mock_os.remove.assert_called_with('example1.txt')


@mock.patch('test_file_actions.FileActions.write_file')
@mock.patch('test_file_actions.os')
@mock.patch('builtins.open')
def test_write_and_dont_delete_file(mock_open, mock_os, mock_write):
    file = FileActions('example1.txt')
    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])

    mock_os.path.isfile.return_value = False

    file.try_to_remove_file()

    mock_open.assert_called_with('example1.txt', 'w+')
    mock_write.assert_called_with(['Oi', 'Me chamo Daniel'])
    mock_os.remove.assert_not_called()
