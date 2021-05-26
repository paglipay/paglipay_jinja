import unittest
from my_packages import JinjaObj as jo

class TestJinjaObj(unittest.TestCase):

    def setUp(self) -> None:
        data = {}
        self.j = jo('test jo', data)

    def tearDown(self) -> None:
        pass

    def test_obj(self):
        self.assertEqual(self.j.data, {}, "Should be \{\}")

    # @unittest.skip("WIP")
    def test_obja(self):
        assert self.j.data == {}, "Should be \{\}"

    def test_obj2(self):
        data = {}
        # j = jo('test jo', data)    
        self.j.test()
        self.j.k_func('open', 'HELLO.json')
        self.j.k_func('open', 'HELLO.txt')
        self.j.v_func('HELLO')
        self.assertEqual(self.j.data, {'json_jusc': 'HELLO.json', 'txt_open': 'HELLO.txt'}, "Should be \{'json_jusc2': 'HELLO.json', 'txt_open': 'HELLO.txt'\}")

if __name__ == '__main__':
    unittest.main()
