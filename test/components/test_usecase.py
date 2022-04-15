import json
import unittest
from datetime import datetime
from unittest import mock

from freezegun import freeze_time

from components.usecase import RecordType, _get_working_date, record_time, register_user


class TestUseCase(unittest.TestCase):
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    @mock.patch("components.repo.Employee.create")
    @mock.patch("components.requester.KOTRequester.get")
    def test_register_user(self, mocked_get, mocked_create):
        user = "dummy-user"
        kot_user_code = "dummy-kot-user-code"
        employee_key = "dummy-employee-key"
        last_name = "dummy-last-name"
        first_name = "dummy-first-name"

        expect_resp_json = {"last_name": last_name, "first_name": first_name}

        mocked_get.return_value = {"key": employee_key, "lastName": last_name, "firstName": first_name}

        resp_json = register_user(user=user, kot_user_code=kot_user_code)

        self.assertEqual(mocked_get.call_count, 1)
        self.assertDictEqual(expect_resp_json, resp_json)

        mocked_get_args, _ = mocked_get.call_args

        self.assertEqual(mocked_get_args[0], f"/employees/{kot_user_code}")

        self.assertEqual(mocked_create.call_count, 1)

        mocked_create_args, _ = mocked_create.call_args

        self.assertEqual(mocked_create_args[0], user)
        self.assertEqual(mocked_create_args[1], employee_key)

    @mock.patch("components.requester.KOTRequester.post")
    def test_record_time(self, mocked_post):
        record_type = RecordType.CLOCK_IN
        employee_key = "dummy-employee-key"

        current_time = datetime.strptime("2030-04-01 12:00:00", self.DATE_FORMAT)

        with freeze_time(current_time):
            record_time(record_type=record_type, employee_key=employee_key)

            self.assertEqual(mocked_post.call_count, 1)

            mocked_post_args, _ = mocked_post.call_args

            self.assertEqual(mocked_post_args[0], f"/daily-workings/timerecord/{employee_key}")
            self.assertDictEqual(
                json.loads(mocked_post_args[1]),
                {
                    "time": current_time.strftime("%Y-%m-%dT%H:%M:%S+09:00"),
                    "date": current_time.strftime("%Y-%m-%d"),
                    "code": record_type.value,
                },
            )

    def test_get_working_date(self):
        patterns = [
            (datetime.strptime("2025-06-30 23:59:59", self.DATE_FORMAT), "2025-06-30"),
            (datetime.strptime("2025-07-01 00:00:00", self.DATE_FORMAT), "2025-06-30"),
            (datetime.strptime("2025-07-01 04:59:59", self.DATE_FORMAT), "2025-06-30"),
            (datetime.strptime("2025-07-01 05:00:00", self.DATE_FORMAT), "2025-07-01"),
            (datetime.strptime("2025-07-01 23:59:59", self.DATE_FORMAT), "2025-07-01"),
        ]

        for current_time, working_date in patterns:
            with self.subTest(msg=f"current_time={current_time}, working_date={working_date}"):
                with freeze_time(current_time):
                    self.assertEqual(_get_working_date(), working_date)
