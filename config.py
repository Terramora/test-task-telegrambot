from dataclasses import dataclass


@dataclass
class Telegram:
    token: str


@dataclass
class Config:
    telegram: Telegram


def get_config():
    return Config(
        telegram=Telegram(
            token='token'
        )
    )
