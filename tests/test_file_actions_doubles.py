import os
from doubles import allow, expect
from understanding_tests.file_actions import FileActions


def test_write_file():
    file = FileActions('example1.txt')

    expect(file).open_file.with_no_args()
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])
    expect(file).close_file.with_no_args()

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.close_file()


def test_write_and_remove_file():
    file = FileActions('example1.txt')

    expect(file).open_file.with_no_args()
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])
    expect(file).close_file.with_no_args()
    allow(file).file_exists.with_no_args().and_return(True)
    expect(os).remove.with_args(file.file_name)

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.close_file()
    file.try_to_remove_file()


def test_write_and_dont_remove_file():
    file = FileActions('example1.txt')

    expect(file).open_file.with_no_args()
    expect(file).write_file.with_args(['Oi', 'Me chamo Daniel'])
    expect(file).close_file.with_no_args()
    allow(file).file_exists.with_no_args().and_return(False)

    file.open_file()
    file.write_file(['Oi', 'Me chamo Daniel'])
    file.close_file()
    file.try_to_remove_file()
