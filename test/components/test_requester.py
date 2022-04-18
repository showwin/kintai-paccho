import json
import unittest
from unittest import mock
from unittest.mock import MagicMock

from components.requester import KOTException, KOTRequester


class TestKOTRequester(unittest.TestCase):
    BASE_URL = "https://api.kingtime.jp/v1.0"

    @mock.patch("requests.get")
    def test_get(self, mocked_get):
        expect_resp_json = {"lastName": "last_name", "firstName": "first_name"}
        expect_path = "/test-path"

        mocked_response = MagicMock()
        mocked_response.text = json.dumps(expect_resp_json)
        mocked_get.return_value = mocked_response

        requester = KOTRequester()
        resp_json = requester.get(uri=expect_path)

        self.assertEqual(mocked_get.call_count, 1)

        args, kwargs = mocked_get.call_args
        self.assertEqual(args[0], f"{self.BASE_URL}{expect_path}")

        self.assertDictEqual(resp_json, expect_resp_json)

    @mock.patch("requests.get")
    def test_get__error(self, mocked_get):
        expect_json = {"errors": [{"message": "message1"}, {"message": "message2"}]}
        expect_path = "/error-path"

        mocked_response = MagicMock()
        mocked_response.text = json.dumps(expect_json)
        mocked_get.return_value = mocked_response

        requester = KOTRequester()
        with self.assertRaises(KOTException, msg="message1"):
            requester.get(uri=expect_path)

        self.assertEqual(mocked_get.call_count, 1)

    @mock.patch("requests.post")
    def test_post(self, mocked_post):
        expect_req_json = {"req_str": "str", "req_int": 10}
        expect_resp_json = {}
        expect_path = "/test-path"

        mocked_response = MagicMock()
        mocked_response.text = json.dumps(expect_resp_json)
        mocked_post.return_value = mocked_response

        requester = KOTRequester()
        resp_json = requester.post(uri=expect_path, payload=expect_req_json)

        self.assertEqual(mocked_post.call_count, 1)

        args, kwargs = mocked_post.call_args
        self.assertEqual(args[0], f"{self.BASE_URL}{expect_path}")

        self.assertDictEqual(kwargs["data"], expect_req_json)

        self.assertDictEqual(resp_json, expect_resp_json)

    @mock.patch("requests.post")
    def test_post__error(self, mocked_post):
        expect_json = {"errors": [{"message": "message10"}, {"message": "message20"}]}
        expect_path = "/error-path"

        mocked_response = MagicMock()
        mocked_response.text = json.dumps(expect_json)
        mocked_post.return_value = mocked_response

        requester = KOTRequester()
        with self.assertRaises(KOTException, msg="message10"):
            requester.post(uri=expect_path, payload={})

        self.assertEqual(mocked_post.call_count, 1)

    @mock.patch("requests.put")
    def test_put(self, mocked_put):
        expect_req_json = {"req_bool": True, "req_none": None}
        expect_resp_json = {}
        expect_path = "/test-path"

        mocked_response = MagicMock()
        mocked_response.text = json.dumps(expect_resp_json)
        mocked_put.return_value = mocked_response

        requester = KOTRequester()
        resp_json = requester.put(uri=expect_path, payload=expect_req_json)

        self.assertEqual(mocked_put.call_count, 1)

        args, kwargs = mocked_put.call_args
        self.assertEqual(args[0], f"{self.BASE_URL}{expect_path}")

        self.assertDictEqual(kwargs["json"], expect_req_json)

        self.assertDictEqual(resp_json, expect_resp_json)

    @mock.patch("requests.put")
    def test_put__error(self, mocked_put):
        expect_json = {"errors": [{"message": "message100"}, {"message": "message200"}]}
        expect_path = "/error-path"

        mocked_response = MagicMock()
        mocked_response.text = json.dumps(expect_json)
        mocked_put.return_value = mocked_response

        requester = KOTRequester()
        with self.assertRaises(KOTException, msg="message100"):
            requester.put(uri=expect_path, payload={})

        self.assertEqual(mocked_put.call_count, 1)
