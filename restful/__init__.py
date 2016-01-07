# coding=UTF-8
import logging
import warnings
import requests

warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('restful')


class RestfulClient:
    def __init__(self, base_url, username=None, password=None, verify=False):
        self.__base_url = base_url
        self.__session = requests.Session()
        self.__session.auth = (username, password) if username and password else None
        self.__session.verify = verify

    def request_get(self, path, parameters=None):
        resp = {}
        try:
            response = self.__session.get(url=self.__base_url + path, params=parameters,
                                            verify=self.__session.verify)
            resp.update({'status_code': response.status_code})
            resp.update(response.json())
        except Exception:
            log.warn('request get exception: %s', self.__base_url + path)
        return resp

    def request_post(self, path, payload=None, parameters=None):
        resp = {}
        try:
            response = self.__session.post(url=self.__base_url + path, json=payload, params=parameters,
                                             verify=self.__session.verify)
            resp.update({'status_code': response.status_code})
            resp.update(response.json())
        except Exception as e:
            log.warn('request get exception: %s', self.__base_url + path)
        return resp

    def request_delete(self, path, payload=None, parameters=None):
        resp = {}
        try:
            response = self.__session.delete(url=self.__base_url + path, json=payload, params=parameters,
                                               verify=self.__session.verify)
            resp.update({'status_code': response.status_code})
            resp.update(response.json())
        except Exception as e:
            log.warn('request get exception: %s', self.__base_url + path)
        return resp
