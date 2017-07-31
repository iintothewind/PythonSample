# coding=UTF-8
import logging
import os
import warnings

import requests
from tzlocal import get_localzone

warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-5s %(process)d:%(thread)d %(pathname)s:%(lineno)d %(message)s')
LOG = logging.getLogger('ewok-agent')
BASE_DIR = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
LOCAL_ZONE = get_localzone()



class RestClient:
    def __init__(self, base_url, username=None, password=None, verify=False, req_timeout=None):
        self.__base_url = base_url
        self.__session = requests.Session()
        self.__session.auth = (username, password) if username and password else None
        self.__session.verify = verify
        self.__req_timeout = req_timeout

    def rest(self, operation_function, path, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None,
             allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):
        """
        :param operation_function: a lambda, for request method, such as: lambda url, **kwargs: self.session.get(url, **kwargs) , or lambda url, **kwargs: self.session.post(url, **kwargs)
        :param path: the request url
        :param json: the request body in Json format
        :return: returns as much information as possible, if response.json() throws exception, it returns status code. if response.status_code() or http method have exception, it returns empty dict.
        """
        resp = {}
        response = {}
        try:
            response = operation_function(url=path if path.startswith("http") else self.__base_url + path, params=params, data=data,
                                          headers=headers, cookies=cookies, files=files,
                                          auth=auth or self.__session.auth, timeout=timeout or self.__req_timeout, allow_redirects=allow_redirects,
                                          proxies=proxies, hooks=hooks, stream=stream, verify=verify or self.__session.verify, cert=cert, json=json)
        except Exception as e:
            log.warn(e.message)
        try:
            resp.update({'json': response.json()})
        except:
            pass
        try:
            resp.update({'headers': response.headers})
        except:
            pass
        try:
            resp.update({'status_code': response.status_code})
        except:
            pass
        try:
            resp.update({'text': response.text})
        except:
            pass

        return resp

    def get(self, path, **kwargs):
        return self.rest(lambda url, **kvargs: self.__session.get(url, **kvargs), path, **kwargs)

    def post(self, path, **kwargs):
        return self.rest(lambda url, **kvargs: self.__session.post(url, **kvargs), path, **kwargs)

    def put(self, path, **kwargs):
        return self.rest(lambda url, **kvargs: self.__session.put(url, **kvargs), path, **kwargs)

    def delete(self, path, **kwargs):
        return self.rest(lambda url, **kvargs: self.__session.delete(url, **kvargs), path, **kwargs)
