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
            token='5033717880:AAE8PbRxh9p7E2XP2ucGUpZjqJI-WVQUuf4'
        )
    )
