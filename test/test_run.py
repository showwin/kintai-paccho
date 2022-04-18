import datetime
import json
import unittest
import urllib.parse
import uuid
from test.mock_web_api_server import cleanup_mock_web_api_server, setup_mock_web_api_server
from unittest import mock

from slack_bolt import BoltRequest
from slack_sdk.signature import SignatureVerifier

from run import create_app


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        setup_mock_web_api_server(self)

    def tearDown(self) -> None:
        cleanup_mock_web_api_server(self)

    @mock.patch("run.record_clock_in")
    def test_app__message__record_clock_in(self, mocked_record_clock_in):
        app = create_app(is_test=True)

        response = app.dispatch(_create_message_event(text="おはー"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_clock_in.call_count, 1)

    @mock.patch("run.record_clock_out")
    def test_app__message__record_clock_out(self, mocked_record_clock_out):
        app = create_app(is_test=True)

        response = app.dispatch(_create_message_event(text="おつー"))
        self.assertEqual(response.status, 200)

        self.assertEqual(mocked_record_clock_out.call_count, 1)

    @mock.patch("run.record_start_break")
    def test_app__message__record_start_break(self, mocked_record_start_break):
        app = create_app(is_test=True)

        response = app.dispatch(_create_message_event(text="休憩開始"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_start_break.call_count, 1)

    @mock.patch("run.record_end_break")
    def test_app__message__record_end_break(self, mocked_record_end_break):
        app = create_app(is_test=True)

        response = app.dispatch(_create_message_event(text="休憩終了"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_end_break.call_count, 1)

    @mock.patch("run.record_clock_in")
    def test_app__command__record_clock_in(self, mocked_record_clock_in):
        app = create_app(is_test=True)

        response = app.dispatch(_create_command_event(command="/clock-in"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_clock_in.call_count, 1)

    @mock.patch("run.record_clock_out")
    def test_app__command__record_clock_out(self, mocked_record_clock_out):
        app = create_app(is_test=True)

        response = app.dispatch(_create_command_event(command="/clock-out"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_clock_out.call_count, 1)

    @mock.patch("run.record_start_break")
    def test_app__command__record_start_break(self, mocked_record_start_break):
        app = create_app(is_test=True)

        response = app.dispatch(_create_command_event(command="/start-break"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_start_break.call_count, 1)

    @mock.patch("run.record_end_break")
    def test_app__command__record_end_break(self, mocked_record_end_break):
        app = create_app(is_test=True)

        response = app.dispatch(_create_command_event(command="/end-break"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_record_end_break.call_count, 1)

    @mock.patch("run.register_employee_code")
    def test_app__command__register_employee_code(self, mocked_register_employee_code):
        app = create_app(is_test=True)

        response = app.dispatch(_create_command_event(command="/employee-code", text="1234"))

        self.assertEqual(response.status, 200)
        self.assertEqual(mocked_register_employee_code.call_count, 1)


def _create_message_event(text: str):
    now = datetime.datetime.now()
    ts = int(now.timestamp())
    client_msg_id = str(uuid.uuid4())
    body = {
        "token": "verification_token",
        "team_id": "T111",
        "enterprise_id": "E111",
        "api_app_id": "A111",
        "event": {
            "client_msg_id": client_msg_id,
            "type": "message",
            "text": text,
            "user": "W222",
            "ts": f"{ts}.{now.strftime('%f')}",
            "team": "T111",
            "channel": "C111",
            "event_ts": f"{ts}.{now.strftime('%f')}",
        },
        "type": "event_callback",
        "event_id": "Ev111",
        "event_time": ts,
        "authed_users": ["W111"],
    }

    return BoltRequest(body=body, mode="socket_mode")


def _create_command_event(command: str, text: str = "Hi!"):
    signature_verifier = SignatureVerifier(signing_secret="secret")

    now = datetime.datetime.now()
    ts = int(now.timestamp())

    body = json.dumps(
        "token=verification_token"
        "&team_id=T111"
        "&team_domain=test-domain"
        "&channel_id=C111"
        "&channel_name=random"
        "&user_id=W111"
        "&user_name=primary-owner"
        f"&command={urllib.parse.quote(command)}"
        f"&text={urllib.parse.quote(text)}"
        "&enterprise_id=E111"
        "&enterprise_name=Org+Name"
        "&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT111%2F111%2Fxxxxx"
        "&trigger_id=111.111.xxx"
    )

    signature = signature_verifier.generate_signature(timestamp=str(ts), body=body)

    headers = {
        "content-type": ["application/x-www-form-urlencoded"],
        "x-slack-signature": [signature],
        "x-slack-request-timestamp": [str(ts)],
    }

    return BoltRequest(body=body, headers=headers)
