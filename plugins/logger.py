import datetime
import functools
import os


# Decorator
def write_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = MessageLogger()
        logger.write(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


class MessageLogger:
    DATA_DIR = os.path.join(os.environ['HOME'], '.kintai_paccho')
    LOG_DIR = os.path.join(DATA_DIR, 'log')

    def __init__(self):
        now = datetime.datetime.now()
        year_str = str(now.year)
        month_str = str(now.month)
        day_str = str(now.day)
        os.makedirs(os.path.join(self.LOG_DIR, year_str, month_str), exist_ok=True)
        filename = '{}.txt'.format(day_str)
        self.log_path = os.path.join(self.LOG_DIR, year_str, month_str, filename)

    def write(self, message):
        """
        :param message: slackbot.bot が渡してくれる message
        """
        ts_unix = message._body['ts'].split('.')[0]
        timestamp = datetime.datetime.fromtimestamp(int(ts_unix)).strftime('%Y-%m-%d %H:%M:%S')
        user = message.channel._client.users[message.body['user']]['name']
        text = message.body['text']
        log = '{}\t{}\t{}\n'.format(timestamp, user, text)
        f = open(self.log_path, 'a')
        f.write(log)
        f.close()
