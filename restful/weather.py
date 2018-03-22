# coding=UTF-8
import unittest

from restful import LOG as log
from restful import RestClient


class WeatherReport:
    def __init__(self, appid, lang='zh_cn', base_url='http://api.openweathermap.org'):
        self.__appid = appid
        self.__lang = lang
        self.__rest_client = RestClient(base_url)

    def report_weather(self, city):
        param = {'appid': self.__appid, 'lang': self.__lang, 'q': city}
        return self.__rest_client.get('/data/2.5/weather', params=param)


class WeatherReportTest(unittest.TestCase):
    def setUp(self):
        self.weather_report = WeatherReport('c9af8741600c1db96759585d1b26a38e')

    def test_report_weather(self):
        report = self.weather_report.report_weather('Shanghai')
        for weather in report['json']['weather']:
            log.info('weather.main == %s', weather['main'])
            log.info('weather.description == %s', weather['description'])
