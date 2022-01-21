import json
import os


class Employee():
    DATA_DIR = os.path.join(os.environ['HOME'], '.kintai_paccho')
    DATA_JSON = os.path.join(DATA_DIR, 'employee_data.json')
    CONFIG_JSON = os.path.join(DATA_DIR, 'employee_config.json')
    EMPLOYEE_DATA_CACHE = {}
    """
    format of data files:
    DATA_JSON = {  # data must be existed if the user exists
        "user_id_1": "EmployeeKey1 of KOT",
        "user_id_2": "EmployeeKey2 of KOT"
    }
    CONFIG_JSON = {  # config value can be null for existing user
        "user_id_1": {
            "timezone": "+09:00",
        },
        "user_id_2": {
            "timezone": "-02:00",
        }
    }
    """

    @classmethod
    def create(cls, user_id, key):
        user_data = cls._read()
        user_data[user_id] = key  # KOT の従業員の EmployeeKey
        cls._write(user_data)

    @classmethod
    def get_key(cls, user_id):
        # if cache is not created
        if not cls.EMPLOYEE_DATA_CACHE:
            cls.EMPLOYEE_DATA_CACHE = cls._read()

        return cls.EMPLOYEE_DATA_CACHE.get(user_id)

    @classmethod
    def update_timezone(cls, user_id, timezone):
        config_data = cls._read_config()
        if user_id not in config_data:
            config_data[user_id] = {}
        config_data[user_id]['timezone'] = timezone
        cls._write_config(config_data)

    @classmethod
    def get_timezone(cls, user_id):
        # if cache is not created
        if not cls.CONFIG_DATA_CACHE:
            cls.CONFIG_DATA_CACHE = cls._read_config()

        user_config = cls.CONFIG_DATA_CACHE.get(user_id)
        if user_config:
            return user_config.get('timezone')
        return None

    @classmethod
    def _write(cls, data):
        if not os.path.exists(cls.DATA_DIR):
            os.makedirs(cls.DATA_DIR, exist_ok=True)
        f = open(cls.DATA_JSON, 'w')
        f.write(json.dumps(data))
        f.close()
        cls._refresh_cache()

    @classmethod
    def _read(cls):
        if not os.path.exists(cls.DATA_JSON):
            cls._write({})
        f = open(cls.DATA_JSON, 'r')
        json_str = f.read()
        f.close()
        return json.loads(json_str)

    @classmethod
    def _write_config(cls, data):
        if not os.path.exists(cls.DATA_DIR):
            os.makedirs(cls.DATA_DIR, exist_ok=True)
        f = open(cls.CONFIG_JSON, 'w')
        f.write(json.dumps(data))
        f.close()
        cls._refresh_cache()

    @classmethod
    def _read_config(cls):
        if not os.path.exists(cls.CONFIG_JSON):
            cls._write_config({})
        f = open(cls.CONFIG_JSON, 'r')
        json_str = f.read()
        f.close()
        return json.loads(json_str)

    @classmethod
    def _refresh_cache(cls):
        """
        refresh_cache is called when a record is created or updated
        since these records are read intensive.
        """
        cls.EMPLOYEE_DATA_CACHE = cls._read()
        cls.CONFIG_DATA_CACHE = cls._read_config()
