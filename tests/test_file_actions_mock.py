from unittest import mock
from understanding_tests.file_actions import FileActions


@mock.patch('understanding_tests.file_actions.FileActions.write_file')
@mock.patch('builtins.open')
def test_write_file(mock_open, mock_write):
    file = FileActions('example1.txt')
    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])

    mock_open.assert_called_with('example1.txt', 'w+')
    mock_write.assert_called_with(['Oi', 'Me chamo Daniel'])


@mock.patch('understanding_tests.file_actions.FileActions.write_file')
@mock.patch('understanding_tests.file_actions.os')
@mock.patch('builtins.open')
def test_write_and_delete_file(mock_open, mock_os, mock_write):
    file = FileActions('example1.txt')
    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.try_to_remove_file()

    mock_open.assert_called_with('example1.txt', 'w+')
    mock_write.assert_called_with(['Oi', 'Me chamo Daniel'])
    mock_os.remove.assert_called_with('example1.txt')


@mock.patch('understanding_tests.file_actions.FileActions.write_file')
@mock.patch('understanding_tests.file_actions.os')
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
