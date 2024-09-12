import requests
import json
import time
from urllib.parse import urlparse, urlunparse

class Requests:
    def __init__(self, url, headers=None, params=None, timeout=10):
        self.url = url
        self.headers = headers if headers else {}
        self.params = params if params else {}
        self.timeout = timeout
        self.response = None

    def get(self):
        try:
            self.response = requests.get(self.url, headers=self.headers, params=self.params, timeout=self.timeout)
            self.response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print ("Something went wrong:", err)

    def get_response(self):
        return self.response

    def get_status_code(self):
        if self.response:
            return self.response.status_code
        else:
            return None

    def get_headers(self):
        if self.response:
            return self.response.headers
        else:
            return None

    def get_json(self):
        if self.response:
            return self.response.json()
        else:
            return None

    def get_text(self):
        if self.response:
            return self.response.text
        else:
            return None

    def get_url(self):
        return self.url

    def get_parsed_url(self):
        return urlparse(self.url)

    def get_unparsed_url(self, parsed_url):
        return urlunparse(parsed_url)

    def sleep(self, seconds):
        time.sleep(seconds)

    def __str__(self):
        return f"Requests instance for {self.url}"
