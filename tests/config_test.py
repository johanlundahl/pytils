import unittest
from dataclasses import dataclass
from unittest.mock import patch, mock_open
from pytils.config import Configuration
from testfixtures import TempDirectory


class ConfigurationTest(unittest.TestCase):

    def tearDown(self):
        TempDirectory.cleanup_all()

    @patch('pytils.config.path.exists')
    @patch('builtins.open', mock_open(read_data='name: Nobody'))
    def test_init_file_exists(self, mock_exists):
        mock_exists.return_value = True
        config = Config.init()
        self.assertEqual(config.name, 'Nobody')

    @patch('pytils.config.path.exists')
    def test_init_file_dont_exists(self, mock_exists):
        with TempDirectory() as dir:
            mock_exists.return_value = False
            file = 'testing.yaml'
            config = Config.init(f'{dir.path}/{file}')
            self.assertEqual(config.name, 'Someone')

    def test_save(self):
        with TempDirectory() as dir:
            file = 'tmp.yaml'
            dir.write(file, b'yada')
            config = Config()
            config.save(f'{dir.path}/{file}')
            result = dir.read(file).decode('utf-8')
            self.assertTrue('Someone' in result)


@dataclass
class Config(Configuration):
    name: str = 'Someone'
    age: int = 42
