import logging
import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from components.typing import SlackRequest
from handler.jp.configuration import register_employee_code
from handler.jp.extra import be_shy, how_to_use, i_am_not_alexa, i_am_not_siri
from handler.jp.time_recorder import record_clock_in, record_clock_out, record_end_break, record_start_break


def create_app(is_test=False):
    if is_test:
        client = WebClient(token="xoxb-valid", base_url="http://localhost:8888")
        app = App(client=client, signing_secret="secret")
    else:
        token = os.environ["SLACK_BOT_TOKEN"]
        app = App(token=token)

    # record timestamp
    @app.message(re.compile("^おはー[！？!?]*$"))
    def record_clock_in_listener(message, say):
        record_clock_in(say, SlackRequest.build_from_message(message))

    @app.command("/clock-in")
    def record_clock_in_command(ack, command, say):
        ack()
        record_clock_in(say, SlackRequest.build_from_command(command))

    @app.message(re.compile("^(店じまい|おつー)[！？!?]*$"))
    def record_clock_out_listener(message, say):
        record_clock_out(say, SlackRequest.build_from_message(message))

    @app.command("/clock-out")
    def record_clock_out_command(ack, command, say):
        ack()
        record_clock_out(say, SlackRequest.build_from_command(command))

    @app.message(re.compile("^休憩開始$"))
    def record_start_break_listener(message, say):
        record_start_break(say, SlackRequest.build_from_message(message))

    @app.command("/start-break")
    def record_start_break_command(ack, command, say):
        ack()
        record_start_break(say, SlackRequest.build_from_command(command))

    @app.message(re.compile("^休憩終了$"))
    def record_end_break_listener(message, say):
        record_end_break(say, SlackRequest.build_from_message(message))

    @app.command("/end-break")
    def record_end_break_command(ack, command, say):
        ack()
        record_end_break(say, SlackRequest.build_from_command(command))

    # setting
    @app.command("/employee-code")
    def employee_code_command(ack, command, say):
        ack()
        register_employee_code(say, SlackRequest.build_from_command(command))

    return app


# misc
# FIX ME react only @mention
# @app.event("message")
# def handle_message_events(event, say):
#     if re.search(r'感謝|ありがとう|好き|すごい', event['text']):
#         be_shy(say)
#     elif re.search(r'アレクサ|Alexa|alexa', event['text']):
#         i_am_not_alexa(say)
#     elif re.search(r'Hey Siri', event['text']):
#         i_am_not_siri(say)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    logger.info("start slackbot")

    app = create_app()

    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
