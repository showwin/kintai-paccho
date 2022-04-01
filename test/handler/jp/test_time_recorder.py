import unittest
from unittest import mock
from unittest.mock import MagicMock

from components.requester import KOTException
from components.typing import SlackRequest
from components.usecase import RecordType
from handler.jp.time_recorder import record_clock_in, record_clock_out, record_start_break, record_end_break


class TestTimeRecorder(unittest.TestCase):
    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_clock_in(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_clock_in(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        mocked_record_time_call_args, _ = mocked_record_time.call_args
        self.assertEqual(mocked_record_time_call_args[0], RecordType.CLOCK_IN)
        self.assertEqual(mocked_record_time_call_args[1], 'dummy-employee-key')

        self.assertEqual(mocked_response_kot_error.call_count, 0)

        self.assertEqual(say.call_count, 1)
        say_call_args, _ = say.call_args
        self.assertIn('おはー', say_call_args[0])

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value=None)
    def test_record_clock_in__employee_not_found(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_clock_in(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 0)

        self.assertEqual(mocked_response_kot_error.call_count, 0)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time", side_effect=KOTException)
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_clock_in__error(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_clock_in(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        self.assertEqual(mocked_response_kot_error.call_count, 1)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_clock_out(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_clock_out(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        mocked_record_time_call_args, _ = mocked_record_time.call_args
        self.assertEqual(mocked_record_time_call_args[0], RecordType.CLOCK_OUT)
        self.assertEqual(mocked_record_time_call_args[1], 'dummy-employee-key')

        self.assertEqual(mocked_response_kot_error.call_count, 0)

        self.assertEqual(say.call_count, 1)
        say_call_args, _ = say.call_args
        self.assertIn('おつー', say_call_args[0])

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value=None)
    def test_record_clock_out__employee_not_found(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_clock_out(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 0)

        self.assertEqual(mocked_response_kot_error.call_count, 0)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time", side_effect=KOTException)
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_clock_out__error(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_clock_out(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        self.assertEqual(mocked_response_kot_error.call_count, 1)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_start_break(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_start_break(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        mocked_record_time_call_args, _ = mocked_record_time.call_args
        self.assertEqual(mocked_record_time_call_args[0], RecordType.START_BREAK)
        self.assertEqual(mocked_record_time_call_args[1], 'dummy-employee-key')

        self.assertEqual(mocked_response_kot_error.call_count, 0)

        self.assertEqual(say.call_count, 1)
        say_call_args, _ = say.call_args
        self.assertIn('ゆっくり休んでね', say_call_args[0])

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value=None)
    def test_record_start_break__employee_not_found(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_start_break(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 0)

        self.assertEqual(mocked_response_kot_error.call_count, 0)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time", side_effect=KOTException)
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_start_break__error(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_start_break(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        self.assertEqual(mocked_response_kot_error.call_count, 1)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_end_break(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_end_break(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        mocked_record_time_call_args, _ = mocked_record_time.call_args
        self.assertEqual(mocked_record_time_call_args[0], RecordType.END_BREAK)
        self.assertEqual(mocked_record_time_call_args[1], 'dummy-employee-key')

        self.assertEqual(mocked_response_kot_error.call_count, 0)

        self.assertEqual(say.call_count, 1)
        say_call_args, _ = say.call_args
        self.assertIn('がんばっていこ', say_call_args[0])

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time")
    @mock.patch("components.repo.Employee.get_key", return_value=None)
    def test_record_end_break__employee_not_found(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_end_break(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 0)

        self.assertEqual(mocked_response_kot_error.call_count, 0)

    @mock.patch("handler.jp.time_recorder.response_kot_error")
    @mock.patch("handler.jp.time_recorder.record_time", side_effect=KOTException)
    @mock.patch("components.repo.Employee.get_key", return_value='dummy-employee-key')
    def test_record_end_break__error(
            self,
            mocked_get_key,
            mocked_record_time,
            mocked_response_kot_error
    ):
        say = MagicMock()
        request = SlackRequest(
            channel_id='dummy-channel-id',
            user_id='dummy-user-id',
            text='dummy-text'
        )

        record_end_break(say=say, request=request)

        self.assertEqual(mocked_get_key.call_count, 1)

        self.assertEqual(mocked_record_time.call_count, 1)

        self.assertEqual(mocked_response_kot_error.call_count, 1)
