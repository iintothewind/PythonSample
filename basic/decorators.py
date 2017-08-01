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
    temp_dict = {'retry_attempts': 3 if attempts < 0 or attempts > 5 else attempts,
                 'retry_after': 1 if after < 0 or after > 6 else after}

    def _decorate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            exception = None
            while temp_dict.get('retry_attempts') > 0:
                try:
                    return fn(*args, **kwargs)
                except Exception as ex:
                    log.info('retry after %s seconds', temp_dict.get('retry_after'))
                    sleep(temp_dict.get('retry_after'))
                    temp_dict['retry_attempts'] -= 1
                    exception = ex
            raise RuntimeError('error: {} while running function {}()'.format(exception.message, fn.func_name))

        return wrapper

    return _decorate


@deco
@retry()
def hello(name):
    if name is not "Python":
        raise Exception('not python error')
    return 'Hello, {}'.format(name)


class DecoratorTest(unittest.TestCase):
    def test_deco(self):
        hello('python')
