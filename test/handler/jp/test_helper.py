import unittest
from unittest.mock import MagicMock

from components.requester import KOTException
from handler.jp.helper import response_configuration_help, response_kot_error


class TestHelper(unittest.TestCase):
    def test_response_configuration_help(self):
        say = MagicMock()

        response_configuration_help(say=say)

        self.assertEqual(say.call_count, 1)

        args, _ = say.call_args

        self.assertIn('kintai-paccho', args[0])
        self.assertIn('/employee-code', args[0])
        self.assertIn('入力するぱっちょ！', args[0])

    def test_response_kot_error(self):
        say = MagicMock()

        error_message = 'dummy error message'

        response_kot_error(say=say, e=KOTException(error_message))

        self.assertEqual(say.call_count, 2)

        call_args_list = say.call_args_list

        self.assertIn('返ってきたぱっちょ！', call_args_list[0][0][0])
        self.assertEqual(error_message, call_args_list[1][0][0])
