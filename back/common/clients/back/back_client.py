import requests


class BackClient(object):
    def __init__(self, base_url):
        self._base_url = base_url

    def business_logic(self):
        return requests.request(method='GET', url=self._base_url + '/business_logic')

    def get_count(self):
        return requests.request(method='GET', url=self._base_url + '/')
