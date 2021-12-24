import json
import os


class Employee():
    DATA_DIR = os.path.join(os.environ['HOME'], '.kintai_paccho')
    DATA_JSON = os.path.join(DATA_DIR, 'employee_data.json')
    EMPLOYEE_DATA_CACHE = {}

    @classmethod
    def create(cls, user_id, key):
        user_data = cls._read()
        user_data[user_id] = key  # KOT の従業員の EmployeeKey
        cls._write(user_data)
        cls.EMPLOYEE_DATA_CACHE = {}

    @classmethod
    def get_key(cls, user_id):
        if user_id in cls.EMPLOYEE_DATA_CACHE:
            return cls.EMPLOYEE_DATA_CACHE[user_id]

        cls.EMPLOYEE_DATA_CACHE = cls._read()
        if user_id in cls.EMPLOYEE_DATA_CACHE:
            return cls.EMPLOYEE_DATA_CACHE[user_id]
        return None

    @classmethod
    def _write(cls, data):
        if not os.path.exists(cls.DATA_DIR):
            os.makedirs(cls.DATA_DIR, exist_ok=True)
        f = open(cls.DATA_JSON, 'w')
        f.write(json.dumps(data))
        f.close()

    @classmethod
    def _read(cls):
        if not os.path.exists(cls.DATA_JSON):
            cls._write({})
        f = open(cls.DATA_JSON, 'r')
        json_str = f.read()
        f.close()
        return json.loads(json_str)
