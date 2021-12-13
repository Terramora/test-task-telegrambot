import requests as requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def get_requests_session(statuses: list[int] = None, retry_count: int = None,
                         retry_methods: list = None) -> requests.Session():
    """
    functions for settings retry strategy
    :param statuses: statusCode for try
    :param retry_count: count of try
    :param retry_methods: HTTP methods for try
    :return:
    """
    if not statuses:
        statuses = [429, 500, 502, 503, 504]
    if not retry_count:
        retry_count = 3
    if not retry_methods:
        retry_methods = ["GET", "POST", "PUT"]

    retry_strategy = Retry(
        total=retry_count,
        status_forcelist=statuses,
        method_whitelist=retry_methods,
        backoff_factor=1
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)

    return http
