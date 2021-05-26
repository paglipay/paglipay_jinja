import unittest
import json
import DTree as d

class TestJinjaObj(unittest.TestCase):

    def setUp(self) -> None:
        json_file = './start1.json'
        flask_data = {}
        import_obj_instance = {}
        self.c = d.DTree(json.load(open(json_file)), name=json_file, import_obj_instance=import_obj_instance, data=flask_data)

    def tearDown(self) -> None:
        pass

    def test_obj(self):
        self.assertEqual(self.c.data, {'Key': ['Hello', 'World', 'BAD', 'GOOD', '3BAD', '3GOOD', 'GOOD', 'Hello', 'World', 'BAD', 'GOOD', '3BAD', '3GOOD', 'GOOD']}, "Should be \{'json_jusc2': 'HELLO.json', 'txt_open': 'HELLO.txt'\}")

if __name__ == '__main__':
    unittest.main()
