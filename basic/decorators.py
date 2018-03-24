import unittest
from functools import wraps
from time import sleep
from basic import log


def deco(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        log.debug("before method call: %s with args: %s", fn.func_name, ','.join(args))
        msg = fn(*args, **kwargs)
        log.debug("after method call: %s with args: %s", fn.func_name, ','.join(args))
        return msg

    return wrapper


def retry(attempts=3, after=1):
    def _decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            exception = None
            temp_dict = {'retry_attempts': 3 if attempts < 0 or attempts > 9 else attempts,
                         'retry_times': 0,
                         'retry_after': 1 if after < 0 or after > 600 else after}
            while temp_dict.get('retry_attempts') > 0:
                temp_dict['retry_times'] += 1
                try:
                    return fn(*args, **kwargs)
                except Exception as ex:
                    log.error('error: %s, failed at %s time, retry after %s seconds', ex or '', temp_dict['retry_times'],
                              temp_dict.get('retry_after'))
                    sleep(temp_dict.get('retry_after'))
                    temp_dict['retry_attempts'] -= 1
                    exception = ex
            if exception:
                raise exception

        return wrapper

    return _decorate


@deco
@retry()
def hello(name):
    if name is not "Python":
        raise Exception('not python error')
    return 'Hello, {}'.format(name)


class DecoratorTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_deco(self):
        hello('python')
