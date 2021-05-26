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
        self.j.test()
        self.j.k_func('open', 'HELLO.json')
        self.j.k_func('open', 'HELLO.txt')
        self.j.v_func('HELLO')
        self.j.k_func('save_as', './my_packages/JinjaObj/test_out.json')
        print('self.j.data: ', self.j.data)
        self.assertEqual(self.j.data, {'./my_packages/JinjaObj/test_out.json':{'json_jusc': 'HELLO.json', 'txt_open': 'HELLO.txt'}}, "Should be \{'json_jusc2': 'HELLO.json', 'txt_open': 'HELLO.txt'\}")

if __name__ == '__main__':
    unittest.main()
