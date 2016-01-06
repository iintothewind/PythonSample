# coding=UTF-8
import unittest


class BasicTest(unittest.TestCase):
    def test_fibonacci(self):
        a, b = 0, 1
        while b < 10:
            print(b)
            a, b = b, a + b

    def test_if(self):
        x = -1
        if x < 0:
            x = 0
            print("Negative changed to zero")
        elif x == 0:
            print("Zero")
        elif x == 1:
            print("Single")
        else:
            print("More")

    def test_for(self):
        words = ['cat', 'window', 'defenestrate']
        for w in words:
            print(w, len(w))

    def test_range(self):
        for i in range(5):
            print(i)

        for i in range(0, 10, 3):
            print(i)

        a = ['Mary', 'had', 'a', 'little', 'lamb']
        for i in range(len(a)):
            print(i, a[i])

    def test_break(self):
        for n in range(2, 10):
            for x in range(2, n):
                if n % x == 0:
                    print(n, 'equals', x, '*', n // x)
                    break
                else:
                    print(n, 'is a prime number')

    def test_continue(self):
        for n in range(2, 10):
            if n % 2 == 0:
                print("Found an even number", n)
                continue
            print("Found an odd number ", n)

    def test_pass(self):
        pass  # do nothing

    def test_print(self):
        print("{0} is {2}, {1} is not {3}".format(1, 2, 4, 5))

    def test_ast(self):
        import ast
        string = "['Dony.LEE@email.com']"
        # string = '["Small", "Medium", "Large", "X-Large"]'
        for s in ast.literal_eval(string):
            print(s)

    def test_dict(self):
        args = {'cn': 'China', 'us': 'America', 'jp': 'Japan'}
        try:
            print(args['ge'])
        except Exception as e:
            print('get keyerror here, because ge is not existing in args')
        print(args.get('ge', 'Germany'))

    def fib(self, n):
        a, b = 0, 1
        while a < n:
            print(a)
            a, b = b, a + b
        print()

    def test_fib(self):
        self.fib(2000)

    def ask_ok(self, prompt, retries=4, complaint='Yes or no, please!'):
        while True:
            ok = prompt
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries -= 1
            if retries < 0:
                raise OSError('uncooperative user')
            print(complaint)

    @unittest.expectedFailure
    def test_ask(self):
        print(self.ask_ok('y'))
        print(self.ask_ok('n'))
        self.ask_ok('yeah')

    def tuple_parameters(self, *args):
        for arg in args:
            print(arg)

    def test_tuple_parameters(self):
        self.tuple_parameters("one", "two", "three", 4, 5, 6)

    def dict_parameters(self, **args):
        for key in args.keys():
            print(key, " -> ", args[key])

    def test_dict_parameter(self):
        self.dict_parameters(us="Washington", cn="Beijing", fr="Paris")

    def make_inc(self, n):
        return lambda x: x + n

    def test_make_inc(self):
        inc = self.make_inc(1)
        print(inc(9))

    def test_doc_str(self):
        print("""Everything comes with a price
Never say no to any obstacles
Protect your dream""")


if __name__ == '__main__':
    unittest.main()
