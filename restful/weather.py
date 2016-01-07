# coding=UTF-8
from restful import log
from restful import RestfulClient


class WeatherReport:
    def __init__(self, appid, lang='zh_cn', base_url='http://api.openweathermap.org'):
        self.__appid = appid
        self.__lang = lang
        self.__restful_client = RestfulClient(base_url)

    def report_weather(self, city):
        param = {'appid': self.__appid, 'lang': self.__lang, 'q': city}
        return self.__restful_client.request_get('/data/2.5/weather', param)


import unittest


class WeatherReportTest(unittest.TestCase):
    def setUp(self):
        self.weather_report = WeatherReport('c9af8741600c1db96759585d1b26a38e')

    def test_report_weather(self):
        report = self.weather_report.report_weather('Shanghai')
        for weather in report['weather']:
            log.info('weather.main == %s', weather['main'])
            log.info('weather.description == %s', weather['description'])
