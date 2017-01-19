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

    def rest(self, operation_function, path, parameters=None, json=None):
        """
        :param operation_function: a lambda, for request method, such as: lambda url, **kwargs: self.session.get(url, **kwargs) , or lambda url, **kwargs: self.session.post(url, **kwargs)
        :param path: the request url
        :param parameters: the reuest parameters
        :param parameters: the request body in Json format
        :return: returns as much infomation as possible, if response.json() throws exception, it returns status code. if response.status_code() or http method have exception, it returns empty dict.
        """
        resp = {}
        path = path[path.find('/rest'):] if path.startswith(self.__base_url) else path
        try:
            response = operation_function(url=self.__base_url + path, params=parameters, json=json, verify=self.__session.verify)
            resp.update({'status_code': response.status_code})
            resp.update(response.json())
        except Exception as e:
            log.warn(e.message)
        return resp
