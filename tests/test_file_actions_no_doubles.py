import os
import unittest
import shutil
import tempfile

from understanding_tests.file_actions import FileActions


class FileActionsTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_write_file(self):
        file = FileActions('example1.txt')
        self.open_write_close_file(file, ['Oi', 'Me chamo Daniel'])

        with open(file.file_name, 'r') as file:
            self.assertEqual(file.read(), 'Oi\nMe chamo Daniel\n')

    def test_write_remove_file(self):
        file = FileActions('example1.txt')
        self.open_write_close_file(file, ['Oi', 'Me chamo Daniel'])
        file.try_to_remove_file()

        with self.assertRaises(FileNotFoundError) as err:
            with open(file.file_name, 'r'):
                self.assertIn('No such file or directory:', err)

    @staticmethod
    def open_write_close_file(file, texts):
        file.open_file()
        file.write_file(texts)
        file.close_file()
