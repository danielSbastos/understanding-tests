import os
from doubles import allow, expect
from understanding_tests.file_actions import FileActions


def test_write_file():
    file = FileActions('example1.txt')

    expect(file).open_file
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])

def test_write_and_remove_file():
    file = FileActions('example1.txt')

    expect(file).open_file
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])
    allow(file).file_exists.with_no_args().and_return(True)
    expect(os).remove.with_args(file.file_name)

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.try_to_remove_file()

def test_write_and_dont_remove_file():
    file = FileActions('example1.txt')

    expect(file).open_file
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])
    allow(file).file_exists.with_no_args().and_return(False)

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.try_to_remove_file()
