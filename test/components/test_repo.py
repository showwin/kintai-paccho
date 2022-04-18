import json
import random
import shutil
import string
import tempfile
import unittest
from os import path
from unittest import mock

from components.repo import Employee


def _random_string(n):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.mkdtemp()
        self.temp_json = path.join(path.join(self.temp_dir, "employee_data.json"))

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_create(self):
        user_id_1 = _random_string(n=10)
        user_id_2 = _random_string(n=10)
        user_key_1 = _random_string(n=20)
        user_key_2 = _random_string(n=20)

        with mock.patch.multiple(
            "components.repo.Employee",
            DATA_DIR=self.temp_dir,
            DATA_JSON=self.temp_json,
            EMPLOYEE_DATA_CACHE={"cached_key": "cached_value"},
        ):
            Employee.create(user_id=user_id_1, key=user_key_1)
            self.assertDictEqual(Employee.EMPLOYEE_DATA_CACHE, {})

            Employee.create(user_id=user_id_2, key=user_key_2)
            self.assertDictEqual(Employee.EMPLOYEE_DATA_CACHE, {})

            with open(self.temp_json) as f:
                self.assertDictEqual(json.loads(f.read()), {user_id_1: user_key_1, user_id_2: user_key_2})

    def test_get_key(self):
        user_id_1 = _random_string(n=10)
        user_key_1 = _random_string(n=20)

        with open(self.temp_json, "w") as f:
            f.write(json.dumps({user_id_1: user_key_1}))

        with mock.patch.multiple(
            "components.repo.Employee", DATA_DIR=self.temp_dir, DATA_JSON=self.temp_json, EMPLOYEE_DATA_CACHE={}
        ):
            self.assertIsNone(Employee.get_key("none_key"))

            self.assertDictEqual(Employee.EMPLOYEE_DATA_CACHE, {user_id_1: user_key_1})

            self.assertEqual(Employee.get_key(user_id_1), user_key_1)
