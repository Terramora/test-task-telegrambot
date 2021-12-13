import requests

from bot.common import get_requests_session


class TelegramBot:
    URL = "https://api.telegram.org/bot"

    def __init__(self, token: str) -> None:
        self._token = token

    def _get_url(self, path: str) -> str:
        return self.URL + self._token + path

    def get_updates(self, offset: int = 0):
        path = '/getUpdates'

        return self.send_request(
            method='get',
            url=self._get_url(path=path),
            params={
                'offset': offset
            }
        )

    @staticmethod
    def send_request(method: str, url: str, params: dict = None, body: dict = None,
                     headers: dict = None) -> dict:
        http = get_requests_session()

        try:
            if method == 'get':
                response = http.get(url=url, params=params, headers=headers)
            elif method == 'post':
                response = http.post(url=url, params=params, json=body, headers=headers)
            elif method == 'put':
                response = http.put(url=url, params=params, json=body, headers=headers)
            else:
                response = None

        except requests.exceptions.ConnectionError as error:
            return {
                'ok': False,
                'result': error
            }
        else:
            return response.json()

    def send_message(self, chat_id: int, text: str, reply_to_message_id: int = None):
        path = '/sendMessage'

        params = {
            'chat_id': chat_id,
            'text': text
        }
        if reply_to_message_id:
            params['reply_to_message_id'] = reply_to_message_id

        return self.send_request(
            method='get',
            url=self._get_url(path=path),
            params=params
        )
