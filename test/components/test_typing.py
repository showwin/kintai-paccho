import unittest

from components.typing import SlackRequest


class TestSlackRequest(unittest.TestCase):
    def test_build_from_message(self):
        params = {
            'channel': 'dummy_channel_id',
            'user': 'dummy_user_id',
            'text': 'dummy_text'
        }

        slack_request = SlackRequest.build_from_message(params=params)

        self.assertEqual(slack_request.channel_id, params["channel"])
        self.assertEqual(slack_request.user_id, params["user"])
        self.assertEqual(slack_request.text, params["text"])

    def test_build_from_command(self):
        params = {
            'channel_id': 'dummy_channel_id',
            'user_id': 'dummy_user_id',
            'text': 'dummy_text'
        }

        slack_request = SlackRequest.build_from_command(params=params)

        self.assertEqual(slack_request.channel_id, params["channel_id"])
        self.assertEqual(slack_request.user_id, params["user_id"])
        self.assertEqual(slack_request.text, params["text"])
