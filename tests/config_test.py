import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from pytils.config import Configuration


class ConfigurationTest(unittest.TestCase):

    @patch('pytils.config.path.exists')
    @patch('builtins.open', mock_open(read_data='name: Nobody'))
    def test_init_file_exists(self, mock_exists):
        mock_exists.return_value = True
        config = Config.init()
        self.assertEqual(config.name, 'Nobody')

    @patch('pytils.config.path.exists')
    @patch('builtins.open', new_callable=StringIO)
    @unittest.skip("reason for skipping")
    def test_init_file_dont_exists(self, mock_open, mock_exists):
        mock_exists.return_value = False
        # mock_open.return_value.__enter__ = StringIO('')
        config = Config.init()
        self.assertEqual(config.name, 'Nobody')


class Config(Configuration):
    name: str = 'Someone'
    age: int = 42
