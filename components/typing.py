from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SlackRequest:
    channel_id: str  # 'C02HFC9H4CF'
    user_id: str  # 'U02HFC9GPC7'
    text: Optional[str]

    @classmethod
    def build_from_message(cls, params) -> "SlackRequest":
        return cls(
            channel_id=params['channel'],
            user_id=params['user'],
            text=params['text']
        )

    @classmethod
    def build_from_command(cls, params) -> "SlackRequest":
        return cls(
            channel_id=params['channel_id'],
            user_id=params['user_id'],
            text=params['text']
        )
